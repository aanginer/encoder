import os

def liststr(l: list):
  string = ""
  for i in l:
    string += str(i)

  return string

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return liststr(m)

def binarystring(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))


class Encoder:
    def __init__(self,data: dict,name: str,game: str):
        self.first = True
        self.data_str = str(data)
        self.data = data
        self.encoded = ''
        self.decoded = ''
    
    def encode(self):
        self.encoded = binarystring(toBinary(self.data_str).replace('0','0_p').replace('1','0').replace('0_p','1'))
        self.encoded.replace('a')
