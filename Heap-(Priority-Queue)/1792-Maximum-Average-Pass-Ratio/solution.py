class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap=[]
        n=len(classes)
        def diff(p,t):
            #used to find the gain
            return ((p+1)/(t+1))-((p)/(t))
        for passed,total in classes:
            gain=diff(passed,total)
            #max-heap
            heap.append((-gain,passed,total))
        heapify(heap)
        while extraStudents>0:
            #we check the gaining by trying add 1 extra students to maximum gain ensuring classes(heap top)
            gain,passed,total=heappop(heap)
            passed+=1
            total+=1
            gain=diff(passed,total)
            heappush(heap,(-gain,passed,total))
            extraStudents-=1
        res=0
        for _,score,total in heap:
            res+=score/total
        return res/n
