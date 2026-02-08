from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            print(f"left: {left}, mid: {mid}, right: {right}")

            if nums[mid] > nums[right]: # minimum is in the right half
                left = mid + 1
            else:
                right = mid
        return nums[left]
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) >> 1
            print(f"low: {low}, mid: {mid}, high: {high}")

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
        """
sol = Solution()
"""
num = [3,4,5,1,2]
print(f"sol.findMin({num}): {sol.findMin(num)}") # 1
"""

num = [2,1]
print(f"sol.findMin({num}): {sol.findMin(num)}") # 1
