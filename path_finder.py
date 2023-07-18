row, col = input("Enter row col : ").split()
row = int(row)
col = int(col)

matrix = []
posr, posc = -1, -1
for i in range(row):
    inp_row = input()
    temp = []
    for j in range(col): 
        if inp_row[j] == "F":
            posr=i
            posc=j
        temp.append(inp_row[j])
    matrix.append(temp)

class POS:
    def __init__(self, posr, posc, where_from):
        self.posr = posr
        self.posc = posc
        self.where_from = where_from

def bfs(matrix, posr, posc):
    q = []
    q.append(POS(posr, posc, 0))
    while q:  
        latest = q.pop(0)
        if latest.posr>len(matrix)-1 or latest.posr<0 or latest.posc>len(matrix[0])-1 or latest.posc<0:
            continue
        if matrix[latest.posr][latest.posc] == "O":
            return 1
        if matrix[latest.posr][latest.posc] != "F" and matrix[latest.posr][latest.posc] != "_":
            continue
        if latest.where_from != 3:
            q.append(POS(latest.posr-1, latest.posc, 1))
        if latest.where_from != 4:
            q.append(POS(latest.posr, latest.posc+1, 2))
        if latest.where_from != 1:
            q.append(POS(latest.posr+1, latest.posc, 3))
        if latest.where_from != 2:
            q.append(POS(latest.posr, latest.posc-1, 4))
        
    return 0

def dfs(matrix, posr, posc, ri, ci):
    posr += ri
    posc += ci
    if posr>len(matrix)-1 or posr<0 or posc>len(matrix[0])-1 or posc<0:
        return 0
    if matrix[posr][posc] == "O":
        return 1
    if matrix[posr][posc] != "F" and matrix[posr][posc] != "_":
        return 0   
    
    if ri == -1:
        return dfs(matrix, posr, posc, -1, 0) or dfs(matrix, posr, posc, 0, 1) or dfs(matrix, posr, posc, 0, -1)
    elif ri == 1:
        return dfs(matrix, posr, posc, 0, 1) or dfs(matrix, posr, posc, 1, 0) or dfs(matrix, posr, posc, 0, -1)
    elif ci == -1:
        return dfs(matrix, posr, posc, -1, 0) or dfs(matrix, posr, posc, 1, 0) or dfs(matrix, posr, posc, 0, -1)
    elif ci == 1:
        return dfs(matrix, posr, posc, -1, 0) or dfs(matrix, posr, posc, 0, 1) or dfs(matrix, posr, posc, 1, 0)
    
    return dfs(matrix, posr, posc, -1, 0) or dfs(matrix, posr, posc, 0, 1) or dfs(matrix, posr, posc, 1, 0) or dfs(matrix, posr, posc, 0, -1)

print(bfs(matrix, posr, posc))