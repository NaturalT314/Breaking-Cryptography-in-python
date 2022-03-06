# library imports
import pwn

# read cipher and encode as bytes
input = open("cipher.txt", "r").read()
input = bytes.fromhex(input)

# xor cipher with your known plaintext to get key
flag = b"HTB{"
key = pwn.xor(flag, input[:4])

# xor key with cipher to get plaintext
pt = pwn.xor(key, input)

print(pt)
