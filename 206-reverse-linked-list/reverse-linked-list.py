# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # Recursive
        def solve(head):
            if not head or not head.next:
                return head
            temp=solve(head.next)
            head.next.next=head
            head.next=None
            return temp
        return solve(head)
        