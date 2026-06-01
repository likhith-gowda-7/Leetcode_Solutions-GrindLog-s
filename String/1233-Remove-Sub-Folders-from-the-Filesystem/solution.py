class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res=[folder[0]]
        for fold in folder[1:]:
            parent=res[-1]+"/"
            if(not fold.startswith(parent)):
                res.append(fold)
        return res