class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        flip1 = 0
        flip2 = 0
        ops = ["0", "1"]
        curr = 1
        mini = n
        for i in range(n):
            if s[i] != ops[curr]:
                flip1 += 1
            else:
                flip2 += 1
            curr ^= 1
        curr=1
        Found=False
        if(n%2==1):
            curr=0
            Found=True
        for i in range(n):
            if s[i] != str(curr):
                flip1 += 1
            else:
                flip2 += 1
            if(Found):
                curr^=1
            if s[i] != str(curr):
                flip1 -= 1
            else:
                flip2 -= 1
            mini = min(mini, flip1, flip2)
        return mini
