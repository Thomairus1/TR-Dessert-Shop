from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
from receipt import make_receipt, main1

class Order():
    def __init__(self, cost=0.0, tax=0.0):
        self.order = []
        self.cost = cost
        self.tax = tax
    def add(self, dessertitem):
        self.order.append(dessertitem)
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        for item in self.order:
            cost += self.item.calculate_cost()
        return cost
    def order_tax(self):
        for item in self.order:
            tax += self.item.calculate_cost() * (self.tax_percent/100)
    
def main(Order):
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    print("Candy Corn")
    order1.add(Candy("Gummy Bears", .25, .35))
    print("Gummy Bears")
    order1.add(Cookie("Chocolate Chip", 6, 3.99))
    print("Chocolate Chip")
    order1.add(IceCream("Pistachio", 2, .79))
    print("Pistachio")
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    print("Vanilla")
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))
    print("Oatmeal Raisin")
    print(f"Total number of items in order: {order1.__len__()}")
    data = []
    for item in order1.order:
        if isinstance(item, Candy):
            data.append([item.name, item.candy_weight, item.price_per_pound])
        elif isinstance(item, Cookie):
            data.append([item.name, item.cookie_quantity, item.price_per_dozen])
        elif isinstance(item, IceCream):
            data.append([item.name, item.scoop_count, item.price_per_scoop])
        elif isinstance(item, Sundae):
            data.append([item.name, item.scoop_count, item.price_per_scoop, item.topping_name, item.topping_price])
    data.append(["Order Subtotals", order1.order_cost, order1.order_tax])
    data.append(["Total", "", (order1.order_cost.cost) + (order1.order_tax.tax)])
    data.append(["Total items in the order", "", order1.__len__()])
    data.make_receipt(data, "receipt.pdf")

    main1()

main(Order)