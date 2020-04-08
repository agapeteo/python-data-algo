# base = 10
base = 2

x = 2

while x > 0:
    digit = x % base
    print digit
    x //= base

