# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while True:
            if not fast or not fast.next:
                return False
            fast=fast.next
            if fast.next:
                fast=fast.next
            
            if fast==slow:
                return True
            slow=slow.next