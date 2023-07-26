##li = list(map(int,input().strip().split()))
##for i in range(len(li),0,-1):
##    a = max(li[:i])
##    b = li.index(a)
##    li[b],li[i-1] = li[i-1],li[b]
##print(*li)
##
##53 54 52 5 2
def square_area(a): #create a module square.py
    a=int(input())
    return a*a
