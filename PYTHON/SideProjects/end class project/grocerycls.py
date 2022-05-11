from datetime import date


class grocery:

    def __init__(self, name = "newProduct", producttype = "product"):
        self.name = name
        self.producttype = producttype
        self.cost = 0
        self.resaleprice = 0
        
        self.markup = 0.0
        self.discout = 0.0
        self.inventory = 0
        self.profit = 0

    def enterinv(self, newInv, newDate):
        self.inventory += newInv
        self.expdate = newDate
        return(self.inventory, self.expdate)

    def recordcost(self, newval):
        self.cost += newval
        return(self.cost)

    def addmarkup(self, percent):
        self.profit += self.cost * percent
        self.resaleprice += self.cost + self.profit
        print(self.resaleprice)
        return(self.resaleprice, self.profit)


class produce(grocery):
    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)
        self.expdate = date

class impulsepur(grocery):

    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)

class nonperish(impulsepur):

    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)

class candy(impulsepur):

    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)
        self.expdate = date

class beverages(grocery):

    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)
        self.sizeOz = 12
        self.expdate = date

class alcohol(beverages):

    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)
        self.alcperc = .075
        self.expdate = date

class nonalcholic(beverages):

    def __init__(self, name="newProduct", producttype="product"):
        super().__init__(name, producttype)
        self.expdate = date
