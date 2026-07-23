# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        
        slow = head
        fast = head.next
        while fast is not None and slow != fast:
            slow = slow.next

            fast = fast.next
            if fast is None: return False
            fast = fast.next

        return fast is not None