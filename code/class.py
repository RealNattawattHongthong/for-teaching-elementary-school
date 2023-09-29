class Car:
    def __init__(self, brand):
        self.brand = brand

    def display_info(self):
        print("Car brand:", self.brand)

car = Car("Toyota")
car.display_info()