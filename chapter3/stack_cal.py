class StackCalc():
    def __init__(self):
        self.s = []
    
    def dup(self):
        self.s.append(self.s[-1])

    def pop(self):
        return self.s.pop()

    def push(self, item):
        self.s.append(item)

    def getValue(self):
        if not self.s:
            return 0
        return int(self.s.pop())

    def run(self, st):
        opers = st.split()
        sym = ['+', '-', '*', '/']
        for oper in opers:
            if oper in sym:
                first = str(self.pop())
                second = str(self.pop())
                self.push(eval(first+oper+second))
            elif oper == "DUP":
                self.dup()
            elif oper == "POP":
                self.pop()
            elif oper>='0' and oper<='9':
                self.push(int(oper))
            else:
                print(f"Invalid instruction: {oper}")
                exit()

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())