def comparator(f, s): 
    if f[0] >= s[0]:
        return True
    return False

def merge(arr1, arr2):
    res = []
    i,j = -0,0 
    while i<len(arr1) and j<len(arr2): 
        if comparator(arr1[i],arr2[j]): 
            res.append(arr1[i])
            i+=1 
        else: 
            res.append(arr2[j])
            j+=1
    while i<len(arr1): 
        res.append(arr1[i])
        i+=1 
    while j<len(arr2): 
        res.append(arr2[j])
        j+=1     
    return res
    
def mergeSort(arr): 
    if len(arr) <= 1: 
        return arr
    mid = int(len(arr)//2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

inp = [int(x) for x in input("input : ").split()]
pairs = []
for i in range(0,len(inp), 2): 
    pairs.append((inp[i:i+2]))
pairs = mergeSort(pairs) 
sum = 0 
for i in range(len(pairs)-1):
    for j in range(i+1, len(pairs)):
        if pairs[i][0]>pairs[j][0] and pairs[i][1]<pairs[j][1]:
            sum += pairs[i][0] + pairs[j][0]
print(f"ans = {sum}")