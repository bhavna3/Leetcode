
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies={}  
        self.shops={}  
        self.rented=set()  

        for shop, movie, price in entries:
            self.movies[(shop, movie)] = price
            if movie not in self.shops:
                self.shops[movie] = []
            self.shops[movie].append((price, shop))

        for movie in self.shops:
            self.shops[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for price, shop in self.shops.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.movies[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()