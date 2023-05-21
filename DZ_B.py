n=0
for i in range(100, 1000):
    if len(set(str(i)))<3: n=n+1
print(n)
n=0