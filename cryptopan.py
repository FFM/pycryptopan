#   pycryptopan - a python module implementing the CryptoPAn algorithm
#   Copyright (C) 2013 - the CONFINE project

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU Lesser General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from functools import reduce
from Crypto.Cipher.AES import AESCipher as AES

class CryptoPanError(Exception):
  def __init__(self,value):
    self.value=value
  
  def __str__(self):
    return repr(self.value)

class CryptoPan():
  
  def __init__(self,key):
    if len(key)!=32:
      raise CryptoPanError("Key must be a 32 byte long string")
    self.aes=AES(key[0:16])
    self.pad=self.aes.encrypt(key[16:32])

    f4=self.pad[0:4]
    # Python 2 requires explicit conversion to ints
    if isinstance(f4, str):
      f4=[ord(x) for x in f4]
      
    f4bp=self.toint(f4)
    self.masks=[(mask,f4bp & (~ mask)) for mask in (0xFFFFFFFF >> (32-p) << (32-p) for p in range(0,32))]

  def toint(self,array):  
    return array[0]<<24|array[1]<<16|array[2]<<8|array[3]
  
  def toarray(self,n):
    for i in range(3,-1,-1):
      yield (n>>(i*8))& 0xFF

  def anonymize(self,ip):
    result=0
    address=[int(x) for x in ip.split(".")]
    if len(address)!=4:
      raise CryptoPanError("Invalid IPv4 Address")
   
    address=self.toint(address)
    
    def calc(a):
      """ calculate the first bit for Crypto-PAN"""
      a_array = self.toarray(a)

      # Python 2 requires converting ints to chars one at a time
      if isinstance(self.pad, str):
        inp="".join((chr(x) for x in a_array))
      else:
        inp=bytes(a_array)

      inp+=self.pad[4:]
      rin_output=self.aes.encrypt(inp)

      out=rin_output[0]
      # Python 2 requires explicit conversion to int
      if isinstance(out, str):
        out=ord(out)

      return out>>7 
    
    addresses=((address & mask[0]) | mask[1] for mask in self.masks)
    result=reduce(lambda x,y: x<<1 | y, (calc(a) for a in addresses),0)
    
    return ".".join(["%s"%x for x in self.toarray(result ^ address)])


if __name__=="__main__":
  import time
  c=CryptoPan("".join((chr(x) for x in range(0,32))))
  print("expected: 2.90.93.17")

  print("calculated: "+c.anonymize("192.0.2.1"))
  print("starting performance check")
  stime=time.time()
  for i in range(0,1000):
    c.anonymize("192.0.2.1")
  dtime=time.time()-stime
  print("1000 anonymizations in %s s"%dtime)
