# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode(0)
        curr=dummy
        #loops over linked lists until both are empty
        while l1 or l2:
            val1=l1.val if(l1) else 0
            val2=l2.val if(l2) else 0
            #adding carry value to sum
            addition=val1+val2+carry
            #it handels carry efficeintly
            carry=addition//10
            #creating a node of lastdigit of the valuw
            lastdigit=ListNode(addition%10)
            curr.next=lastdigit
            curr=curr.next
            #used to handle NULL nodes
            l1=l1.next if(l1) else None
            l2=l2.next if(l2) else None
        if(carry):
            curr.next=ListNode(carry)
        return dummy.next

        