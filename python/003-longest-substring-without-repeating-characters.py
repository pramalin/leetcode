"""
Given a string s, find the length of the longest substring without duplicate characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       if (len(s) == 1):
          return 1
       
       subs = []
       for i in range(len(s)):
         sub = {s[i]} 
         for j in range(i+1, len(s)):
            if(not s[j] in sub):
              sub.add(s[j])
            else:
                break
         subs.append(sub)

       print(f"subs: {subs}")
       subs_lengths = [len(sub) for sub in subs]
       max_length = max(subs_lengths) if subs_lengths else 0
       return max_length

# copilot optimized version using sliding window technique
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # To store unique characters in the current window
        left = 0  # Left pointer of the sliding window
        max_length = 0

        for right in range(len(s)):
            # If the character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set and update max_length
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            print(f"right: {right}, left: {left}, char_set: {char_set}, max_length: {max_length}")
        return max_length
    
sol = Solution2()

s = "abcabcbb"
print("Input: s =", s)
print(sol.lengthOfLongestSubstring(s))

s = " "
print(sol.lengthOfLongestSubstring(s))

s = "au"
print(sol.lengthOfLongestSubstring(s))
