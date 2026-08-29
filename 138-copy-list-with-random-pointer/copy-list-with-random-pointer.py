"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        new_head=Node(head.val) if head else None
        temp=new_head
        dic=defaultdict(Node)
        dic[head]=new_head
        while head:
            if head.next in dic:
                next_node=dic[head.next]
            else:
                next_node=Node(head.next.val) if head.next else None
                dic[head.next]=next_node
            if head.random in dic:
                random_node=dic[head.random]
            else:
                random_node=Node(head.random.val) if head.random else None
                dic[head.random]=random_node
            temp.next=next_node
            temp.random=random_node
            temp=temp.next
            head=head.next
        return new_head
        