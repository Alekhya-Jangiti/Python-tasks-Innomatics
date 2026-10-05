# class Parent:
#     def brave(self):
#         print("Iam brave")
#     def talent(self):
#         print("Iam talent")
# p=Parent()
# #setting instance variable
# # p.land=100
# # p.brave()
# # p.talent()
# # print("Land =",p.land)

# #setting inheritance
# class Child(Parent): #sub class
#     def artist(self):
#         print("Iam artist")

# c=Child()
# c.artist() #its own(child class) method
# c.brave() #super class-->inherited method prom parent
# c.talent()


#----------------------------------single inheritance------------------------------

# class Animal:
#     def eat(self):
#         print("Eating...")
#     def sleeps(self):
#         print("sleeping...")
# class Dog(Animal):
#     def barks(self):
#         print("Dog barks")
# d=Dog()
# d.eat()
# d.sleeps()
# d.barks()

# class Bank:
#     bank_name = "Innomatics bank"
# class HydBranch(Bank):
#     # def m1(self):
#     #     print("m1 from hydBranch")
#     pass
# print("bank = ",Bank.bank_name)
# print("Hyderabad Branch = ",HydBranch.bank_name)

# h=HydBranch()
# print("HydBranch = ",h.bank_name)


# example with passing constructor and using constructor and method using super() method

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
        
#     def displayProdDet(self):
#         print("product Name =",self.name)
#         print("product price =",self.price)
# p=Product("Product",95000)

# p.displayProdDet()
# class Laptop(Product):
#     #inherited parent constructor is deleted from child and the current constructor is stored
#     # def __init__(self,name,price,ram):
#     #     self.name=name
#     #     self.price=price
#     #     self.ram=ram
#     def __init__(self,name,price,ram):
#         super().__init__(name,price)
#         self.ram=ram
#     def displayLapDet(self):
#         super().displayProdDet()
#         print("ram =",self.ram)
# l=Laptop("laptop",93000,"12gb")
# l.displayLapDet()

#------------------------------------multi-level inheritance--------------------------

# class A:
#     def m1(self):
#         print("method from A")
# class B(A):
#     def m2(self):
#          print("method from B")
# class C(B):
#     def m3(self):
#         print("method from C")
# c=C()
# c.m1()
# c.m2()
# c.m3()

# class GrandParent:
#     def house(self):
#         print("Grand parents Home")
# class Parent(GrandParent):
#     def car(self):
#         print("parents car")
# class Child(Parent):
#     def money(self):
#         print("Childs money")

# p=Parent()
# p.house()
# p.car()
# # c=Child()
# # print("---------------Child--------------")
# # c.house()
# # c.car()
# # c.money()

# Example
# class A:
#     def m1():
#         print("Iam m1 from A- Grand parent")
# class B(A):
#     def m2():
#         print("Iam m2 from B-parent ")
# class C(B):
#     def m3():
#         print("Iam m1 from C- Child")
# c=C()
# c.m1() #grand parent
# c.m2() #parent
# c.m3() #child

#--------multi level inheritance with constructor-------

class BankAccount:
    def __init__(self,bank_acc,bank_hld_name):
        self.bank_acc=bank_acc
        self.bank_hld_name=bank_hld_name
    def displayBankAccDet(self):
        print("bank account number :", self.bank_acc)
        print("bank holder name :", self.bank_hld_name)
        
# b1 = BankAccount(1001,"Hero")
# b1.displayBankAccDet()

# class BankAccountBlc(BankAccount):
#     def __init__(self,bank_acc,bank_hld_name,bank_blc):
#         super().__init__(bank_acc,bank_hld_name)
#         self.bank_blc = bank_blc
        
#     def displayBankAccBlc(self):
#         super().displayBankAccDet()
#         print("Account Balance", self.bank_blc)
# # b2 = BankAccountBlc(1002,"Hero2",95000)
# # b2.displayBankAccBlc()

# class BankAccType(BankAccountBlc):
#     def __init__(self,bank_acc,bank_hld_name,bank_blc,bank_type):
#         super().__init__(bank_acc,bank_hld_name,bank_blc)
#         self.bank_type=bank_type
        
#     def displayBankAndType(self):
#         super().displayBankAccBlc()
#         print("Account Type :", self.bank_type)
# bt = BankAccType(1003,"Hero3",900000,"Current Accunt")
# bt.displayBankAndType()

# ----------------------------------------------Hierarchical inheritance-----------------------------------

# class Parent:
#     def m1(self):
#         print("m1 from parent")
# class Child1(Parent):
#     def m2(self):
#         print("m2 from child 1")
# class Child2(Parent):
#     def m3(self):
#         print("m3 from child 2")
# c1 = Child1()
# c1.m2() #its own method -->right
# c1.m1() #its parent method -->right
# c1.m3() #its sibling method -->wrong

# c2= Child2()
# c2.m3() #its own method -->right
# c2.m1() #its parent method -->right
# c2.m2() #its sibling method -->wrong

# p= Parent()
# p.m1()
# p.m2()
# p.m3()

#Example

# class Employee:
#     def det(self):
#         print("iam employee")
# class Manager(Employee):
#     def myWork(self):
#         print("I work as Manager")
# class Developer(Employee):
#     def myDesig(self):
#         print("I work as Developer")

# d=Developer()
# d.myDesig()
# d.det()

# m=Manager()
# m.myWork()
# m.det()

#--------------------------------------------------Multiple inheritance---------------------------------

# class Father:
#     def brave(self):
#         print("iam brave")
# class Mother:
#     def beautiful(self):
#         print("Iam beautiful")
# class Child(Father,Mother):
#     def intelligent(self):
#         print("iam intelligent")
        
# c = Child()
# c.intelligent()
# c.brave()
# c.beautiful()

# class Camera:
#     def cam(self):
#         print("Iam Camera")
# class MusicPlayer:
#     def music(self):
#         print("iam music")
# class SmartPhone(Camera,MusicPlayer):
#     def phone(self):
#         print("iam smart phone")
# p = SmartPhone()
# p.phone()
# p.cam()
# p.music()

# ----------------------------------------hybrid inheritance-----------------------------------

# Example multilevel + multiple
# class A:
#     def m1(self):
#         print("m1 from A")
# class B:
#     def m2(self):
#         print("m2 from B")
# class C(A,B):
#     def m3(self):
#         print("m3 from C")
# class D(C):
#     def m4(self):
#         print("m4 from D")
# d = D()
# d.m4()
# d.m3()
# d.m2()
# d.m1()

#Example hierarchical + multi level

# class A:
#     def m1(self):
#         print("m1 from A")
# class B(A):
#     def m2(self):
#         print("m2 from B")
# class C(A):
#     def m3(self):
#         print("m3 from C")
# class D(C):
#     def m4(self):
#         print("m4 from D")
# d = D()
# d.m4()
# d.m3()
# d.m2()
# d.m1()

#--------------------------------MRO (Method Resolution Order)------------------------------------------------
# for single inheritance
# class A:
#     def m1(self):
#         print("iam m1 from A")
# class B(A):
#     def m2(self):
#         print("iam m2 from B")
# b = B()
# # b.m2()
# b.m1()

# # formulti-level inheritance
# class GrandPArent:
#     def m1(self):
#         print("iam m1 from Grand Parent")
# class Parent(GrandPArent):
#     def m2(self):
#         print("iam m2 from Parent")
# class Child(Parent):
#     def m3(self):
#         print("iam m3 from Child")
# c = Child()
# c.m1()
# print(Child.mro())  #Order = Child --> Parent --> Grandprent --> Object

# class A:
#     pass
# print(A.mro()) #MRO path--> a ->Object

# class A:
#     def m1(self):
#         print("M1 from A")
# class B:
#     def m1(self):
#         print("M1 from B")
# class C(A,B):
#     pass
# c=C()
# c.m1()
# print(C.mro()) #C-->A-->B-->Object

# Diamond problem
class X:
    def m0(self):
        print("iam m0 from X")
class A:
    def m1(self):
        print("M1 from A")
class B:
    def m1(self):
        print("M1 from B")
class C(A,B):
    pass
c=C()
c.m1()
print(C.mro())