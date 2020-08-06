class VendingMachine:
    def __init__(self):
        self.total_money_amount = 0

    def insert_money(self, money):
        self.total_money_amount += money

    def get_total_money_amount(self):
        return self.total_money_amount

    def refund_money(self):
        return self.total_money_amount

