# library import
import pwn

# read a png
luigi = open("2.luigi.png", "rb").read()

# read the cipher and encode to bytes
cipher = open("cipher.enc", "r").read()
cipher = bytes.fromhex(cipher)

# xor first 16 bytes of both to get key
key = pwn.xor(cipher[:16], luigi[:16])

# xor key with cipher to get plaintext
image = pwn.xor(key, cipher)

# write output to file to get image
f = open("output.png", "wb").write(image)
