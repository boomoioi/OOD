def sequence(nums): 
    res = []
    mx = 0
    for i in range(len(nums)): 
        end = len(res)
        for j in range(len(res)-1, -1, -1): 
            if res[j] >= nums[i]:
                end = j
        res = res[:end]
        res.append(nums[i])
        if len(res) > mx:
            mx = len(res)
            
        print(f"{i+1} : {res}")
    print("longest increasing subsequence :", mx)

nums = [int(x) for x in input("Data : ").split()]
sequence(nums)