class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if(letters[mid]>target):
                r=mid-1
            else:
                l=mid+1
        return letters[l] if(0<=l<n) else letters[0]