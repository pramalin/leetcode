# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize pointers
        slow = head
        fast = head
        result = None

        # move slow once, move fast twice
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (fast == slow):
                result = True
                break

        return result