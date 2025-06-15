import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide

def bank_operations(args):
    if len(args) < 1:
        print("Usage: python main.py bank <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    command, *params = args[0].split(':')
    amount = float(params[0]) if params else None
    account = BankAccount(100)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

def division_operations(args):
    if len(args) != 2:
        print("Usage: python main.py divide <numerator> <denominator>")
        sys.exit(1)
    numerator = args[0]
    denominator = args[1]
    result = safe_divide(numerator, denominator)
    print(result)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py bank <command>:<amount>")
        print("  python main.py divide <numerator> <denominator>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    args = sys.argv[2:]

    if mode == "bank":
        bank_operations(args)
    elif mode == "divide":
        division_operations(args)
    else:
        print("Invalid mode. Choose 'bank' or 'divide'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
