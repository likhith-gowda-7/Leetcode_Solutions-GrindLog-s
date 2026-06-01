class Solution:
    def findContentChildren(self, childrens: List[int], cookies: List[int]) -> int:
        if(not cookies):
            return 0
        childrens.sort()
        cookies.sort()
        n=len(childrens)
        i=0
        for cookie in cookies:
            if(i<n and cookie>=childrens[i]):
                i+=1
        return i
