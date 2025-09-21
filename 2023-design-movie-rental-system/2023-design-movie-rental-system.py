from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.available = {}
        self.rented = SortedList()
        self.shop_movie_price = {(shop, movie): price for shop, movie, price in entries}

        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((price, shop))

    def search(self, movie: int) -> list[int]:
        return [shop for _, shop in self.available.get(movie, [])[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]