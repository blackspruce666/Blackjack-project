print("Money zone")


def reset_account(money):
    money = 100.00

def add_money(money, bet):
    bet *= 1.5
    money += bet
    return money

def lose_money(money, bet):
    money -= bet
    return money