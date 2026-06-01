# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        #Bit Manupulation
        curr=head
        res=0
        while curr:
            res=res<<1
            res=res|curr.val
            curr=curr.next
        return res