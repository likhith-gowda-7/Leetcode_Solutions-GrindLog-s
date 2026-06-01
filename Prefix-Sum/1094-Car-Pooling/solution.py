class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi=max(trips,key=lambda i:i[2])[2]
        diff_arr=[0]*(maxi+1)
        #fill the diff array
        for no,pick,drop in trips:
            diff_arr[pick]+=no
            diff_arr[drop]-=no
        #filling the range
        for i in range(1,maxi+1):
            diff_arr[i]+=diff_arr[i-1]
        for seats_taken in diff_arr:
            if(seats_taken>capacity):
                return False
        return True