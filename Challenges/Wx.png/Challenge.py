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

# output result of xor into file named challenge.enc
outputFile = open("cipher.enc", "wb").write(output)


x = "Rmlyc3QgMTYgYnl0ZXMgb2YgYW55IHBuZyBmaWxlIGFyZSBjb25zdGFudA=="

# uncomment to reveal hint
# print(base64.b64decode(x))
