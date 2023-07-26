def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left,right)

def merge(a,b):
    i,j = 0,0
    final = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            final.append(a[i])
            i += 1
        else:
            final.append(b[j])
            j += 1
    while i < len(a):
        final.append(a[i])
        i += 1
    while j < len(b):
        final.append(b[j])
        j += 1
    return final

li = list(map(int,input().strip().split()))
print(mergeSort(li))
