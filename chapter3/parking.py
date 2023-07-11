class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.items:
            return "items is empty."
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


class ParkingLot():
    def __init__(self, max, cars):
        self.max_size = int(max)
        self.cars = Stack()
        self.car_park(cars)
    
    def car_park(self, cars):
        car_list = cars.split(',')
        for car in car_list:
            car = int(car)
            if car == 0:
                continue
            self.cars.push(car)
    
    def add(self, mode, car):
        car = int(car)
        if mode == "depart":
            if self.cars.size() == 0:
                return f"car {car} cannot depart : Soi Empty"
            if car not in self.cars.items:
                return f"car {car} cannot depart : Dont Have Car {car}"
            else:
                self.cars.items.remove(car)
                return f"car {car} depart ! : Car {car} was remove"
        if car in self.cars.items:
            return f"car {car} already in soi"
        if mode == "arrive":
            if self.cars.size() == self.max_size:
                return f"car {car} cannot arrive : Soi Full"
            else:
                self.cars.push(car)
                return f"car {car} arrive! : Add Car {car}"

max, cars, mode, car = input('******** Parking Lot ********\nEnter max of car,car in soi,operation : ').split(' ')
parking_lot = ParkingLot(max, cars)
print(parking_lot.add(mode, car))
print(parking_lot.cars.items)