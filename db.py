import csv


def read_file():
    record = []
    try:
        with open ("money.csv", newline = "") as f:
            reader = csv.reader(f)
            for row in reader:
                record.append(row)
        return record[-1][0]
    except FileNotFoundError:
        pass
    else:
        return record[-1][0]


def write_file(money):
    with open("money.csv", "a", newline = "\n") as f:
        writer = csv.writer(f, delimiter = " ")
        writer.writerow(money)


def reset_account():
    money = 100.00
    write_file("ACCOUNT RESET")
    write_file([str(money)])



def add_money(money, bet):
    bet *= 1.5
    money = round(money + bet)
    write_file([str(money)])
    return money


def lose_money(money, bet):
    money = round(money - bet, 2)

    write_file([str(money)])
    return money
