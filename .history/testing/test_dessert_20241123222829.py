from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_candy_init():
    candy = Candy("Chocolate", 3.5, 1.5)
    name = candy.get_name()
    assert name == "Chocolate"
    weight = candy.get_candy_weight()
    assert weight == 3.5
    price = candy.get_price_per_pound()
    assert price == 1.5
    cost = candy.candy_weight * candy.price_per_pound
    assert candy.calculate_cost() == cost

def test_cookie_init():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    name = cookie.get_name()
    assert name == "Chocolate chip"
    quant = cookie.get_cookie_quantity()
    assert quant == 12
    price = cookie.get_price_per_dozen()
    assert price == 15.60
    cost = cookie.cookie_quantity * (cookie.price_per_dozen/12)
    assert cookie.calculate_cost() == cost

def test_iceCream_init():
    ice_cream = IceCream("Vanilla", 2, 2.99)
    name = ice_cream.get_name()
    assert name == "Vanilla"
    count = ice_cream.get_scoop_count()
    assert count == 2
    price = ice_cream.get_price_per_scoop()
    assert price == 2.99
    cost = ice_cream.scoop_count * ice_cream.price_per_pound
    assert ice_cream.calculate_cost() == cost

def test_sundae_init():
    sundae = Sundae("Rocky Road", 2, 3.11, "Cherry", 1.00)
    name = sundae.get_name()
    assert name == "Rocky Road"
    count = sundae.get_scoop_count()
    assert count == 2
    price = sundae.get_price_per_scoop()
    assert price == 3.11
    topping = sundae.get_topping_name()
    assert topping == "Cherry"
    topping_price = sundae.get_topping_price()
    assert topping_price == 1.00
    
def test_tax_percent():
    candy1 = Candy("Chocolate", 3.5, 1.5)
    assert candy1.tax_percent == 7.25