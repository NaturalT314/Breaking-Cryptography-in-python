# library imports
import pwn
import base64
import os

# open file and read contents as bytes
image = open("welcome.png", "rb").read()

# choose 16 random bytes from /dev/urandom
x = os.urandom(16)

# xor the image with the 16 random bytes
output = pwn.xor(image, x)

# encode output as hex
output = bytes.hex(output)

# output result of xor into file named challenge.enc
outputFile = open("cipher.enc", "w").write(output)

# uncomment to reveal hint
# x = "Rmlyc3QgMTYgYnl0ZXMgb2YgYW55IHBuZyBmaWxlIGFyZSBjb25zdGFudA=="
# print(base64.b64decode(x))
