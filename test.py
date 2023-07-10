to_print = ".#"

def print_even(index, width):
    index += 1
    print(to_print*(index//2) + "."*(width-(2*index)-1) + to_print*(index//2+1))

def print_odd(index, width):
    index += 1
    print(to_print*(index//2) + "#"*(width-(2*index)-1) + to_print*(index//2))
    
n = int(input(""))
width = 4*n-3
print("#"*width)
for i in range(0, width//2):
    if(i%2==0):
        print("#", end="")
        print_even(i, width)
    else:
        print("#", end="")
        print_odd(i, width)

for i in range(width//2-2, -1, -1):
    if(i%2==0):
        print("#", end="")
        print_even(i, width)
    else:
        print("#", end="")
        print_odd(i, width)

print("#"*width)
