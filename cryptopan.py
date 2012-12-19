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
    self.first4bytes_pad=[ord(x) for x in self.pad[0:4]]

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
    
    def calc(a,result,offset):
      inp= "".join([chr(x) for x in a])+self.pad[4:]
      rin_output=self.aes.encrypt(inp)
      return result |  ord(rin_output[0])>>7 <<offset

    result=calc(self.first4bytes_pad,result,31)
    for position in range(1,32):
      mask = 0xFFFFFFFF >> (32-position) << (32-position)
      first4bytes_input = (address & mask) | (self.toint(self.first4bytes_pad) & (~ mask))
      result=calc(self.toarray(first4bytes_input),result,31-position)
    
    return ".".join(["%s"%x for x in self.toarray(result ^ address)])


if __name__=="__main__":
  c=CryptoPan("".join([chr(x) for x in range(0,32)]))
  print "expected: 2.90.93.17"

  print "calculated: "+c.anonymize("192.0.2.1")
