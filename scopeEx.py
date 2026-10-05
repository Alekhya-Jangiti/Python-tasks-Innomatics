# ----------------global variable and its global scope------------------

# fname="hero" # global variable
# print("Before :Outside function :",fname)

# def gbScope():
#     print("Inside Function :",fname)
# gbScope()
# print("After : Outside function",fname)


# ----------------local variable and its local scope---------------------

# def localScope():
#     fname="hero" # local scope
#     print("Inside Function :",fname)
# localScope()
# print("After : Outside function",fname) # it will not work because it is outside the function

# def displayName(name):
#     print("Name inside :",name)
# displayName("hero")
# print("Outside function :",fname) # it will not print 
    
    
# fname="Global" #global variable
# def myFun():
#     fname="Local" #local variable
#     print("Inside Function =",fname)
# myFun()
# print("Outside Function =",fname)

# fname="Hero" #global variable
# def myFun():
#     global fname
#     fname="Zero" #local variable
# myFun()
# print("Outside Function =",fname)

#--------------------------nested function------------------
# def outerFunc():
#     print("Outer function")
#     def innerFunc():
#         print("Inner function")
#     # innerFunc() #✅
# outerFunc()
# #innerFunc() #❌

#----------------------------Enclosing Scope------------------------------

# def outerFunc():
#     #Enclosing scope
#     myName="hero" #Enclosing variable
#     def innerFun():
#         print("Inner func")
#         print("Nested Func=",myName)
#     innerFun()
#     print("Enclosing Func=",myName)
# outerFunc()

# def outerFunc():
#     #Enclosing scope
#     myName="hero" #Enclosing variable
#     def innerFun():
#         myName="Zero"
#         print("Nested Func=",myName)
#     innerFun()
#     print("Enclosing Func=",myName)
# outerFunc()

# def outerFunc():
#     #Enclosing scope
#     myName="hero" #Enclosing variable
#     def innerFun():
#         nonlocal myName
#         myName="Zero"
#         print("My name is",myName) #zero
#     innerFun()
#     print("Enclosing Func=",myName) #zero
# outerFunc()


# an example using global,nonlocal and directly modify
# name="Allu" #global variable
# def outerFunc():
#     name="Alekhya"
#     def innerFunc():
#         global name
#         #nonlocal name
#         name="Anku"
#         print("name in inner func=",name)
#     innerFunc()
#     print("enclosing variable =",name)
# outerFunc()
# print(name)

#---------------------------------built-in Scope-----------------------------------

# import builtins
# print(dir(builtins))

# a="Alekhya"
# print(len(a))

# ------------------------------------scope chain--------------------------------------------
#myName="global"
# def outer():
#     #myName="enclosing"
#     def inner():
#         #myName="Hero"
#         print("Inner func",myName)
#     inner()
# outer()

#example using len function
# def outer():
#     def inner():
#         print(len("Hero")) # it is accesed from built in scope- LEGB
#     inner()
# outer()

#---------------------------------------lexical scope------------------------------

# gvar="Global Var"
# def outer():
#     evar="Enclosing Var"
#     def inner():
#         lvar="Local Var"
#         print("-----------Data from nested function-----------")
#         print("Global Variable :",gvar)✅
#         print("Enclosing var :",evar)✅
#         print("Local var :",lvar)✅
#     inner()
#     print("-----------Data from enclosing function-----------")
#     print("Global Variable :",gvar)✅
#     print("Enclosing var :",evar)✅
#     print("Local var :",lvar)❌
# outer()
# print("-----------Data outside function-----------")
# print("Global Variable :",gvar)✅
# print("Enclosing var :",evar)❌
# print("Local var :",lvar)❌



