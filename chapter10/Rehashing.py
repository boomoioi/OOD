class HashTable:
    def __init__(self, table_size, max_collision, treshold):
        self.table_size = table_size
        self.max_collision = max_collision
        self.treshold = treshold
        self.data_list = []
        self.table = [None] * table_size
        self.items = 0
        print("Initial Table :")
        self.showTable()
        
    def isPrime(self, num):
        if num <= 1:
            return False

        for i in range(2, num//2):
            if (num % i) == 0:
                return False
        return True
        
    def nextPrime(self): 
        start = self.table_size*2
        while True:
            if self.isPrime(start):
                return start
            start += 1
        
    def hash(self, data): 
        
        print(f'Add : {data}')
        if (self.items+1)/self.table_size >= self.treshold/100:
            print("****** Data over threshold - Rehash !!! ******")
            self._rehash()
        self.data_list.append(data)
        if self._hash(data) == 2:
            print("****** Max collision - Rehash !!! ******")
            self._rehash()
        self.showTable()
        
    def _rehash(self):
        self.table_size = self.nextPrime()
        self.table = [None] * self.table_size
        for d in self.data_list:
            self._hash(d)
            self.items -= 1
        
    def _hash(self, data) -> None:
       
        index = data%self.table_size
        i = 0
        for coll in range(self.max_collision):
            cur_index = (index + i*i)%self.table_size
            if self.table[cur_index] != None:
                print(f"collision number {coll+1} at {cur_index}")
            else: 
                self.table[cur_index] = data
                self.items += 1
                return 1
            if coll >= self.max_collision-1:
                return 2
            i+=1

    def showTable(self):  
        for i in range(1, self.table_size+1):
            print(f"#{i}	{self.table[i-1]}")
        print("----------------------------------------")
        
        
inp = input(" ***** Rehashing *****\nEnter Input : ").split("/")
hash_props = inp[0].split()
data_list = [int(x) for x in inp[1].split()]
hashTable = HashTable(int(hash_props[0]), int(hash_props[1]), int(hash_props[2]))
for data in data_list:
    hashTable.hash(data)