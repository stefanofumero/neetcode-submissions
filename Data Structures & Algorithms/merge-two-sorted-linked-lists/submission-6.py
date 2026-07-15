# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        res = cur_res = None
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                new_node = ListNode(cur1.val,None)
                cur1 = cur1.next
            else:
                new_node = ListNode(cur2.val,None)
                cur2 = cur2.next
            if cur_res:
                cur_res.next = new_node
                cur_res = cur_res.next
            else:
                cur_res = new_node
                res = cur_res

        while cur1:
            new_node = ListNode(cur1.val,None)
            if cur_res:
                cur_res.next = new_node
                cur_res = cur_res.next
            else:
                cur_res = new_node
                res = cur_res
            cur1 = cur1.next

        while cur2:
            new_node = ListNode(cur2.val,None)
            if cur_res:
                cur_res.next = new_node
                cur_res = cur_res.next
            else:
                cur_res = new_node
                res = cur_res
            cur2 = cur2.next

        return res

        