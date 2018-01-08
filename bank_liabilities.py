class Bank:

    def __init__(self, rr, checkable_deposits=0, required_reserves=0, excess_reserves=0, loans=0):
        self.loans = loans
        self.excess_reserves = excess_reserves
        self.required_reserves = required_reserves
        self.checkable_deposits = checkable_deposits
        self.rr = rr

        self.current_loans = 0
        self.transaction_num = 0

    def deposit(self, amount):
        self.checkable_deposits += amount
        self.required_reserves += amount * self.rr
        self.excess_reserves += amount - (amount * self.rr)
        self.print()

    def loan_all(self):
        self.loans += self.excess_reserves
        self.current_loans = self.excess_reserves
        self.excess_reserves = 0
        self.print()

    def deposit_loans(self):
        self.checkable_deposits += self.current_loans
        self.required_reserves += self.current_loans * self.rr
        self.excess_reserves += self.current_loans - (self.current_loans * self.rr)
        self.print()

    def print(self):
        print("\nTransaction Num: " + str(self.transaction_num))
        print("Assets                   |                Liabilities")
        print("Required Reserves: " + str(self.required_reserves) + " | Checkable Deposits: " + str(self.checkable_deposits))
        print("Excess Reserves: " + str(self.excess_reserves))
        print("Loans: " + str(self.loans))
        self.transaction_num += 1

bank = Bank(.1)
bank.deposit(5000)
bank.loan_all()
bank.deposit_loans()
bank.loan_all()
bank.deposit_loans()
input()
