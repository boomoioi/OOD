class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class HashTable:
    def __init__(self, max_size, max_collision):
        self.max_size = max_size
        self.max_collision = max_collision
        self.table = [None] * max_size
        self.items = 0
        
    def sumASCII(self, text:str) -> int:
        sum = 0
        for ch in text:
            sum += ord(ch)
        return sum
        
    def hash(self, data:Data) -> None:
        if self.items == self.max_size:
            print("This table is full !!!!!!")
            exit()
        
        index = self.sumASCII(data.key)%self.max_size
        i = 0
        for coll in range(self.max_collision):
            cur_index = (index + i*i)%self.max_size
            if self.table[cur_index] != None:
                print(f"collision number {coll+1} at {cur_index}")
            else: 
                self.table[cur_index] = data
                self.items += 1
                break
            if coll >= self.max_collision-1:
                print("Max of collisionChain")
            i+=1

        self.showTable()

    def showTable(self):  
        for i in range(1, self.max_size+1):
            print(f"#{i}	{self.table[i-1]}")
        print("---------------------------")
        
        
inp = input(" ***** Fun with hashing *****\nEnter Input : ").split("/")
hash_props = inp[0].split()
data_list = [Data(data.split()[0], data.split()[1]) for data in inp[1].split(",")]
hashTable = HashTable(int(hash_props[0]), int(hash_props[1]))
for data in data_list:
    hashTable.hash(data)