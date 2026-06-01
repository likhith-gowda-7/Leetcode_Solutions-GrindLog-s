# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(not head and k==1):
            return head
        #function for getting the kth node
        def has_knodes(curr,k):
            while curr and k>0:
                curr=curr.next
                k-=1
            return curr
        dummy=ListNode(0,head)
        prev_group_end=dummy
        while True:
            #kth node
            kth_node=has_knodes(prev_group_end,k)
            #if kth node is None,it means its end so break the loop
            if(not kth_node):
                break
            #starting node of the next group
            next_group=kth_node.next
            #prev is starting node of the next group and curr is starting node of the current group
            prev,curr=next_group,prev_group_end.next
            #reverse till the kth node
            while curr!=next_group:
                Next=curr.next
                curr.next=prev
                prev=curr
                curr=Next
            #after reverse,Connect prev group end to kth node
            start=prev_group_end.next
            prev_group_end.next=kth_node
            #now current group becomes preveous group
            prev_group_end=start
        return dummy.next
        