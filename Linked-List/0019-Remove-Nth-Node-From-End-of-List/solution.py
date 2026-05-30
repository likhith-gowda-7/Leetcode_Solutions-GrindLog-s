# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        k=n
        while curr and k>0:
            curr=curr.next
            k-=1
        prev=None
        s=head
        while curr:
            prev=s
            curr=curr.next
            s=s.next
        if(prev==None):
            return s.next
        else:
            prev.next=s.next
        return head