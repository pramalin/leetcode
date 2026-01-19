"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    """
    def isPalindrome(self, s: str) -> bool:
        left = 0
        end = len(s) - 1;
        right = end
        while (right >= 0 and left < end):
            # skip non-alphanumeric characters
            if(not s[left].isalnum()):
                left += 1
            elif (not s[right].isalnum()):
                right -= 1
            elif (s[left].lower() == s[right].lower()):
                left += 1
                right -= 1
            else:
                return False
        return True
    """
    # Copilot optimized version
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the filtered string is equal to its reverse
        return filtered_s == filtered_s[::-1]


sol = Solution()

input = "amanaplanacanalpanama"
print(f"{input} is palindrome: {sol.isPalindrome(input)}")

input = "A man, a plan, a canal: Panama"
print(f"{input} is palindrome: {sol.isPalindrome(input)}")

input = "race a car"
print(f"{input} is palindrome: {sol.isPalindrome(input)}")

input = " "
print(f"{input} is palindrome: {sol.isPalindrome(input)}")

input = ".a"
print(f"{input} is palindrome: {sol.isPalindrome(input)}")
