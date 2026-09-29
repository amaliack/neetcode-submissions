# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. input constraints --> heads of two lists, the length of each being at least 0
        2. empty input --> the heads can be null, empty so we have to handle this
        3. positive/negative --> can have both
        4. sorted input --> each individual list is sorted, we need to merge into one
        5. duplicates --> not relevant
        6. modify input --> yes, we need to modify the lists for the merged one
        7. edge cases --> when lists are different lengths

        brute force --> we could maybe read into an array, sort and rebuild a list from scratch
        invariant:
        - this forces extra space
        - we can use two pointers, one for each list and then move them based on their values
        - and then if diff length, we fill with the rest of the linked list
        """

        p1 = list1
        p2 = list2
        new_list = dummy = ListNode()
        
        while p1 and p2:
            if p1.val < p2.val:
                new_list.next = p1
                p1 = p1.next
            else:
                new_list.next = p2
                p2 = p2.next
            new_list = new_list.next
        
        new_list.next = p1 if p1 else p2
        return dummy.next













