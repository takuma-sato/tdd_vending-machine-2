class VendingMachine:
    def __init__(self):
        self.total_money_amount = 0
        self.juice_dict = {
            "コーラ": Juice(price=120, name="コーラ", stock=5)
        }  # Juiceと本数を渡す {"cola":(Juice, stock)}
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
        # if juice_name in self.juice_dict.keys():
        #     self.juice_dict[juice_name].stock > 0


class Juice:
    def __init__(self, price, name, stock) -> None:
        self.price = price
        self.name = name
        self.stock = stock
