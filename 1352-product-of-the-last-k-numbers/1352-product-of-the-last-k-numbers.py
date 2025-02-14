class ProductOfNumbers:

    def __init__(self):
        self.products= []
        self.current_product = 1
        

    def add(self, num: int) -> None:
        if num: 
            self.current_product *= num
            self.products.append(self.current_product)
        else: 
            self.products= []
            self.current_product = 1
        

    def getProduct(self, k: int) -> int:
        if len(self.products) < k: 
            return 0
        elif len(self.products) == k: 
            # return self.products[-1]
            return self.current_product
        else: 
            return int(self.products[-1]/self.products[-1-k])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)