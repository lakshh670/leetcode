# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        k=right-left
        # My apprach:
        # def reverse(first_node,last_node):
        #     stack=[]
        #     temp=first_node
        #     for i in range(k):
        #         stack.append(temp)
        #         temp=temp.next
        #     head=temp
        #     while stack:
        #         temp.next=stack.pop()
        #         temp=temp.next
        #     temp.next=last_node
        #     return head
        # last_node=head
        # for i in range(right):
        #     last_node=last_node.next
        # first_node=head
        # if left==1:
        #     first_node=reverse(first_node,last_node)
        #     return first_node
        # for i in range(left-2):
        #     first_node=first_node.next
        # first_node.next=reverse(first_node.next,last_node)
        # return head

        # Cleaner appraoch
        if left==right or head is None:
            return head
        dummy=ListNode(0,head) # Concept of dummy node
        
        list_prev=dummy
        for i in range(left-1):
            list_prev=list_prev.next
        prev=None
        curr=list_prev.next
        for _ in range(k):
            forw=curr.next
            curr.next=prev
            prev=curr
            curr=forw
        list_prev.next.next=curr.next
        list_prev.next=curr
        curr.next=prev
        return dummy.next
        
        