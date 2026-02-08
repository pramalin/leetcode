from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}, mid: {mid}, high: {high}")

            if (nums[mid] == target):
                return mid

            if(nums[low] <= nums[mid]):
                if (nums[low] <= target and target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1 
            else: 
                if(nums[mid] <= target and target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1 
        return -1
    
sol = Solution()

nums = [7, 0, 1, 2, 3, 4, 5, 6]
target = 5
#4
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")

nums = [4,5,6,7,0,1,2]
target = 0
#4
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")

nums = [4,5,6,7,0,1,2]
target = 3
# Output: -1
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")


nums = [1]
target = 0
# Output: -1
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")

nums = [1, 3]
target = 2
# Output: -1
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")


nums = [1]
target = 1
# Output: 0
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")

nums = [1]
target = 2
# Output: 0
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")

nums = [1, 3, 5]
target = 1
# Output: 0
print(f"sol.search({nums}, {target}): {sol.search(nums, target)}")


"""
nums = [4,5,6,7,0,1,2]
target = 0


nums = [1, 3, 5]
target = 1

"""