"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.
"""

def atm() -> None:
    fb_list = []
    def interest_on_balance(current_balance: float, count_of_dw: int) -> list:
        count_of_dw = (count_of_dw + 1) % interest_occurrence
        if count_of_dw == 0:
            current_balance = balance * (1 + interest)
        return [current_balance, count_of_dw]

    def current_balance_print(balances: float) -> None:
        print(f"Current balance is {balances}")

    def wealth_tax(current_balnce: float, thresh: float, tax_rate: float) -> float:
        if current_balnce > thresh:
            current_balnce = current_balnce * (1 - tax_rate)
        return current_balnce

    balance = 0
    threshhold = 5000000000
    tax = .1
    withdrawal_fee = .015
    min_fee = 30
    max_fee = 600
    count_of_deposit_withdrawal = 0
    interest_occurrence = 3
    interest = .03
    while True:
        command = input('Available options are "D - Deposit", "W - Withdraw ", '
                        'P - Payment history, "E - Exit": ').lower()
        match command:
            case "d":
                correct_input = False
                while not correct_input:
                    deposit = input("Please input multiple of 50 to deposit: ")
                    correct_input = deposit.isdigit() and (int(deposit) % 50 == 0) and int(deposit) > 0
                    balance = wealth_tax(balance, threshhold, tax)
                    if not correct_input:
                        print("Incorrect input")
                        current_balance_print(balance)
                balance += int(deposit)

                after_interest_list = interest_on_balance(balance, count_of_deposit_withdrawal)
                balance, count_of_deposit_withdrawal = after_interest_list[0], after_interest_list[1]
                current_balance_print(balance)
                fb_list.append(f"Deposit {deposit}")


            case "w":
                correct_input = False
                while not correct_input:
                    withdraw = input("Please input sum to withdraw: ")
                    balance = wealth_tax(balance, threshhold, tax)
                    correct_input = withdraw.isdecimal() and int(withdraw) > 0
                    if correct_input:
                        fee = min(max(min_fee, int(withdraw) * withdrawal_fee), max_fee)
                        if (int(withdraw) + fee < balance):
                            withdraw = int(withdraw) + fee
                        else:
                            correct_input = False
                    if not correct_input:
                        print("incorrect input")
                        current_balance_print(balance)
                balance -= int(withdraw)
                after_interest_list = interest_on_balance(balance, count_of_deposit_withdrawal)
                balance, count_of_deposit_withdrawal = after_interest_list[0], after_interest_list[1]
                current_balance_print(balance)
                fb_list.append(f"Withdraw {withdraw}")

            case "e":
                return

            case "p":
                print(fb_list)
            case _:
                balance = wealth_tax(balance, threshhold, tax)
                print("Incorrect command")
                current_balance_print(balance)


atm()