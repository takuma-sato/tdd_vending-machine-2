class VendingMachine:
    def __init__(self):
        self.total_money_amount = 0
        self.juice_dict = {"コーラ": {'price':120,'stock':5}}
        self.sales_amount = 0

    def insert_money(self, money):
        if money in [10, 50, 100, 500, 1000]:
            self.total_money_amount += money
            return
        else:
            return money

    def get_total_money_amount(self):
        return self.total_money_amount

    def refund_money(self):
        return self.total_money_amount

    def purchase(self, juice_name):
        pass
    
    #
    def check_stock(self, name):
        if name in self.juice_dict:
            return self.juice_dict[name]['stock']
        else:
            return None

    def check_price(self, name):
        if name in self.juice_dict:
            return self.juice_dict[name]['price']
        else:
            return None

    def check_purchace(self,name):
        if name not in self.juice_dict:
            return False
        elif self.total_money_amount < self.juice_dict[name]['price']:
            return False
        else:
            return self.juice_dict[name]['stock'] > 0

class JuicePrice:
    def __init__(self, price, name, stock) -> None:
        self.price = price
        self.name = name 
    

class JuiceStock:
    def __init__(self, stock, name) -> None:
        self.stock = stock
        self.name = name

    def set_stock