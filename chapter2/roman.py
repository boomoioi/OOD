class translator:

    def deciToRoman(self, num):
        res = ""
        sym = ["M", "CM", "D", "CD", "C", "XC",
               "L", "XL", "X", "IX", "V", "IV", "I"]
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        while (num > 0):
            res += sym[i]*(num//val[i])
            num -= val[i]*(num//val[i])
            i += 1
        return res

    def romanToDeci(self, s):
        res = 0
        roman = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
        }
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        res += roman[s[-1]]
        return res
    
num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
