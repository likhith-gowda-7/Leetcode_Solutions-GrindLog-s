class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        h1=set()
        max_length=0
        def solve(num):
            curr=num
            while curr:
                h1.add(curr)
                curr//=10
        for val in arr1:
            solve(val)
        for val in arr2:
            curr=val
            l=0
            found=False
            while curr:
                if(curr in h1):
                    found=True
                if(found):
                    l+=1
                curr//=10
            max_length=max(max_length,l)
        return max_length