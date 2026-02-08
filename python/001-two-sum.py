from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                if ((a + b) == target):
                    return [i, i + j + 1]

        return []

sol = Solution()

# nums = [2,7,11,15]
# target = 9
nums = [2,5,5,11]
target = 10

print ("Input: nums =", nums, ", target =", target)
print (sol.twoSum(nums, target))

