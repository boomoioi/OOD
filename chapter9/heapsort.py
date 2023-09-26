def heapify(arr, N, i): 
    smallest  = i
    l = 2*i + 1 
    r = 2*i + 2
    if l < N and arr[l] < arr[smallest]:
        smallest = l
    if r < N and arr[r] < arr[smallest]:
        smallest = r
        
    if smallest != i: 
        arr[i], arr[smallest] = arr[smallest], arr[i]
        arr = heapify(arr, N, smallest)
    
def heapSort(arr): 
    for i in range(len(arr)//2 -1 , -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        
    return arr
    
nums = [int(x) for x in input("Enter Input : ").split()]
print(heapSort(nums))
    
# 0 1 2 3 4 5 6 7 8 9 10
# 7 8 9 7 3 0 4 2 6 5