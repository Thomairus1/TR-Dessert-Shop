from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_candy_init():
    candy = Candy("Chocolate", 3.5, 1.5)
    name = candy.get_name()
    assert name == "Chocolate"
    weight = candy.get_candy_weight()
    assert weight == 3.5
    price = candy.get_price_per_pound()
    assert price == 1.5

def test_cookie_init():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    name = cookie.get_name()
    assert name == "Chocolate chip"
    quant = cookie.get_cookie_quantity()
    assert quant == 12
    price = cookie.get_price_per_dozen()
    assert price == 15.60

def test_iceCream_init():
    ice_cream = IceCream("Vanilla", 2, 2.99)
    name = ice_cream.get_name()
    assert name == "Vanilla"
    count = ice_cream.get_scoop_count()
    assert count == 2
    price = ice_cream.get_price_per_scoop()
    assert price == 2.99

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
    
def test_calculate_cost():
    candy = Candy("Chocolate", 3.5, 1.5)
    cost = candy.get_candy_weight() * candy.get_price_per_pound()
    assert candy.calculate_cost() == cost
    cookie = Cookie("Chocolate chip", 12, 15.60)
    cost = cookie.get_cookie_quantity() * (cookie.get_price_per_dozen()/12)
    assert cookie.calculate_cost() == cost
    ice_cream = IceCream("Vanilla", 2, 2.99)
    cost = ice_cream.get_scoop_count() * ice_cream.get_price_per_scoop()
    assert ice_cream.calculate_cost() == cost
    sundae = Sundae("Rocky Road", 2, 3.11, "Cherry", 1.00)
    cost = sundae.get_scoop_count() * sundae.get_price_per_scoop() + sundae.get_topping_price()
    assert sundae.calculate_cost() == cost

def test_calculate_tax():
    candy = Candy("Chocolate", 3.5, 1.5)
    tax = candy.calculate_cost() * (7.25/100)
    assert candy.calculate_tax() == tax

    cookie = Cookie("Chocolate chip", 12, 15.60)
    tax = cookie.calculate_cost() * (7.25/100)
    assert cookie.calculate_tax() == tax

    ice_cream = IceCream("Vanilla", 2, 2.99)
    tax = ice_cream.calculate_cost() * (7.25/100)
    assert ice_cream.calculate_tax() == tax


    sundae = Sundae("Rocky Road", 2, 3.11, "Cherry", 1.00)
    tax = sundae.calculate_cost() * (7.25/100)
    assert sundae.calculate_tax() == tax