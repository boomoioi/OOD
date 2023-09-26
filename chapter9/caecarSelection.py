class Monkey:
    ID = 0 
    def __init__(self, st):
        attr = st.split()
        self.name = attr[0]
        self.str = int(attr[1])
        self.int = int(attr[2])
        self.agi = int(attr[3])
        self.id = Monkey.ID
        Monkey.ID += 1
    
    def getAttribute(self, attr): 
        if attr == "str":
            return self.str
        elif attr == "int":
            return self.int
        elif attr == "agi":
            return self.agi
        elif attr == "name":
            return self.name
        else:
            raise ValueError(f'No attribute named {attr}')
    
    def compare(self, other, attr_list, order):
        if order == "A":
            for attr in attr_list: 
                if self.getAttribute(attr) < other.getAttribute(attr):
                    return True
                elif self.getAttribute(attr) > other.getAttribute(attr):
                    return False
            
        else:
            for attr in attr_list: 
                if self.getAttribute(attr) < other.getAttribute(attr):
                    return False
                elif self.getAttribute(attr) > other.getAttribute(attr):
                    return True
        return True
            
            
    def __str__(self) -> str:
        return f"{self.id}-{self.name}"
  
def merge(arr1, arr2, attr_list, order):
    res = []
    i,j = -0,0 
    while i<len(arr1) and j<len(arr2): 
        if arr1[i].compare(arr2[j], attr_list, order): 
            res.append(arr1[i])
            i+=1 
        else: 
            res.append(arr2[j])
            j+=1
    while i<len(arr1): 
        res.append(arr1[i])
        i+=1 
    while j<len(arr2): 
        res.append(arr2[j])
        j+=1     
    return res
    
def mergeSort(arr, attr_list, order): 
    if len(arr) <= 1: 
        return arr
    mid = int(len(arr)//2)
    left = mergeSort(arr[:mid], attr_list, order)
    right = mergeSort(arr[mid:], attr_list, order)
    return merge(left, right, attr_list, order)  
    
def sortMonkey(attr_list, monkey_list, order):
    if not attr_list:
        return monkey_list
    return mergeSort(monkey_list, attr_list, order)
    
inp = input("Enter Input: ").split("/")
order = inp[0]
if not inp[1]:
    attr_list = []
else:
    attr_list = inp[1].split(",")
monkeys = inp[2].split(",")
monkey_list = []
for monkey in monkeys:  
    monkey_list.append(Monkey(monkey))
if attr_list:
    monkey_list = mergeSort(monkey_list, attr_list, order)
print(f"[{', '.join([f'{monkey}' for monkey in monkey_list])}]")