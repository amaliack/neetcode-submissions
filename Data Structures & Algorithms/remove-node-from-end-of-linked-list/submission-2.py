# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        rev = reverseList(head)

        # case 1: we delete the last node (first in reversed list)
        if n == 1:
            return reverseList(rev.next)

        # case 2: we find the nth node
        curr = rev
        count = 1
        while curr and count < n - 1:
            curr = curr.next
            count += 1
        curr.next = curr.next.next

        return reverseList(rev)

        