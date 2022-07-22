""" Exercise #7. Python for Engineers."""


#########################################
# Question 1 - do not delete this comment
#########################################

class Beverage:
    
    def __init__(self, name, price, is_diet):
        if price<=0:
            raise ValueError("Do you give beverages for FREE? You Madman!")
        self.name=name
        self.price=float(price)
        self.is_diet=is_diet
        
    def get_final_price(self, size='Large'):
        if size=='Large':
            return self.price
        if size=='Normal':
            return self.price*3/4
        if size=='XL':
            return self.price*5/4
        else:
            raise ValueError("The size you entered is INVALID")

#########################################
# Question 2 - do not delete this comment
#########################################

class Pizza:
    
    def __init__(self, name, price, calories, toppings):
        if price<=0:
            raise ValueError('Pizza is not free you know...')
        if calories<=0:
            raise ValueError('Pizza will not get you thinner...')
        self.name=name
        self.price=float(price)
        self.calories=calories
        self.toppings=toppings
        
    def get_final_price(self, size='Family'):
        if size=='Family':
            return self.price
        if size=='XL':
            return self.price*23/20
        if size=='Personal':
            return self.price*3/5
        else:
            raise ValueError('Size is INVALID')
        
    def add_topping(self, topping, calories, price):
        if topping in self.toppings:
            raise ValueError('You can not add more ' +topping)
        self.price=price+self.price
        self.calories=calories+self.calories
        self.toppings.append(topping)
        
    def remove_topping(self, topping, calories, price):
        if self.price-price<=0:
            raise ValueError('Less toppings does not mean the pizza is free')
        if self.calories-calories<=0:
            raise ValueError('Less toppings will still get you fat...')
        if topping not in self.toppings:
            raise ValueError('You can not remove a topping which is not there')
        self.price=self.price-price
        self.calories=self.calories-calories
        self.toppings.remove(topping)


#########################################
# Question 3 - do not delete this comment
#########################################

class Meal:

    def __init__(self, beverage, pizza):
        self.beverage = beverage
        self.pizza = pizza

    def get_final_price(self, beverage_size, pizza_size):
        return self.beverage.get_final_price(beverage_size) + self.pizza.get_final_price(pizza_size)

    def is_healthy(self):
        if self.beverage.is_diet == False:
            return False
        if self.pizza.calories >= 1000:
            return False
        else:
            return True
