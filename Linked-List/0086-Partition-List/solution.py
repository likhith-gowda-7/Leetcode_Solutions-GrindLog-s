# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than=ListNode(-1)
        st1=less_than
        greater_than=ListNode(-1)
        st2=greater_than
        curr=head

        while curr:
            if(curr.val<x):
                st1.next=curr
                st1=st1.next
            else:
                st2.next=curr
                st2=st2.next
            curr=curr.next
        #Connecting both less than and greater than
        st1.next=greater_than.next
        st2.next=None
        return less_than.next