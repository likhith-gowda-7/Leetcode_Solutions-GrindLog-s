# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #the technique here is to connect tail back to head and make the rotational last node point to null. this stimulate the rotation behaviour...
        if(not head or not head.next or k==0):
            return head
        curr=head
        n=1
        while curr.next:
            n+=1
            curr=curr.next
        #connect tail back to head
        curr.next=head
        k=n-(k%n)
        curr=head
        i=1
        while curr:
            if(i==k):
                new_head=curr.next
                curr.next=None
                return new_head
            i+=1
            curr=curr.next 