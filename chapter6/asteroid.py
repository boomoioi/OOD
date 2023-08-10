def asteroid_collision(asts):
    if asts == []:
        return []
    
    tail = asteroid_collision(asts[1:])
    asts = [asts[0]]
    while asts and tail and asts[0] > 0 and tail[0] < 0:
        if abs(asts[0]) > abs(tail[0]):
            tail = tail[1:]
        elif abs(asts[0]) < abs(tail[0]):
            asts = []
        else:
            asts = []
            tail = tail[1:]
    return asts + tail

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))
