# ----------------------------------------public modifier-----------------------------

# class Test:
#     fname="Hero" #public class variable
#     @staticmethod
#     def display():
#         print("within same class -->Name :",Test.fname) #within same class
# t=Test()
# t.display()
# print("Within outside class -->Name :",Test.fname) #outside the class

# # another class
# class Test2:
#     fname="Hero" #public class variable
#     @staticmethod
#     def m2():
#         print("within anothet class --> Name :",Test.fname)
# t2=Test2()
# t2.m2()

# class Test:
#     fname="Hero" #public class variable
# class Test2(Test):
#     @staticmethod
#     def display2():
#         print("Within subclass -->Name :",Test2.fname)
# t2=Test2()
# t2.display2()

# class Test:
#     def m1(self):
#         self.name="Hero" #public instance variable
#         # within same class
#         print("Within the same class -->Name :",self.name)
# t=Test()
# t.m1()
# #oustide the class
# print("Within oustide class-->Name :",t.name) 

# class Test:
#     def __init__(self):
#         self.name="Hero"
# class Test2:
#     def m2(self):
#         t=Test()
#         print("Within another class--> Name :",t.name)
# t2=Test2()
# t2.m2()

# ---------------------public static method
# class Test:
#     @staticmethod
#     def m1():
#         print("Within ststic method")

# t2=Test()
# t2.m1()

# -----------------------------------------private class member-------------------------------------

# class Test:
#     __fname="hero" #private class variable
#     @staticmethod
#     def display():
#         print("Class member within same class",Test.__fname)
# t=Test()
# t.display()
# print("class member outside the class",Test.__fname)

#sub class 

# class Test:
#     __fname="hero" #private class variable
# class Test2(Test):
#     @staticmethod
#     def display2(self):
#         print("Within another class",Test.__fname)
# Test2.display2()
    
#private method

# class Test:
#     @staticmethod
#     def __display():
#         print("iam display")
#     @staticmethod
#     def call_m():
#         print("within same class")
#         Test.__display()
# Test.call_m()

# oustide class

# class Test:
#     @staticmethod
#     def __display():
#         print("iam display")
# print("outside class")
# Test.__display()

# ---------------------------------Name mangling-----------------------

# class Test:
#     __fname="hero"
    
# class Test2:
#     def m1(self):
#         print("name outside using Name mangling ",Test._Test.__fname)
# t2=Test2()
# t2.m1()

# -----------------------------protected class member-------------------------------

class Test:
    _fname="Hero"
    @staticmethod
    def display():
        print("within same class",Test._fname)
Test.display()
print("Outside the class",Test._fname)
# another class
class Test2:
    _fname="Hero"
    @staticmethod
    def display2():
        print("within another class",Test._fname)
Test2.display2()
