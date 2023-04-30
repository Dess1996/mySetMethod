"""
Сценарий заказа блюд быстрого питания с четырьмя классами

"""


class Lunch:
    def __init__(self):
        self.cus = Customer()
        self.emp = Employee()
    
    def order(self, foodName):
        self.cus.placeOrder(foodName, self.emp)
    
    def result(self):
        self.cus.printFood()


class Customer:
    def __init__(self):
        self.food = None
    
    def placeOrder(self, foodName, employee):
        self.food = employee.takeOrder(foodName)
    
    def printFood(self):
        print('Place order %s' % self.food.name)


class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)


class Food:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    x = Lunch()
    x.order('Babab')
    x.result()
    x.order('Pizza')
    x.result()