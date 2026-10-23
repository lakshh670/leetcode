# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        temp=dummy
        temp1,temp2=l1,l2
        s,carry=0,0
        while temp1 and temp2:
            s=temp1.val+temp2.val+carry
            carry,digit=s//10,s%10
            temp.next=ListNode(digit)
            temp=temp.next
            temp1,temp2=temp1.next,temp2.next
        while temp1:
            s=temp1.val+carry
            carry,digit=s//10,s%10
            temp.next=ListNode(digit)
            temp=temp.next
            temp1=temp1.next
        while temp2:
            s=temp2.val+carry
            carry,digit=s//10,s%10
            temp.next=ListNode(digit)
            temp=temp.next
            temp2=temp2.next
        if carry:
            temp.next=ListNode(carry)
        return dummy.next