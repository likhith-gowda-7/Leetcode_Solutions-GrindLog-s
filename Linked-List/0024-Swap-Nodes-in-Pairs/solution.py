# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while head:
            if(prev):
                head.val,prev.val=prev.val,head.val
                prev=None
            else:
                prev=head
            head=head.next
        return curr