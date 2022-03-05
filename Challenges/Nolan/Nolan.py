import random
import time

seed1 = int(time.time())
random.seed(seed1)

with open('flag.txt', 'r') as f:
    flag = f.read().strip()

t = [random.randint(0,255) for _ in flag]
cipher = []
x = 0
for i in flag:
    cipher.append(ord(i) ^ t[x])
    x += 1

cipher = ''.join(chr(_) for _ in cipher)
with open('cipher.enc', 'w', encoding='utf-8') as f:
    f.write(cipher)
