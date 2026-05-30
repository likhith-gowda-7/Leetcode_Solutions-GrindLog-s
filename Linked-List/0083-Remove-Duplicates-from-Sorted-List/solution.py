# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-200)
        curr=dummy
        while head:
            if(head.val!=curr.val):
                curr.next=head
                curr=curr.next
            head=head.next
        curr.next=None
        return dummy.next

        