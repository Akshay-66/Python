li = list(map(int,input().strip().split()))
for i in range(len(li),0,-1):
   a = max(li[:i])
   b = li.index(a)
   li[b],li[i-1] = li[i-1],li[b]
print(*li)


