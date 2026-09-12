# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Possible problems here: don't forget to set fast and slow equal to head at the beginning,
        not head and head.next

        Then, first update pointers then check whether they're equal

        Additionally, in the while condition check whether both fast and fast.next are not null,
        otherwise you risk an exception!
        """
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False

