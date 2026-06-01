# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        slow.next=None
        prev=None
        while temp:
            Next=temp.next
            temp.next=prev
            prev=temp
            temp=Next    
        first=head
        last=prev
        while last:
            t1,t2=first.next,last.next
            first.next,last.next=last,t1
            first,last=t1,t2
        
        