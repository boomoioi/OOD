def permu(inp):
    if len(inp) == 1:
        return [inp]
    all = permu(inp[1:])
    res = []
    for sub_list in all:
        for i in range(len(inp)):
            res.append(sub_list[:i] + [inp[0]] + sub_list[i:])
    return res
print(permu([3,2,1,1]))