class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        #sort both array
        players.sort()
        trainers.sort()
        c=0
        l=len(players)
        for cap in trainers:
            if(cap>=players[c]):
                c+=1
                if(c==l):
                    break
        return c
