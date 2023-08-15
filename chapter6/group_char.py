def count_group(st, index, min, max, target):
    if index>max or index<min or st[index]!=target:
        return 0
    left = count_group(st, index-1, min, index-1, target)
    right = count_group(st, index+1, index+1, max, target)
    return 1+left+right
def solve(st, pos):
    if not st:
        print("Output : List is entry")
        return
    if pos>len(st):
        print("Output : Pin number out of range")
        return 
    if pos<1:
        print("Output : Pin number less than 1")
        return
    print(f"Character : {st[pos-1]}")
    print(f"Count : {count_group(st, pos-1, 0, len(st)-1, st[pos-1])}")
    
    
inp = input("input number : ")
solve(inp.split(",")[0], int(inp.split(",")[1]))
    