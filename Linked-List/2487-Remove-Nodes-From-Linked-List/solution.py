# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            Next=curr.next
            curr.next=prev
            prev=curr
            curr=Next
        curr=prev
        maxi=ListNode(0)
        prev=None
        while curr:
            Next=curr.next
            if(curr.val>=maxi.val):
                curr.next=prev
                prev=curr
                maxi=curr
            curr=Next
        return prev
