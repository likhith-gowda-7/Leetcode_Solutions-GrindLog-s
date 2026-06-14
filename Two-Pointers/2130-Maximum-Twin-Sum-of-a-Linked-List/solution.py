# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=0
        fast=head
        slow=head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            Next=slow.next
            slow.next=prev
            slow,prev=Next,slow
        while slow:
            twin_sum=prev.val+slow.val
            res=max(res,twin_sum)
            prev=prev.next
            slow=slow.next
        return res