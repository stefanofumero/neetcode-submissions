# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        # Find the half of the list
        s,f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        second_half = s.next
        s.next = None

        # reverse the second half
        cur, prev = second_half, None

        while cur:
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp

        reversed_list = prev

        # result
        node = head
        while reversed_list:
            tmp1,tmp2 = node.next, reversed_list.next
            node.next = reversed_list
            reversed_list.next = tmp1
            node, reversed_list = tmp1,tmp2

