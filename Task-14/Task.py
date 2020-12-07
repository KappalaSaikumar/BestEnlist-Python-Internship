class CoffeeMaker(object):

    Report={"Water":1000,
        "Milk":1000,
        "Coffee":100,
        "Money":20}

    def __init__(self):
        pass

    def start(self,type,money):
        #self.name=input("What would you like : ")
        self.name=type
        if self.name=="report":
            return (self.report())
        elif self.name=="espresso":
            return espresso.func(self,money)
        elif self.name=="latte":
            return latte.func(self,money)
        elif self.name=="cappuccino":
            return cappuccino.func(self,money)
        else:
            return ("Invalid")
            self.start()

    def report(self):
        return ("Water: ",self.Report["Water"],"ml \nMilk: ",self.Report["Milk"],"ml \nCoffee: ",self.Report["Coffee"],"g \nMoney: $",self.Report["Money"])
        self.start()

class espresso(CoffeeMaker):
    def func(self,money):
        self.__emoney=money #float(input("Enter Money : "))
        if(self.Report["Water"]>=250 and self.Report["Milk"]>=200 and self.Report["Coffee"]>=30 and self.__emoney>=float(3)):
            self.Report["Water"]-=250
            self.Report["Milk"]-=200
            self.Report["Coffee"]-=30
            self.Report["Money"]+=3
            if(self.__emoney>3):
                return ("Here's your change : ",str(self.__emoney-3),"Here's your espresso. Enjoy!")
            return ("Here's your espresso. Enjoy!")
            self.start()
        elif self.__emoney<3:
            return ("Not enough money")
            self.start()
        else:
            return ("There are no enough resources .. Sorry !")

class latte(CoffeeMaker):
    def func(self,money):
        self.__lmoney=money#float(input("Enter Money : "))
        if(self.Report["Water"]>=200 and self.Report["Milk"]>=150 and self.Report["Coffee"]>=24 and self.__lmoney>=2.5):
            self.Report["Water"]-=200
            self.Report["Milk"]-=150
            self.Report["Coffee"]-=24
            self.Report["Money"]+=2.5
            if(self.__lmoney>2.5):
                return ("Here's your change : ",str(self.__lmoney-2.5),"Here's your latte. Enjoy!")
            return ("Here's your latte. Enjoy!")
            self.start()
        elif self.__lmoney<2.5:
            return ("Not enough money")
            self.start()
        else:
            return ("There are no enough resources .. Sorry !")

class cappuccino(CoffeeMaker):
    def func(self,money):
        self.__cmoney=money#float(input("Enter Money : "))
        if(self.Report["Water"]>=275 and self.Report["Milk"]>=160 and self.Report["Coffee"]>=33 and self.__cmoney>=float(5.0)):
            self.Report["Water"]-=275
            self.Report["Milk"]-=160
            self.Report["Coffee"]-=33
            self.Report["Money"]+=5
            if(self.__cmoney>5):
                return ("Here's your change : ",str(self.__cmoney-5),"Here's your cappuccino. Enjoy!")
            return ("Here's your cappuccino. Enjoy!")
            self.start()
        elif self.__cmoney<5:
            return ("Not enough money")
            self.start()
        else:
            return ("There are no enough resources .. Sorry !")
