import os

class Moive(object):
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1
    def __init__(self, title, priceCode):
        self.title = title
        self.priceCode = priceCode

    @property
    def priceCode(self):
        return self.__priceCode

    @priceCode.setter
    def priceCode(self, x):
        self.__priceCode = x

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,x):
        self.__title = x
        
    def __str__(self):
        return "[Title: {:<10} Price: {:<5}]".format(self.title, self.priceCode)

class Rental(object):
    def __init__(self,moive, daysRent):
        self.moive = moive
        self.daysRent = daysRent

    @property
    def moive(self):
        return self.__moive

    @moive.setter
    def moive(self, x):
        self.__moive = x

    @property
    def daysRent(self):
        return self.__daysRent

    @daysRent.setter
    def daysRent(self,x):
        self.__daysRent = x

    def __str__(self):
        return "Moive: {:<10}, daysRent: {:<5}".format(self.moive, self.daysRent)

    def getCharge(self):
        thisAmount = 0        
        c_moive_code = self.moive.priceCode
        if c_moive_code == Moive.REGULAR:
            thisAmount += 2
            if self.daysRent > 2:
                thisAmount += (self.daysRent -2)*1.5
        if c_moive_code == Moive.NEW_RELEASE:
            thisAmount += self.daysRent*3
        if c_moive_code == Moive.CHILDREN:
            thisAmount += 1.5
            if self.daysRent > 3:
                thisAmount += (self.daysRent - 3)*1.5
        return thisAmount
    
class Customer(object):
    def __init__(self, name):
        self.name = name
        self.rental_list = []
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,x):
        self.__name = x

    def addRental(self, x):
        self.rental_list.append(x)

    def statement(self):
        pass

    def __str__(self):
        res = "Name: {}\n".format(self.name)
        for i, rent in enumerate(self.rental_list):
            res += "[Rental No.{}/{:<3}]: {:<20}\n".format(i, len(self.rental_list), rent)

        res += self.statement()
        return res

    
    def statement(self):
        totalAmount = 0
        frequentRenterPoints = 0
        res_str = "Rental Record for {}\n".format(self.name)

        for each in self.rental_list:
            frequentRenterPoints += 1
            if each.moive.priceCode == Moive.NEW_RELEASE and each.daysRent > 1:
                frequentRenterPoints += 1

            res_str += "\t {} \t {}\n".format(each.moive.title, each.getCharge())
            totalAmount += each.getCharge()

        res_str += "Amount owed is {}\n".format(totalAmount)
        res_str += "You earned {} frequent renter points".format(frequentRenterPoints)
        return res_str
                
def f():
    m1 = Moive("Disney", 1)
    print(m1)
    print(Moive.CHILDREN)
    m2 = Moive("Japan", 2)
    m3 = Moive("US", 0)
    
    r1 = Rental(m1, 1)
    print(r1)
    r_lst = [r1, Rental(m1, 3), Rental(m2, 2), Rental(m3, 1)]

    c1 = Customer("Ran")
    for r in r_lst:
        c1.addRental(r)
    print(c1)
    
if __name__ == "__main__":
    f()
