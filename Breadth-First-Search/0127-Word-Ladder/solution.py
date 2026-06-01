class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #BFS-Soultion(invert thinking)
        word_map=set(wordList)
        if(endWord not in word_map):
            return 0
        if(beginWord not in word_map):
            word_map.add(beginWord)
        q=deque([endWord])
        seen=set(endWord)
        shortest_sequence=1
        alpha="abcdefghijklmnopqrstuvwxyz"
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if(word==beginWord):
                    return shortest_sequence
                #go for each word and make every possible one letter change for the word and check if that word exist in the wordList, if yes then add it to the q
                for i in range(len(word)):
                    #trying every one letter combination
                    for ch in alpha:
                        #i.e left side + (any alphabet) + right side(remaining)
                        change=word[:i]+ch+word[i+1:]
                        if(change in word_map and change not in seen):
                            q.append(change)
                            seen.add(change)
            shortest_sequence+=1
        return 0

