import math

a = [int(input()) for i in range(5)]
b = [x%10 if x%10!=0 else 10 for x in a]
c = [math.ceil(x/10)*10 for x in a]
d = 10 if any(b) else 0
print(sum(c)-d+min(b))
