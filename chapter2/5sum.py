inp = input("Enter Your List : ").split()
nums = [int(num) for num in inp]

if len(nums)<3:
    print("Array Input Length Must More Than 2")
else:
    nums.sort()
    res=[]
    length = len(nums)-2
    for i in range(length):
        if nums[i]>5:
            break
        if i>0 and nums[i-1]==nums[i]:  #skipping if we found the duplicate of i
            continue 
        j=i+1
        k=length+1
        while j<k: 
            sum=nums[i]+nums[j]+nums[k] 
            if sum>5:
                k-=1
            elif sum<5:
                j+=1
            else:
                res.append([nums[i],nums[j],nums[k]])
                j+=1 
                while nums[j-1]==nums[j] and j<k:
                    j+=1   
    print(res)