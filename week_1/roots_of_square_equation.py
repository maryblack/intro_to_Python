import sys
from math import sqrt
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

def roots(a, b, c):
    D = b**2 - 4*a*c
    d1 = (-b+sqrt(D))/(2*a)
    d2 = (-b-sqrt(D))/(2*a)
    return int(d1), int(d2)

if __name__ == "__main__":
    d1, d2 = roots(a, b, c)
    print(f'{d1}\n{d2}')