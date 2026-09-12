# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) ->    Optional[ListNode]:
        """
        Here the trick to solve the entire problem is in the first row: remind to create a 
        dummy node, put in front of the list, useful when handling the list to start from is 
        not that simple.

        Don't forget to keep node = node.next
        """
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
            

        