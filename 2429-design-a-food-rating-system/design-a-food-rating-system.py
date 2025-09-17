class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods=defaultdict(tuple)
        self.cuisines=defaultdict(list)

        for f,c,r in zip(foods, cuisines, ratings):
            self.foods[f]=(c,r)
            heapq.heappush(self.cuisines[c], (-r, f))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating=self.foods[food]
        self.foods[food]=(cuisine, newRating)
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))

        

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines[cuisine]
        while heap:
            rating, food = heap[0]
            if self.foods[food][1]==-rating:
                return food
            heapq.heappop(heap)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)