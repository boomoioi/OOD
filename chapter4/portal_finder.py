inp = input("Enter width, height, and room: ").split()
col = int(inp[0])
row = int(inp[1])

matrix = []
pos = ()
if len(inp[2].split(",")) != row:
    print("Invalid map input.")
    exit()
for i in range(row):
    inp_row = inp[2].split(",")[i]
    if len(inp_row) != col:
        print("Invalid map input.")
        exit()
    temp = []
    for j in range(col): 
        if inp_row[j] == "F":
            pos = (j, i)
        temp.append(inp_row[j])
    matrix.append(temp)
if not pos:
    print("Invalid map input.")
    exit()
passed =  [[0 for i in range(col)] for j in range(row)]

def isokay(matrix, x, y):
    row_count = len(matrix)
    col_count = len(matrix[0])
    if x<0 or y<0 or x>col_count-1 or y>row_count-1:
        return 0
    if matrix[y][x] == "O":
        return 2
    if matrix[y][x] != "_":
        return 0 
    if passed[y][x] != 0:
        return 0
    return 1


def bfs(matrix, f_pos):
    adder = [(0,-1), (1,0), (0,1), (-1,0)]
    q = []
    q.append(f_pos)
    while q:
        print("Queue:", q)
        latest = q.pop(0)
        x = latest[0]
        y = latest[1]
        passed[y][x] = 1
        if matrix[y][x] == "O":
            print(x, y)
            return 1  
        for add in adder:
            status = isokay(matrix, x+add[0], y+add[1])
            if status == 2:
                print("Found the exit portal.")
                return 1
            elif status:
                q.append((x+add[0], y+add[1]))
                passed[y+add[1]][x+add[0]] = 1
    print("Cannot reach the exit portal.")
    return 0

bfs(matrix, pos)

