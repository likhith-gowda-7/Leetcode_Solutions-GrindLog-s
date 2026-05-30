# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        while head:
            if(head and head.val==val):
                while head and head.val==val:
                    head=head.next
                curr.next=head
            else:
                curr=curr.next
                head=head.next
        return dummy.next

        