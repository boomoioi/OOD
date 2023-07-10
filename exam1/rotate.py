first, second = input("*** String Rotation ***\nEnter 2 strings : ").split()
copy1, copy2 = first, second
i=1
while(i==1 or copy1 != first or copy2 != second):
    copy1 = copy1[-2:] + copy1[:-2]
    copy2 = copy2[3:] + copy2[:3]
    if i<=5:
        print(f"{i} {copy1} {copy2}")
    i+=1
if(i>6):
    print(" . . . . . ")
    print(f"{i-1} {copy1} {copy2}")
print(f"Total of  {i-1} rounds.")