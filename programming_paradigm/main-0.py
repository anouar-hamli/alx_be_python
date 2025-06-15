import sys
from bank_account import BankAccount
from robust_division_calculator import safe_divide
from library_management import Book, Library

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

def library_operations(args):
    # Create a Library instance and pre-populate some books
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    if len(args) == 0:
        print("Usage: python main.py library <command> [<book_title>]")
        print("Commands: list, checkout:<title>, return:<title>")
        sys.exit(1)

    command = args[0]
    if command == "list":
        print("Available books:")
        library.list_available_books()
    elif command.startswith("checkout:"):
        title = command.split(":", 1)[1]
        if library.check_out_book(title):
            print(f"Checked out '{title}'")
        else:
            print(f"Book '{title}' is not available or does not exist.")
    elif command.startswith("return:"):
        title = command.split(":", 1)[1]
        if library.return_book(title):
            print(f"Returned '{title}'")
        else:
            print(f"Book '{title}' was not checked out or does not exist.")
    else:
        print("Invalid command for library. Use list, checkout:<title>, or return:<title>.")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py bank <command>:<amount>")
        print("  python main.py divide <numerator> <denominator>")
        print("  python main.py library <command>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    args = sys.argv[2:]

    if mode == "bank":
        bank_operations(args)
    elif mode == "divide":
        division_operations(args)
    elif mode == "library":
        library_operations(args)
    else:
        print("Invalid mode. Choose 'bank', 'divide', or 'library'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
