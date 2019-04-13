import math

a = [int(input()) for i in range(6)]
b = min([a[n] for n in range(1,6)])
print(math.ceil(a[0]/b)+4)
