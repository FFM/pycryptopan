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
    print address
    rin_input="".join([chr(x) for x in self.first4bytes_pad])
    rin_input=rin_input+self.pad[4:]
    rin_output=self.aes.encrypt(rin_input)
    result = result | ord(rin_output[0])>>7<<31
    for position in range(1,32):
      first4bytes_input = ((address >> (32-position)) << (32-position)) | (((self.toint(self.first4bytes_pad) << position) & 0xFFFFFFFF) >> position)

      rin_input="".join([chr(x) for x in self.toarray(first4bytes_input)])
      rin_input=rin_input+self.pad[4:]
      rin_output=[ord(x) for x in self.aes.encrypt(rin_input)]
      result = result | (rin_output[0]>>7) << (31-position)
    
    return ".".join(["%s"%x for x in self.toarray(result)])
