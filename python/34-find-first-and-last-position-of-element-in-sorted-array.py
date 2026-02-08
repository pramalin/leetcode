from typing import List

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int, leftMost: bool) -> int:
            left = 0
            right = len(nums) - 1
            index = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else : 
                    index = mid
                    if leftMost:
                        right = mid - 1
                    else:
                        left = mid + 1
            return index
        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)
        
        return [left, right]


sol = Solution()

nums, target = [5,7,7,8,8,10], 8 # Output: [3,4]
print(f"sol.searchRange({nums}, {target}): {sol.searchRange(nums, target)}")

nums, target = [5,7,7,8,8,10], 6 # [-1,-1]
print(f"sol.searchRange({nums}, {target}): {sol.searchRange(nums, target)}")

nums, target = [], 0 # [-1,-1]
print(f"sol.searchRange({nums}, {target}): {sol.searchRange(nums, target)}")
