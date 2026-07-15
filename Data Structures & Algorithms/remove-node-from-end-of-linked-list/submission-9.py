# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        We can face this problem using two pointers:
        - initially the first at the head, the other tries to stay n + 1 places ahead
        - When the second reaches the position, they go on one pos at a time
        - When second.next == None, then first.next = first.next.next
        """
        dummy = ListNode(0,head)
        first, second = dummy, head
        for i in range(n):
            second = second.next

        while second != None:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next