import os

class Price(object):
    def getPriceCode(self):
        pass

    def getCharge(self):
        pass

    def getFrequentRenterPoints(self, daysRent):
        return 1
    
class NewRelasePrice(Price):
    def getPriceCode(self):
        return Moive.NEW_RELEASE
    def getCharge(self, daysRent):
        return daysRent*3
    def getFrequentRenterPoints(self, daysRent):
        if daysRent > 1:
            return 2
        else:
            return 1
    
class RegularPrice(Price):
    def getPriceCode(self):
        return Moive.REGULAR

    def getCharge(self, daysRent):
        res = 2
        if daysRent > 2:
            res += (daysRent-2)*1.5
        return res
    
class ChildrensPrice(Price):
    def getPriceCode(self):
        return Moive.CHILDREN

    def getCharge(self, daysRent):
        res = 1.5
        if daysRent > 3:
            res += (daysRent - 3)*1.5
        return res
    
class Moive(object):
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1
    def __init__(self, title, priceCode):
        self.title = title
        self.price = priceCode
        self.priceCode = priceCode

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, x):
        self.__price = x

    @property
    def priceCode(self):
        return self.__price.getPriceCode()

    @priceCode.setter
    def priceCode(self, x):
        if x == self.REGULAR:
            self.price = RegularPrice()
        if x == self.CHILDREN:
            self.price = ChildrensPrice()
        if x == self.NEW_RELEASE:
            self.price = NewRelasePrice()
            
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self,x):
        self.__title = x
        
    def __str__(self):
        return "[Title: {:<10} Price: {:<5}]".format(self.title, self.priceCode)

    def getCharge(self, daysRent):
        return self.price.getCharge(daysRent)
    
    def getFrequentRenterPoints(self, daysRent):
        return self.price.getFrequentRenterPoints(daysRent)    

        
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
        return self.moive.getCharge(self.daysRent)
    
    def getFrequentRenterPoints(self):
        return self.moive.getFrequentRenterPoints(self.daysRent)
        
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

        res += self.statement() + "\n"
        res += self.htmlStatement()
        return res
    
    def statement(self):
        res_str = "Rental Record for {}\n".format(self.name)
        for each in self.rental_list:
            res_str += "\t {} \t {}\n".format(each.moive.title, each.getCharge())

        res_str += "Amount owed is {}\n".format(self.getTotalCharge())
        res_str += "You earned {} frequent renter points".format(self.getTotalFrequentRenterPoints())
        return res_str

    def htmlStatement(self):
        html_str = "<H1>Rental for <EM> {} </EM> </H1><P>\n".format(self.name)
        for each in self.rental_list:
            html_str += "{} : {} <BR>\n".format(each.moive.title, each.getCharge())
        html_str += "<P> You owe <EM> {} </EM><P>\n".format(self.getTotalCharge())
        html_str += "On this rental you earned <EM> {} </EM> frequent renter points<P>".format(self.getTotalFrequentRenterPoints())
        return html_str
        
    def getTotalCharge(self):
        res = 0
        for each in self.rental_list:
            res += each.getCharge()
        return res

    def getTotalFrequentRenterPoints(self):
        res = 0
        for each in self.rental_list:
            res += each.getFrequentRenterPoints()
        return res
    
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
