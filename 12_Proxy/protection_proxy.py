class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car being driven by {self.driver.name}")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print(f"Driver {self.driver.name} too young")


if __name__ == "__main__":
    car = CarProxy(Driver("John", 12))
    car.drive()
