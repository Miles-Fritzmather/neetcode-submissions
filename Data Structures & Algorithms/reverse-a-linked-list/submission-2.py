# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev




    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head == None: return None
        
    #     stack = []
    #     node = head
    #     while node is not None:
    #         stack.append(node.val)
    #         node = node.next

    #     root = ListNode(stack[-1], None)
    #     node = root
    #     i = len(stack) - 1
    #     while i > 0:
    #         i -= 1
    #         node.next = ListNode(stack[i], None)
    #         node = node.next

    #     return root