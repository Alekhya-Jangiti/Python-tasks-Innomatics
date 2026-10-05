#-------------------------------Single inheritance---------------------------------------

# single inheritance without constructor
class Restaurant:
    def prepare_food(self):
        print("Restaurant prepares food")

    def serve_food(self):
        print("Restaurant serves food")

class Chef(Restaurant):
    def cooking(self):
        print("Chef cooks food")

    def menu(self):
        print("Chef prepares the menu")

c = Chef()
c.prepare_food()
c.serve_food()
c.cooking()
c.menu()

# single inheritance with constructor
class Vehicle:
    def start(self):
        print("Vehicle starts")

    def stop(self):
        print("Vehicle stops")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

    def horn(self):
        print("Car horn is working")

c = Car()
c.start()
c.stop()
c.drive()
c.horn()

#single inheritance with constructor + super()
class BankAccount:
    def __init__(self, name, account_no):
        self.name = name
        self.account_no = account_no

    def displayaccount(self):
        print("Account holder:", self.name)
        print("Account number:", self.account_no)

class SavingsAccount(BankAccount):
    def __init__(self, name, account_no, balance, interest):
        super().__init__(name, account_no)
        self.balance = balance
        self.interest = interest

    def displaysavings(self):
        super().displayaccount()
        print("Balance:", self.balance)
        print("Interest:", self.interest)

s = SavingsAccount("Ravi", 12345, 50000, "6.5%")
s.displaysavings()

#single inheritance with constructor + super()
class Cricketer:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def displayplayer(self):
        print("Player Name:", self.name)
        print("Country:", self.country)

class Bowler(Cricketer):
    def __init__(self, name, country, bowling_style):
        super().__init__(name, country)
        self.bowling_style = bowling_style

    def displaybowler(self):
        super().displayplayer()
        print("Bowling Style:", self.bowling_style)

b = Bowler("Jasprit Bumrah", "India", "Fast Bowling")
b.displaybowler()

#-----------------------------Multi-level inheritance------------------------------
# multilevel inheritance without constructor
class Shopping:
    def select_product(self):
        print("Customer selects a product")

class OnlineShopping(Shopping):
    def add_cart(self):
        print("Product added to cart")

class MobileShopping(OnlineShopping):
    def make_payment(self):
        print("Payment completed using mobile")

m = MobileShopping()
m.select_product()
m.add_cart()
m.make_payment()

# multilevel inheritance with constructor
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def displaycompany(self):
        print("Company:", self.company_name)

class Employee(Company):
    def __init__(self, company_name, employee_name):
        super().__init__(company_name)
        self.employee_name = employee_name

    def displayemployee(self):
        super().displaycompany()
        print("Employee:", self.employee_name)

class Developer(Employee):
    def __init__(self, company_name, employee_name, language):
        super().__init__(company_name, employee_name)
        self.language = language

    def displaydeveloper(self):
        super().displayemployee()
        print("Language:", self.language)

d = Developer("Infosys", "Alekhya", "Python")
d.displaydeveloper()

# multilevel inheritance with constructor + super()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def displayvehicle(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def displaycar(self):
        super().displayvehicle()
        print("Model:", self.model)

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def displayelectriccar(self):
        super().displaycar()
        print("Battery:", self.battery)
e = ElectricCar("Tesla", "Model 3", "75 kWh")
e.displayelectriccar()

# multilevel inheritance with constructor + super()

class Cricket:
    def __init__(self, player_name):
        self.player_name = player_name

    def displayplayer(self):
        print("Player Name:", self.player_name)

class Batsman(Cricket):
    def __init__(self, player_name, runs):
        super().__init__(player_name)
        self.runs = runs

    def displaybatsman(self):
        super().displayplayer()
        print("Runs:", self.runs)

class Captain(Batsman):
    def __init__(self, player_name, runs, team):
        super().__init__(player_name, runs)
        self.team = team

    def displaycaptain(self):
        super().displaybatsman()
        print("Team:", self.team)

c = Captain("Virat", 25000, "India")
c.displaycaptain()
