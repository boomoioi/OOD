def summary(n):
    sum = 0
    for i in range(1, n+1): 
        sum += 1/(i*(i+2))
    return sum 

print(summary(int(input("Enter N : "))))