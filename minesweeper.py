def counter(ini, inj, mine_map, length):
    count = 0
    if mine_map[ini][inj] == '#':
        return '#' 
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (ini == 0 and i == -1) or (inj == 0 and j == -1):
                continue
            elif (ini == length-1 and i == 1) or (inj == length-1 and j == 1):
                continue
            elif mine_map[ini+i][inj+j] == '#':
                count += 1
    return str(count)


inp = input().split(",")
mine_map = [row.split(" ") for row in inp]
length = len(mine_map)
ans_map = [['+' for i in range(length)] for j in range(length)]

for i in range(length):
    for j in range(length):
        ans_map[i][j] = counter(i, j, mine_map, length)
for row in ans_map:
    print(row)