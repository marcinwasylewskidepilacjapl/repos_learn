class Result:
    def __init__(self, isSuccess, message, value=None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        """ tu jest cos co sprawdza, czy pieniądze są prawdziwe"""
        self.balance += amount
        print("Jestem rodzicem")
    def try_withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            return  Result(True, "Wypłacono kasę", amount)
        return Result(False, "Nie wypłacono", amount)
    def __str__(self):
        return str(self.balance)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance
    # def deposit(self, amount):
    #     """ tu jest cos co sprawdza, czy pieniądze są prawdziwe"""
    #     self.balance += amount
    #     print("Jestem dzieckiem")
    def try_withdraw(self, amount):
        if (self.balance - amount > self.minimumBalance):
            return super().try_withdraw(amount)
        else:
            return Result(False, "Nie udało się, próba przekroczenia progu", amount)


# konto = BankAccount()
# konto.deposit(1000)
# result = konto.withdraw(400)
# for i in result:
#     print(result[i])
accountMin = MinimumBalanceAccount(1500, 1000)
result = accountMin.try_withdraw(300)
# accountMin.deposit(500)
print(result.message)