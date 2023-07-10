inp = int(input("*** Fun with Drawing ***\nEnter input : "))

print("."*(inp-1) + "*" + "."*(2*(inp)-3) + "*" + "."*(inp-1))

for i in range(inp-2, 0, -1):
    print("."*(i) + "*" + "+"*(2*(inp-i-2)+1) + "*" + "."*(2*(i)-1) + "*" + "+"*(2*(inp-i-2)+1) + "*" + "."*(i))

print("*" + "+"*(2*(inp)-3) + "*" + "+"*(2*(inp)-3) + "*")

for i in range(1, 2*inp-2):
    print("."*(i) + "*" + "+"*(2*((2*inp-3)-i)+1) + "*" + "."*(i))

print("."*(2*inp-2) + "*" + "."*(2*inp-2))
