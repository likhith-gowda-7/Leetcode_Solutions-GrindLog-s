class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        if(n==0):
            return []
        num_letters={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res=[]
        def backtrack(curr_idx,sol):
            if(len(sol)==n):
                res.append("".join(sol))
                return
            for ch in num_letters[digits[curr_idx]]:
                sol.append(ch)
                backtrack(curr_idx+1,sol)
                sol.pop()
        backtrack(0,[])
        return res
       