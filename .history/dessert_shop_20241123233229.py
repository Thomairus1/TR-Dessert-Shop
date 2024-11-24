from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
from receipt import make_receipt

class Order():
    def __init__(self):
        self.order = []
    def add(self, dessertitem):
        self.order.append(dessertitem)
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        cost = 0.0
        for item in self.order:
            cost += item.calculate_cost()
        return cost
    def order_tax(self):
        tax = 0.0
        for item in self.order:
            tax += item.calculate_cost() * (item.tax_percent/100)
        return tax

class DessertShop():
    def user_prompt_candy(self):
        print("Type in the type of candy, the weight in pounds, and the price per pound")
        while True:
        candy_type = input("Candy type: ")
        weight = int(input("Candy weight in pounds: "))
        price = int(input("Price per pounds: "))
    def user_prompt_cookie(self):
        pass
    def user_prompt_ice_cream(self):
        pass
    def user_prompt_sundae(self):
        pass
    
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
    data.append(["Order Subtotals", "$"+str(round(order1.order_cost(), 2)), "$" + str(round(order1.order_tax(), 2))])
    data.append(["Total", "", "$" + str(round(order1.order_cost() + order1.order_tax(), 2))])
    data.append(["Total items in the order", "", str(order1.__len__())])
    import receipt
    receipt.make_receipt(data, "receipt.pdf")
    print(data)

main(Order)