# Example 1

# class CricketPlayer:
#     def __init__(self, jerseyNo, name, team, runs):
#         self.__jerseyNo = jerseyNo
#         self.__name = name
#         self.__team = team
#         self.__runs = runs

#     def getJerseyNo(self):
#         return self.__jerseyNo

#     def getName(self):
#         return self.__name

#     def getTeam(self):
#         return self.__team

#     def getRuns(self):
#         return self.__runs

#     def setJerseyNo(self, myJerseyNo):
#         self.__jerseyNo = myJerseyNo

#     def setName(self, myName):
#         self.__name = myName

#     def setTeam(self, myTeam):
#         self.__team = myTeam

#     def setRuns(self, myRuns):
#         self.__runs = myRuns

# p = CricketPlayer(18, "Virat", "India", 12000)

# print("----------Cricket Player details Before updating----------")
# print("Player ID :", p.getJerseyNo())
# print("Player Name :", p.getName())
# print("Team :", p.getTeam())
# print("Runs :", p.getRuns())

# p.setJerseyNo(45)
# p.setName("Rohit")
# p.setTeam("India")
# p.setRuns(11000)

# print("----------Cricket Player details After updating----------")
# print("Player ID :", p.getJerseyNo())
# print("Player Name :", p.getName())
# print("Team :", p.getTeam())
# print("Runs :", p.getRuns())

# Example 2

# class Patient:
#     def __init__(self, patientId, name, disease, bill):
#         self.__patientId = patientId
#         self.__name = name
#         self.__disease = disease
#         self.__bill = bill

#     def getPatientId(self):
#         return self.__patientId

#     def getName(self):
#         return self.__name

#     def getDisease(self):
#         return self.__disease

#     def getBill(self):
#         return self.__bill

#     def setPatientId(self, myPatientId):
#         self.__patientId = myPatientId

#     def setName(self, myName):
#         self.__name = myName

#     def setDisease(self, myDisease):
#         self.__disease = myDisease

#     def setBill(self, myBill):
#         self.__bill = myBill

# p = Patient(101, "Shravya", "Fever", 5000)

# print("----------Patient details Before updating----------")
# print("Patient ID :", p.getPatientId())
# print("Patient Name :", p.getName())
# print("Disease :", p.getDisease())
# print("Bill :", p.getBill())

# p.setPatientId(102)
# p.setName("Vidya")
# p.setDisease("Typhoid")
# p.setBill(8500)

# print("----------Patient details After updating----------")
# print("Patient ID :", p.getPatientId())
# print("Patient Name :", p.getName())
# print("Disease :", p.getDisease())
# print("Bill :", p.getBill())

# Example 3

class Product:
    def __init__(self, productId, name, category, price):
        self.__productId = productId
        self.__name = name
        self.__category = category
        self.__price = price

    def getProductId(self):
        return self.__productId

    def getName(self):
        return self.__name

    def getCategory(self):
        return self.__category

    def getPrice(self):
        return self.__price

    def setProductId(self, myProductId):
        self.__productId = myProductId

    def setName(self, myName):
        self.__name = myName

    def setCategory(self, myCategory):
        self.__category = myCategory

    def setPrice(self, myPrice):
        self.__price = myPrice

p = Product(501, "Laptop", "Electronics", 55000)

print("----------Product details Before updating----------")
print("Product ID :", p.getProductId())
print("Product Name :", p.getName())
print("Category :", p.getCategory())
print("Price :", p.getPrice())

p.setProductId(502)
p.setName("Mobile")
p.setCategory("Electronics")
p.setPrice(30000)

print("----------Product details After updating----------")
print("Product ID :", p.getProductId())
print("Product Name :", p.getName())
print("Category :", p.getCategory())
print("Price :", p.getPrice())