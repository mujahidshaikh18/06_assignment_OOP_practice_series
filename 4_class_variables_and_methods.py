class Bank:
    bank_name = "Bank of Python"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {self.bank_name}")

account1 = Bank("Rehan")
account2 = Bank("Mujahid")

account1.display_info()
account2.display_info() # Display initial bank name

Bank.change_bank_name("Askari") # Change bank name

account1.display_info()
account2.display_info() # Display updated bank name
