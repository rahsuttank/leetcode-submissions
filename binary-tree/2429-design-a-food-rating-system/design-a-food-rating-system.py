class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisinesHeaps = defaultdict(list)
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        for i in range(len(foods)):
            heapq.heappush(self.cuisinesHeaps[cuisines[i]],[-ratings[i], foods[i]])
            self.food_to_cuisine[foods[i]] = cuisines[i]
            self.food_to_rating[foods[i]] = ratings[i]
        
        # for key in self.cuisinesHeaps.keys():
        #     heapq.heapify(self.cuisinesHeaps[key])
        

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisinesHeaps[cuisine], [-newRating, food])

        

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisinesHeaps[cuisine]
        

        while -heap[0][0] != self.food_to_rating[heap[0][1]]:
            heapq.heappop(heap)
        return heap[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)