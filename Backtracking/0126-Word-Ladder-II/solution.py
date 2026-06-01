class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_map=set(wordList)
        if(endWord not in word_map):
            return []
        #first we'll use BFS to find the shortest distance to reach the end word
        seen=set([beginWord])
        q=deque([beginWord])
        alpha="abcdefghijklmnopqrstuvwxyz"
        dist_map=defaultdict(int)
        dist_map[beginWord]=0
        dist=1
        found=False
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if(word==endWord):
                    found=True
                    break
                for i in range(len(word)):
                    for ch in alpha:
                        changed_word=word[:i]+ch+word[i+1:]
                        if(changed_word in word_map and changed_word not in seen):
                            q.append(changed_word)
                            seen.add(changed_word)
                            dist_map[changed_word]=dist
            if(found):
                break
            dist+=1
        if(not found):
            return []
        #backtrack and found all the combination that could the endWord with same distance
        res=[]
        sol=[endWord]
        seen.clear()
        seen.add(endWord)
        def backtrack(word,curr_dist):
            if(word==beginWord):
                res.append(sol[::-1].copy())
                return
            if(curr_dist!=dist_map[word]):
                return
            for i in range(len(word)):
                for ch in alpha:
                    changed_word=word[:i]+ch+word[i+1:]
                    if(changed_word in dist_map and changed_word not in seen):
                        seen.add(changed_word)
                        sol.append(changed_word)
                        backtrack(changed_word,curr_dist-1)
                        #undo the changes
                        seen.remove(changed_word)
                        sol.pop()
        backtrack(endWord,dist_map[endWord])
        return res