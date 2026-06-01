# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        curr=head
        count=0
        while curr:
            l.append((curr.val,count,curr))
            curr=curr.next
            count+=1
        l.sort()
        dummy=ListNode(0)
        curr=dummy
        for i in range(len(l)):
            curr.next=l[i][2]
            curr=curr.next
        curr.next=None
        return dummy.next