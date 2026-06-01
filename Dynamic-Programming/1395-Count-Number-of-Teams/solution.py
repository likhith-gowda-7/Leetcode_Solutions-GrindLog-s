class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l=len(rating)
        res=0
        #considering j as middle element and finding value accordinglly
        for j in range(l):
            #for increasing order checking small<middle(j)<greater
            left_smaller=0
            right_greater=0
            #for decreasing order checking small>middle(j)>greater
            left_greater=0
            right_smaller=0
            for i in range(0,j):
                if(rating[i]<rating[j]):
                    left_smaller+=1
                elif(rating[i]>rating[j]):
                    left_greater+=1
            for i in range(j+1,l):
                if(rating[i]>rating[j]):
                    right_greater+=1
                elif(rating[i]<rating[j]):
                    right_smaller+=1
            #for increasing order
            res+=left_smaller*right_greater
            #for decreasing order
            res+=left_greater*right_smaller
        return res