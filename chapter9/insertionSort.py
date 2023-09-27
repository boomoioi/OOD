def insertionSort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > cur: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
        print(f"Round {i} {arr}")  
 
inp = list(map(int, input("Enter list for number: ").split(",")))
print("Before sort:", inp)
insertionSort(inp)
print("After sort:", inp)