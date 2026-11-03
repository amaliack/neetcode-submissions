# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # find cutoff point
        cut = (length + 1) // 2
        second = head
        link_node = None
        for i in range(cut):
            link_node = second
            second = second.next
        # disconnect first half
        link_node.next = None

        # reverse second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev
        while first and second:
            first_temp = first.next
            second_temp = second.next

            first.next = second
            second.next = first_temp

            first = first_temp
            second = second_temp       
                        