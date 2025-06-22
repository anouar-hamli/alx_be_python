from book_class import Book
from library_system import Book as LibBook, EBook, PrintBook, Library
from polymorphism_demo import Rectangle, Circle
from class_static_methods_demo import Calculator


def test_book_class():
    print("\n=== Testing Book Class (Magic Methods) ===")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)  # __str__
    print(repr(my_book))  # __repr__
    del my_book



def test_library_system():
    print("\n=== Testing Library System (Inheritance & Composition) ===")
    my_library = Library()

    # Add different types of books
    my_library.add_book(LibBook("Pride and Prejudice", "Jane Austen"))
    my_library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
    my_library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))

    # List all books
    my_library.list_books()


def test_polymorphism():
    print("\n=== Testing Polymorphism (Shapes) ===")
    shapes = [Rectangle(10, 5), Circle(7)]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


def test_class_static_methods():
    print("\n=== Testing Class/Static Methods ===")
    # Static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


def main():
    test_book_class()
    test_library_system()
    test_polymorphism()
    test_class_static_methods()


if __name__ == "__main__":
    main()