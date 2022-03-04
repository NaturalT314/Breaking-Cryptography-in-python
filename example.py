# library imports
from matplotlib.pyplot import ylabel
import pwn

# data definition
x = 0
y = "Hello World"

# print statement
print(y)
print(f"formatted print: {y}")

# for loop
for i in range(0, 10):
    x = x + 1

for c in y:
    x = ord(c)
# indentation is important

# If statements
if x == 10:
    print(1)
    print("x equals 10")

if "Hello" in y:
    print('"Hello" in y is true')

# file read
setup = open("setup.sh", "r").read()

# ease of type cast
y = y.encode()
print(y)
y = y.decode()
print(y)

# String slicing
z = hex(123)
print(z)
z = z[2:]
print(z)
