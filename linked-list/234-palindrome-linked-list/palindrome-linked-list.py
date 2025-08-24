# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left, right = head, head
        pali = []
        while(left is not None):
            pali.append(left.val)
            left = left.next
        
        leng = len(pali) - 1
        for i in range(len(pali) // 2):
            if(pali[i] != pali[leng - i]):
                return False
        return True
        
        
        