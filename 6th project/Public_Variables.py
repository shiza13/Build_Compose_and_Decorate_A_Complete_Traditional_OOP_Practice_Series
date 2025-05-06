class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "car has started.")

my_car = Car("Toyota")
print("Brand of the car:", my_car.brand)
my_car.start()


