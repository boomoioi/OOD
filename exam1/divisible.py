num = int(input(" *** Divisible number ***\nEnter a positive number : "))
if(num<=0):
    print("0 is OUT of range !!!")
else:
    res = []
    for i in range(1, num+1):
        if(num%i == 0):
            res.append(i)
    print("Output ==>", end="")

    for number in res: 
        print(" " + str(number), end="")
    print()
    print(f"Total ==> {len(res)}")