#  Example 1 -> Employee salary

from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def __init__(self,months,sal):
        self.total=months * sal
    def calculate_salary(self):
        print("Total Full Time Salary =",self.total)

class freeLance(Employee):
    def __init__(self,hours,sal):
        self.total=hours * sal
    def calculate_salary(self):
        print("Total Free lance Salary =",self.total)

class partTime(Employee):
    def __init__(self,module,sal):
        self.total=module * sal
    def calculate_salary(self):
        print("Total Part Time Salary =",self.total)

full=FullTime(4,65000)
full.calculate_salary()

free=freeLance(15,1000)
free.calculate_salary()

part=partTime(5,20000)
part.calculate_salary()

# Example 2 -> mobile recharge

from abc import ABC, abstractmethod
class MobileRecharge(ABC):
    @abstractmethod
    def calculate_amount(self):
        pass
    
class Prepaid(MobileRecharge):
    def __init__(self, recharge, gst):
        gst_amount=recharge * gst / 100
        self.total=recharge + gst_amount
    def calculate_amount(self):
        print("Prepaid Recharge Amount =", self.total)

class Postpaid(MobileRecharge):
    def __init__(self, bill, late_days):
        late_fee= late_days * 20
        self.total = bill + late_fee
    def calculate_amount(self):
        print("Postpaid Bill Amount =", self.total)

class DataPack(MobileRecharge):
    def __init__(self, price, discount):
        discount_amt= price * discount / 100
        self.total = price- discount_amt
    def calculate_amount(self):
        print("Data Pack Amount =", self.total)

prepaid = Prepaid(899, 18)
prepaid.calculate_amount()

postpaid = Postpaid(599, 2)
postpaid.calculate_amount()

data = DataPack(499, 10)
data.calculate_amount()

# Example 3 -> Cab Booking

from abc import ABC, abstractmethod
class Cab(ABC):
    @abstractmethod
    def calculate_total(self):
        pass

class Bike(Cab):
    def __init__(self, distance,waiting_min):
        self.total= 30 + (distance * 8) + (waiting_min * 2) 
    def calculate_total(self):
        print("Bike Total =", self.total)

class Auto(Cab):
    def __init__(self, distance,waiting_min):
        self.total = 50 +(distance * 12) + (waiting_min * 3)
    def calculate_total(self):
        print("Auto Total =", self.total)

class Car(Cab):
    def __init__(self, distance,waiting_min):
        self.total = 100 + (distance * 18) + (waiting_min * 5)
    def calculate_total(self):
        print("Car Total =", self.total)


bike = Bike(10,4)
bike.calculate_total()

auto = Auto(10,5)
auto.calculate_total()

car = Car(10, 5)
car.calculate_total()





