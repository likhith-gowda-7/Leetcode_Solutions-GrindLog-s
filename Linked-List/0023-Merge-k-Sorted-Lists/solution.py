# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(not lists):
            return None
        min_heap=[]
        for i in range(len(lists)):
            curr=lists[i]
            while curr:
                min_heap.append(curr.val)
                curr=curr.next
        heapq.heapify(min_heap)
        root=None
        if(min_heap):
            val=heapq.heappop(min_heap)
            root=ListNode(val)
        curr=root
        while min_heap:
            n=heapq.heappop(min_heap)
            curr.next=ListNode(n)
            curr=curr.next
        return root
