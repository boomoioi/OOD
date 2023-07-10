class MyInt():
    def __init__(self, inp):
        self.num = inp 
    
    def toRoman(self):
        res = ""
        copy = self.num
        sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        val = [1000, 900, 500, 400, 100, 90, 50 , 40, 10, 9, 5, 4, 1]
        i=0
        while(copy>0):
            res += sym[i]*(copy//val[i])
            copy -= val[i]*(copy//val[i])
            i+=1
        return res

    def __add__(self, other):
        temp  = self.num + other.num
        temp  += temp//2
        return temp
    
    def __str__(self):
        return str(self.num)

inp1, inp2 = input(" *** class MyInt ***\nEnter 2 number : ").split()
a = MyInt(int(inp1))
b = MyInt(int(inp2))
print(f"{a} convert to Roman : {a.toRoman()}")
print(f"{b} convert to Roman : {b.toRoman()}")
print(f"{a} + {b} = {a+b}")
