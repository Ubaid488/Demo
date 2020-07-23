class Bike:
    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = False

    def update_sale_price(self, sale_price):
        if self.sold:
            raise Exception("Action not allowed. Bike has already been sold")
        self.sale_price = sale_price

    def sell(self, sold_for=None):
        if sold_for:
            self.update_sale_price(sold_for)
        self.sold = True
        return self.sale_price - self.cost


if __name__ == "__main__":
    b = Bike("Univega Alpina, orange", cost=100, sale_price=500, condition=0.5)
    b.update_sale_price(350)
    print(b.sell())
