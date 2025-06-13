# Simple Calculator Program

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def sub(x, y):
    """Return the difference of x and y."""
    return x - y

def mul(x, y):
    """Return the product of x and y."""
    return x * y

def main():
    """Main function to run the calculator."""
    print("-"*10,"Simple Calculator", "-"*10)
    print("Select option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Enter choice (1/2/3): ")
    if choice in ('1', '2'):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == '1':
            print(f"Result = {add(a, b)}")
        elif choice == '2':
            print(f"Result = {sub(a, b)}")
        elif choice == '3':
            print(f"Result = {mul(a, b)}")
    else:
        print("Invalid Input!")


if __name__ == "__main__":
    main()