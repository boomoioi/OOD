def boxFinder(nums, box):
    for i in range(max(int(s//box), max(nums)), s+1):
        box_i = 1
        cur_sum = 0
        for num in nums: 
            cur_sum += num
            if cur_sum > i:
                box_i+=1
                cur_sum = num  
        if box_i == box:
            return i
        
nums, box = input("Enter Input : ").split('/')
nums = [int(x) for x in nums.split()]
box = int(box)
s = sum(nums)
print(f"Minimum weigth for {box} box(es) = {boxFinder(nums, box)}")