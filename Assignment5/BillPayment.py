class Bill:
    def __init__(self, amount):
        self.amount = amount


class Cash(Bill):
    def pay(self):
        print(f"Paid Rs.{self.amount} by Cash")


class Cheque(Bill):
    def pay(self):
        print(f"Paid Rs.{self.amount} by Cheque")


# Driver code
cash_payment = Cash(500)
cheque_payment = Cheque(1000)

cash_payment.pay()
cheque_payment.pay()
