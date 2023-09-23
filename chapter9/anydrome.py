def anydrome(st): 
    ascend = False
    decend = False 
    dup = 0
    seen = set() 
    seen.add(st[0])
    for i in range(1, len(st)): 
        if st[i] > st[i-1]: 
            ascend = True
        if st[i] < st[i-1]:
            decend = True
        if st[i] in seen: 
            dup +=1 
        seen.add(st[i]) 
    if ascend and decend: 
        return "Nondrome"
    elif dup == len(st)-1:
        return "Repdrome"
    elif ascend and not dup: 
        return "Metadrome"
    elif ascend and dup: 
        return "Plaindrome"
    elif decend and not dup: 
        return "Katadrome"
    elif decend and dup: 
        return "Nialpdrome"
       
print(anydrome(input("Enter Input : ")))