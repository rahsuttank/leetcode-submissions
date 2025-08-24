# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        hsh = set()
        while slow:
            if slow in hsh:
                return slow
            hsh.add(slow)
            slow = slow.next
        else:
            return None
        
        # print(slow.val)

        # return slow
        