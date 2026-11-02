# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        q=[(node.val,ind,node) for ind,node in enumerate(lists) if node]
        heapq.heapify(q)
        dummy=tail=ListNode()
        while q:
            val,ind,node=heapq.heappop(q)
            tail.next=node
            if node.next:
                heapq.heappush(q,(node.next.val,ind,node.next))
            tail=tail.next
        return dummy.next

        