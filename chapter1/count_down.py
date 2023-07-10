inp = input("*** Fun with countdown ***\nEnter List : ")
numbers = [int(num) for num in inp.split()]
i = len(numbers)-1
res = [0, []]
while(i>=0): 
    if(numbers[i]==1):
        temp = [1]
        i-=1
        while(i>=0 and numbers[i]==numbers[i+1]+1):
            temp = [numbers[i]] + temp
            i-=1
        res[0] += 1
        res[1] = [temp] + res[1]
    else:
        i-=1
print(res)