def deleteIsland(Map,y,x):
    if y<0 or x<0 or y>=len(Map) or x>= len(Map[0]) or Map[y][x]==0:
        return Map
    Map[y][x] = 0
    Map = deleteIsland(Map,y-1,x)
    Map = deleteIsland(Map,y,x+1)
    Map = deleteIsland(Map,y+1,x)
    Map = deleteIsland(Map,y,x-1)
    return Map

def countIsland(Map):
    count = 0
    for i in range(len(Map)):
        for j in range(len(Map[0])):
            if Map[i][j] == 1:
                count += 1
                Map = deleteIsland(Map, i, j)
    return count

Input = input("Enter Input : ").split('/')

Map=[]

for i in Input:

    temp=[*i]

    temp = list(map(int,temp))

    Map.append(temp)
print(f"Island have : {countIsland(Map)}")