# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow = head
        fast = head
        while True:
            slow = slow.next
            if fast.next: fast = fast.next.next
            else: return False
            if not slow or not fast:
                break
            if slow.val == fast.val:
                return True

        return False