# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev=None
        curr=head
        st=dummy
        pos=0
        while curr:
            pos+=1
            if(pos>=left):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            else:
                st=st.next
                curr=curr.next
            if(pos==right):
                break
        #Connecting tail of revesed nodes to start(left-1) next
        tail=st.next
        st.next=prev
        tail.next=curr
        return dummy.next
        