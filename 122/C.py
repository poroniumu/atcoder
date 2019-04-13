import itertools
n,q = map(int,input().split())
s = input()
lr = []
for i in range(q): lr.append(list(map(int, input().split())))
ac = [1 if i!=0 and 'AC'==s[i-1:i+1] else 0 for i in range(0,len(s))]
acc = list(itertools.accumulate(ac))
for i in lr: print(acc[i[1]-1]-acc[i[0]-1])
