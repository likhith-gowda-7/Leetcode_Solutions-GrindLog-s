class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        h1=defaultdict(set)
        for i in range(len(languages)):
            for lang in languages[i]:
                h1[i+1].add(lang)
        users=set()
        for u,v in friendships:
            uni=h1[u].isdisjoint(h1[v])
            if(uni):
                users.add(u)
                users.add(v)
        if(not users):
            return 0
        min_teaching=float('inf')
        for lang in range(1,n+1):
            already_knows=sum([1 for user in users if(lang in h1[user])])
            need_to_teach=len(users)-already_knows
            min_teaching=min(min_teaching,need_to_teach)
        return min_teaching

        