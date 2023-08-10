lst = input("Enter your List : ").split(",")
nums = [int(x) for x in lst]

def sorter(nums):
    if len(nums) == 1:
        return nums
    max_val = max(nums)
    index = nums.index(max_val)
    return [max_val] + sorter(nums[:index]+nums[index+1:])

nums = sorter(nums)
print("List after Sorted :", nums)