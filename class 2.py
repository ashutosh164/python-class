class Account:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        print('Account for : ' + self.name)

    def deposite(self, amount):
        if amount > 0:
            self.amount += amount

    def withdraw(self, amount):
        if amount > 0:
            self.amount -= amount

    def show_run(self):
        print(f"{self.name} = {self.amount}")


if __name__ == '__main__':
    ashu = Account('ashu', 0)
    ashu.deposite(23)
    ashu.deposite(7)
    ashu.deposite(10)
    ashu.show_run()
    jilu = Account('jilu',0)
    jilu.deposite(3)
    jilu.deposite(1)
    jilu.deposite(4)
    jilu.show_run()
    silu = Account('silu', 0)
    silu.deposite(4)
    silu.deposite(4)
    silu.show_run()
