menu = """

[d] Deposit
[s] Withdraw
[e] Statement
[q] Quit

=> """

balance = 0
limit = 500
statement = ""
withdrawals_number = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = input(menu)

    if option == "d":
        value = float(input("Enter the deposit amount: "))
        print("Deposit successful!!!!")
        if value > 0:
            balance += value
            statement += f"Deposit made, statement: R$ {value:.2f}\n"

        else:
            print("Operation failed! The value entered is not valid.")

    elif option == "s":
        value = float(input("Enter the withdrawal amount: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdrawals = withdrawals_number >= WITHDRAWAL_LIMIT

        if exceeded_balance:
            print("Operation failed! You're broke.")

        elif exceeded_limit:
            print("Operation failed! The withdrawal amount exceeds the limit allowed by the bank.")

        elif exceeded_withdrawals:
            print("Operation failed! You have exceeded the withdrawal limit.")

        elif value > 0:
            balance -= value
            statement += f"Withdrawal: R$ {value:.2f}\n"
            withdrawals_number += 1

        else:
            print("Operation failed! The entered value is invalid.")

    elif option == "e":
        print("\n================ STATEMENT ================")
        print("No transactions were made." if not statement else statement)
        print(f"\nBalance: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Invalid operation, please select a valid operation.")
