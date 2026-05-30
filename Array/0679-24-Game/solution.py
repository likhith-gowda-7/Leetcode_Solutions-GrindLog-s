class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = [operator.add,operator.sub,operator.mul,operator.truediv]
        def dfs(arr):
            if(len(arr)==1):
                return abs(arr[0]-24) < 1e-6
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if(i!=j):
                        a,b=arr[i],arr[j]
                        rest=[arr[k] for k in range(len(arr)) if(k!=i and k!=j)]
                        for op in ops:
                            if(op==operator.truediv and b==0):
                                continue
                            try:
                                result=op(a,b)
                                if(dfs(rest+[result])):
                                    return True
                            except:
                                continue
            return False
        return dfs(cards)

                            
