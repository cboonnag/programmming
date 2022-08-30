# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = list_tmp = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                list_tmp.next = list1
                list1 = list1.next
            else:
                list_tmp.next = list2
                list2 = list2.next
            list_tmp = list_tmp.next
        if list1:
            list_tmp.next = list1
        else:
            list_tmp.next = list2
        return result_list.next
        