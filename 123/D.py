k = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

A = sorted(a, reverse=True)[:k[3]]
B = sorted(b, reverse=True)[:k[3]]
C = sorted(c, reverse=True)[:k[3]]

ab = sorted(list(ax+bx for ax in A for bx in B), reverse=True)[:k[3]]
abc = sorted(list(aby+cy for aby in ab for cy in C), reverse=True)[:k[3]]
for i in abc: print(i)
