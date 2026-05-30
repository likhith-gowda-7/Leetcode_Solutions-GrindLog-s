class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n=len(deck)
        dq=deque(range(n))
        q=[0]*n
        for val in deck:
            i=dq.popleft()
            q[i]=val
            if(dq):
                dq.append(dq.popleft())
        return q

        


