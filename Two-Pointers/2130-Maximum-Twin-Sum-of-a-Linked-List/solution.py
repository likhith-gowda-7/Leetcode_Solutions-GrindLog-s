# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        idx=0
        idx_map={}
        res=0
        curr=head
        while curr:
            idx_map[idx]=curr.val
            idx+=1
            curr=curr.next
        for i in range((idx//2)):
            twin_idx=(idx-i)-1
            twin_sum=idx_map[i]+idx_map[twin_idx]
            res=max(res,twin_sum)
        return res