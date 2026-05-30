# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        c=0
        if(head):
            while head.next:
                c+=1
                if(head.val!=head.next.val):
                    if(c==1):
                        curr.next=head
                        curr=curr.next
                    c=0
                head=head.next
            curr.next=None
            if(c==0):
                curr.next=head
        return dummy.next

                
        