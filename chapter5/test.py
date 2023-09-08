class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(self.permutation([str(i) for i in range(1, n+1)])[k-1])
    
    def permutation(self, nums):
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)): 
            temp  = self.permutation(nums[:i] + nums[i+1:])
            for item in temp: 
                res.append([nums[i]] + item)
        return res
    
sol = Solution()

print(sol.getPermutation(9, 219601))