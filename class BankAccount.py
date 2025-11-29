class BankAccount:
    """Клас, що представляє банківський рахунок."""
    def __init__(self, initial_balance=0):
        if initial_balance >= 0:
            self._balance = initial_balance
        else:
            self._balance = 0
            print("Початковий баланс не може бути від'ємним. Встановлено баланс 0.")
    def deposit(self, amount):
        """Метод для внесення коштів на рахунок."""
        if amount > 0:
            self._balance += amount
            print(f"Внесено: {amount}. Поточний баланс: {self._balance}")
        else:
            print("Сума внесення повинна бути додатною.")

    def withdraw(self, amount):
        """Метод для зняття коштів з рахунку."""
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Знято: {amount}. Поточний баланс: {self._balance}")
        else:
            print("Недостатньо коштів або сума зняття некоректна.")

    def get_balance(self):
        """Метод для отримання поточного балансу."""
        return self._balance

def main():
    acc = BankAccount(1000)
    print(f"Поточний баланс: {acc.get_balance()}")

    acc.deposit(500)
    acc.withdraw(200)
    acc.withdraw(2000)
    acc.deposit(-100)
    print(f"Кінцевий баланс: {acc.get_balance()}")

main()


        

        