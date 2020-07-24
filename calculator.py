class Calculator:
    """This is a calculator class The idea is to
    implement class and static methods"""

    x = 0
    y = 0

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def divide(x, y):
        return x / y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def modulus(x, y):
        return x % y

    @classmethod
    def calculate(cls, option):
        if option == "+":
            return cls.add(cls.x, cls.y)
        elif option == "-":
            return cls.subtract(cls.x, cls.y)
        elif option == "*":
            return cls.multiply(cls.x, cls.y)
        elif option == "/":
            return cls.divide(cls.x, cls.y)
        elif option == "%":
            return cls.modulus(cls.x, cls.y)

    @classmethod
    def take_input(cls):
        cls.x = int(input("Please enter the first number = "))
        cls.y = int(input("Please enter the second number = "))
        print(f"x = {cls.x}\ny = {cls.y}")


if __name__ == "__main__":
    function_choice = 0
    while function_choice != -1:
        print("Enter 1 to input numbers")
        print("Enter 2 to add numbers")
        print("Enter 3 to subtract numbers")
        print("Enter 4 to multiply numbers")
        print("Enter 5 to divide numbers")
        print("Enter 6 to get modulus of numbers")
        function_choice = int(input())
        if function_choice == 1:
            Calculator.take_input()
        elif function_choice == 2:
            print(Calculator.calculate("+"))
        elif function_choice == 3:
            print(Calculator.calculate("-"))
        elif function_choice == 4:
            print(Calculator.calculate("*"))
        elif function_choice == 5:
            print(Calculator.calculate("/"))
        elif function_choice == 6:
            print(Calculator.calculate("%"))
        elif function_choice != -1:
            print("Wrong choice entered")
#Done