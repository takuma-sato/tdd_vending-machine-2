from vending_machine.vending_machine import VendingMachine


class TestVendingMachine:
    def test_insert_money(self):
        vm = VendingMachine()
        vm.insert_money(10)
        assert vm.total_money_amount == 10
        vm.insert_money(1)
        assert vm.total_money_amount == 10

    def test_get_total_money_amount(self):
        vm = VendingMachine()
        vm.insert_money(10)
        vm.insert_money(500)
        vm.insert_money(1000)
        assert vm.get_total_money_amount() == 1510

    def test_refund_money(self):
        vm = VendingMachine()
        vm.insert_money(10)
        vm.insert_money(500)
        vm.insert_money(1000)
        assert vm.refund_money() == 1510

    ### todo
    def test_check_stock(self):
        vm = VendingMachine()
        name ='コーラ'
        assert vm.check_stock(name) == 5
        name ='スプライト'
        assert vm.check_stock(name) is None

    def test_check_price(self):
        vm = VendingMachine()
        name ='コーラ'
        assert vm.check_price(name) == 120
        name ='スプライト'
        assert vm.check_price(name) is None

    def test_check_purchace(self):
        vm = VendingMachine()
        name ='コーラ'
        vm.insert_money(10)
        assert vm.check_purchace(name) == False
        vm = VendingMachine()
        name ='スプライト'
        vm.insert_money(10)
        assert vm.check_purchace(name) == False
        vm = VendingMachine()
        name ='スプライト'
        vm.insert_money(500)
        assert vm.check_purchace(name) == False
        vm = VendingMachine()
        name ='コーラ'
        vm.insert_money(500)
        assert vm.check_purchace(name) == True
        