# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        output = ListNode(0)
        output_tail = output
        tmp = 0 
        
        while l1 or l2 or tmp:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            
            tmp, remain = divmod(val1 + val2 + tmp, 10)
            
            output_tail.next = ListNode(remain)
            output_tail = output_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return output.next