import json,itertools
digits={int(k):bytes.fromhex(v) for k,v in json.load(open('keypad/Keypad-Oracle.app/KeypadConfig.json'))['digits'].items()}
salt=bytes.fromhex('3a91442fd0186bc3720ea95d11be8027f466399a05cc701b8842e153')
def rotate(x,n):return ((x<<n)|(x>>(8-n)))&255
for direction in [1,-1]:
 for pin in itertools.permutations(range(10),4):
  out=bytearray(len(digits[0]))
  for pos,d in enumerate(pin):
   a=digits[d]
   for i in range(len(out)):
    x=a[i%len(a)]^((pos+1)*33)^((d*19)&255)^((i*7)&255)
    out[i]^=rotate(x,((d+pos+i)*direction)%8)^((i+d+pos*11)&255)
  out=bytes(x^s for x,s in zip(out,salt))
  if b'deadface' in out or all(32<=c<127 for c in out):print(pin,direction,out)

