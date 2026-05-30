class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # backtracking i_s, i_t
        len_t = len(t)
        len_s = len(s)
        memo = {}

        def recursive(ind_s, ind_t):

            if (ind_s, ind_t) in memo:
                return memo[(ind_s, ind_t)]

            if ind_t == len_t:
                return 1

            if ind_s >= len_s or (len_s - ind_s) < (len_t - ind_t):
                return 0
            
            distinct_count = 0 
            if s[ind_s] == t[ind_t]:
                distinct_count += recursive(ind_s+1, ind_t+1)
            
            distinct_count += recursive(ind_s + 1, ind_t)
            memo[(ind_s, ind_t)] = distinct_count

            return distinct_count


        return recursive(0,0)
        