class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        #cusines -> heap of (food's rating and food)
        self.details=defaultdict(list)
        # food -> cuisine
        self.food_map=defaultdict(list)
        for i in range(len(foods)):
            val=[-ratings[i],foods[i]]
            self.food_map[foods[i]]=[-ratings[i],cuisines[i]]
            self.details[cuisines[i]].append(val)
        for val in self.details.values():
            heapify(val)
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine=self.food_map[food][1]
        self.food_map[food][0]=-newRating
        heappush(self.details[cuisine],[-newRating,food])
    def highestRated(self, cuisine: str) -> str:
        heap=self.details[cuisine]
        while heap:
            r,f=heap[0]
            if(r==self.food_map[f][0]):
                return f
            heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)