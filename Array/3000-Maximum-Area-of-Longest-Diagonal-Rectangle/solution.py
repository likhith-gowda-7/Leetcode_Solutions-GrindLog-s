class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_length=0
        max_area_of_rectangle=0
        for h,w in dimensions:
            diag_len=pow(h,2)+pow(w,2)
            if(diag_len>max_diag_length):
                max_diag_length=diag_len
                max_area_of_rectangle=h*w
            elif(diag_len==max_diag_length):
                max_area_of_rectangle=max(h*w,max_area_of_rectangle)
        return max_area_of_rectangle