# ------------------------------------method overriding----------------------------------
# with single inheritance
# class A:
#     def m1(self):
#         print("method 1 from A")
# class B(A):
#     #overriding
#     def m1(self):
#         print("method 2 from B")
# a=A()
# a.m1()
# b=B()
# b.m1()

# multi level inheritance
# class A:
#     def m1(self):
#         print("method 1 from A")
# class B(A):
#     # method overriding
#     def m1(self):
#         print("method 2 from B")
# class C(B):
#     # method overriding
#     def m1(self):
#         print("method 3 from C")
# a=A()
# a.m1()
# b=B()
# b.m1()
# c=C()
# c.m1()

# class Mobile:
#     def camera(self):
#         print("Camera quality : 5px")
# class SmartPhone(Mobile):
#     #overriding
#     def camera(self):
#         print("Camera quality : 64px")
# class LatestSmartPhone(SmartPhone):
#     # overriding
#     def camera(self):
#         print("Camera quality : 200px")
        
# latest = LatestSmartPhone()
# latest.camera()
# smart = SmartPhone()
# smart.camera()

#example
# class Mobile:
#     def call(self):
#         print("Calling")
#     def camera(self):
#         print("camera quality : 5px")
        
# class SmartMobile(Mobile):
#     def internet(self):
#         print("Browsing Enabled")
#     def camera(self):
#         print("camera quality : 64px")
        
# class LatestMobile(SmartMobile):
#     def fingerprint(self):
#         print("Unlock mobile with fingerprint")
#     def camera(self):
#         print("camera quality : 200px")
# latest=LatestMobile()
# latest.call()
# latest.internet()
# latest.fingerprint()     

#example
# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meow..")
# c=Cat()
# c.sound()

# ------------------------------------method overloading-------------------------------

# class Test:
#     def add(self,a,b):
#         print("Two parameters")
#         # here overload will not  work override will work as it only takes new method
#     def add(self,a,b,c):
#         print("Three parameters")
# t=Test()
# t.add(10,20,30)

# polymorphism with operators
# a=10
# b=20
# print(a+b) # addition
# print("hero" + "Zero") # concatenation
# print([1,2,3,4] +[5,6,7]) # merging list

