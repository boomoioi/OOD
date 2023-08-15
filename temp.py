input = "154 151 147 150 164"
res = ""
import binascii
res = ""
for word in input.split():
    n = int(word)
    res += chr(n)
    
print(res)