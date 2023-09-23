def merge(arr1, arr2):
    res = []
    i,j = -0,0 
    while i<len(arr1) and j<len(arr2): 
        if arr1[i]<arr2[j]: 
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

def addSortToOrig(arr, sorted_arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] >= 0: 
            arr[i] = sorted_arr[j]
            j+=1
    return " ".join([str(num) for num in arr])

nums = [int(x) for x in input("Enter Input : ").split()]
pos_nums = [x for x in nums if x>=0]
print(addSortToOrig(nums, mergeSort(pos_nums)))