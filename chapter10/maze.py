rc, nums = input("input : ").split(",")
col = int(rc.split()[0])
row = int(rc.split()[1])
nums = [int(x) for x in nums.split()]
min_index = nums.index(min(nums))
start = col * int(min_index//col)
max_index = nums.index(max(nums[start:start+col]))
max_col = max_index%col
print(max([nums[i] for i in range(max_col, row*col, col)]))