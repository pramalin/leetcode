from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        
        for i in range(n):
            complement = target - nums[i]
            if complement in dict1:
                return [dict1[complement], i]
            dict1[nums[i]] = i
            print(f"complement: {complement} dict1: {dict1}")

            
sol = Solution()

# nums = [2,7,11,15]
# target = 9

nums = [2,5,5,11]
target = 10

print ("Input: nums =", nums, ", target =", target)
print (sol.twoSum(nums, target))

