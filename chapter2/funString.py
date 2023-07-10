class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        res = ""
        for ch in self.string:
            if ch >= 'a' and ch <= 'z':
                res += chr(ord(ch)-32)
            elif ch >= 'A' and ch <= 'Z':
                res += chr(ord(ch)+32)
        self.string = res
        return self.string

    def reverse(self):
        res = ""
        for i in range(len(self.string)-1, -1, -1):
            res += self.string[i]
        self.string = res
        return self.string

    def deleteSame(self):
        seen = []
        res = ""
        for ch in self.string:
            if ch not in seen:
                seen.append(ch)
                res += ch 
        self.string = res
        return self.string



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    
    print(res.size())
elif str2 == "2":  
    print(res.changeSize())
elif str2 == "3" : 
    print(res.reverse())
elif str2 == "4" : 
    print(res.deleteSame())