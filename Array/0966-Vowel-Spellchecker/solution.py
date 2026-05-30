class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels="aeiou"
        n=len(queries)
        exact_word=set()
        case_map=defaultdict(str)
        def vowels_check(word):
            ans=""
            for i in range(len(word)):
                if(word[i] in vowels):
                    ans+="*"
                else:
                    ans+=word[i]
            return ans
        for word in wordlist:
            exact_word.add(word)
            if(word.lower() not in case_map):
                case_map[word.lower()]=word
            w=vowels_check(word.lower())
            if(w not in case_map):
                case_map[w]=word

        res=[""]*n
        for idx,word in enumerate(queries):
            w=vowels_check(word.lower())
            if(word in exact_word):
                res[idx]=word
            elif(word.lower() in case_map):
                res[idx]=case_map[word.lower()]
            elif(w in case_map):
                res[idx]=case_map[w]
        return res
                