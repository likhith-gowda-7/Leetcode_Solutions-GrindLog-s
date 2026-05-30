class Solution(object):
    def countOfSubstrings(self, word, k):
        def atleastk(k):
            count=defaultdict(int)
            non_vowels=0
            l=0
            res=0
            for r in range(len(word)):
                if(word[r] in "aeiou"):
                    count[word[r]]+=1
                else:
                    non_vowels+=1
                while len(count)==5 and non_vowels>=k:
                    res+=(len(word)-r)
                    if(word[l] in "aeiou"):
                        count[word[l]]-=1
                    else:
                        non_vowels-=1
                    if(count[word[l]]==0):
                       count.pop(word[l])
                    l+=1
            return res
        return atleastk(k)-atleastk(k+1)
            


        