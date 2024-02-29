#Create a class named MathCalculator. In this class define a constructor that initialises an empty list called calculations_history which will be used to store calculation history. In Python, all variables that are initialised in a constructor are called instance variables or instance attributes. 1)Constructor is a special method in a class that is called init. 2)Constructor should contain parameter self.
#(Make your code clear and readable)
class MathCalculator:
    def __init__(self):
        self.calculations_history = []  # we are creating an empty list called "calculations_history" to store history of calculations

    def add(self, j, m):
        result = j + m
        self.calculations_history.append(f"{j} + {m} = {result}")  # we are storing the calculations to the the history
        return result

    def subtract(self, j, m):
        result = j - m
        self.calculations_history.append(f"{j} - {m} = {result}")  # process of storing the calculations in the history
        return result

# Creating the instance of MathCalculator
calculator = MathCalculator()

# We are performing calculations
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(15, 7)

# we are accessing the calculation history
print("Calculation History:")
for calculation in calculator.calculations_history:
    print(calculation)

#Add methods to the MathCalculator class for the following arithmetic operations: multiply(x, y): Multiplication of two numbers and also divide(x, y): Division of two numbers. Those methods should complete the operation and print out result in such format: '18 * 12 = 216'
class MathCalculator:
    def __init__(self):
        self.calculations_history = []  # Creaing the empty list called "calculations_history" for storing calculation history )

    def add(self, x, y):
        result = x + y
        self.calculations_history.append(f"{x} + {y} = {result}")  # procces of storing the calculation in the history
        return result

    def subtract(self, x, y):
        result = x - y
        self.calculations_history.append(f"{x} - {y} = {result}")  # procces of storing the calculation in the history
        return result

    def multiply(self, x, y):
        result = x * y
        self.calculations_history.append(f"{x} * {y} = {result}")  # procces of storing the calculation in the history
        return result

    def divide(self, x, y):
        if y != 0:  # Ensure not dividing by zero
            result = x / y
            self.calculations_history.append(f"{x} / {y} = {result}")  # procces of storing the calculation in the history
            return result
        else:
            print("Error: Cannot divide by zero.")
            return None

# proccess of creating the instance of MathCalculator
calculator = MathCalculator()

# Performing calculations
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(15, 7)
result_multiply = calculator.multiply(18, 12)
result_divide = calculator.divide(36, 6)

# Displaying the calculation history
print("Calculation History:")
for calculation in calculator.calculations_history:
    print(calculation)

#Modify the divide method in the MathCalculator class to handle division by zero errors. You can do this by checking if the denominator (the y parameter) is zero before performing the division operation. If y is zero, return a string 'Error: Division by zero is undefined' instead of performing the division. We should use if-else statement:
class MathCalculator:
    def __init__(self):
        self.calculations_history = []  # Creating the empty list called calculations_history to store calculation history

    def add(self, x, y):
        result = x + y
        self.calculations_history.append(f"{x} + {y} = {result}")  # storing the calculation to the history
        return result

    def subtract(self, x, y):
        result = x - y
        self.calculations_history.append(f"{x} - {y} = {result}")  # storing the calculation in the history
        return result

    def multiply(self, x, y):
        result = x * y
        self.calculations_history.append(f"{x} * {y} = {result}")  # storing the calculation in the history
        return result

    def divide(self, x, y):
        if y != 0:  # Check if the denominator is not zero
            result = x / y
            self.calculations_history.append(f"{x} / {y} = {result}")  # storing the calculation in the history
            return result
        else:
            error_message = 'Error: Division by zero is undefined'
            self.calculations_history.append(error_message)  # storing the error announcement in the history
            return error_message

# Create thee instance of MathCalculator
calculator = MathCalculator()

# Performing calculations
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(15, 7)
result_multiply = calculator.multiply(18, 12)
result_divide = calculator.divide(36, 6)
result_divide_by_zero = calculator.divide(42, 0)

# SHowing the calculation history
print("Calculation History:")
for calculation in calculator.calculations_history:
    print(calculation)

#Outside the MathCalculator class create an instance of MathCalculator. An instance, also known as an object, is a realisation of the class blueprint. It has the ability to use the functionality defined in the class, such as methods and attributes. Call multiply(x, y) and divide(x, y) methods to try out the created calculator. It should be possible to call the object's methods as following:
class MathCalculator:
    def __init__(self):
        # Making an empty list to store the calculation history
        self.calculations_history = []

    def add(self, x, y):
        # Perform addition proccess
        result = x + y
        # Record the calculation in the proper format
        self.calculations_history.append(f"{x} + {y} = {result}")
        return result

    def subtract(self, x, y):
        # Perform subtraction
        result = x - y
        # Record the calculation in the accurate format
        self.calculations_history.append(f"{x} - {y} = {result}")
        return result

    def multiply(self, x, y):
        # Perform multiplication process
        result = x * y
        # Recording the calculation in the good format
        self.calculations_history.append(f"{x} * {y} = {result}")
        return result

    def divide(self, x, y):
        if y != 0:
            # Performing hte division if the denominator is not zero (0)
            result = x / y
            # Recording the calculation process in the appropriate format
            self.calculations_history.append(f"{x} / {y} = {result}")
            return result
        else:
            # Making division wiht zero
            error_message = 'Error: Division by zero is undefined'
            self.calculations_history.append(error_message)
            print(error_message)
            return None

# Creating the instance for the MathCalculator
myCalculator = MathCalculator()

# multiplying and dividing methods
result_multiply = myCalculator.multiply(7, 17)
result_divide = myCalculator.divide(15, 5)

# Printing the our results
print("Result of multiplication:", result_multiply)
print("Result of division:", result_divide)

# showing the calculation history
print("Calculation History:")
for calculation in myCalculator.calculations_history:
    print(calculation)

#Update the multiply and divide methods to add a string representing the calculation to the calculationsHistory list before performing the calculation. The string should be in the format 'Expression: < expression >, Result: < result >':
class MathCalculator:
    def __init__(self):
        # Making an empty list for storing the calculation history
        self.calculations_history = []

    def add(self, x, y):
        # it is Performing addition
        result = x + y
        # Recording the calculation in the given format
        expression = f"{x} + {y}"
        self._record_calculation(expression, result)
        return result

    def subtract(self, x, y):
        # Performing subtraction process
        result = x - y
        # Recording the calculation in the proper format
        expression = f"{x} - {y}"
        self._record_calculation(expression, result)
        return result

    def multiply(self, x, y):
        # Performing multiplication process
        result = x * y
        # Recording the calculation in the appropriate format
        expression = f"{x} * {y}"
        self._record_calculation(expression, result)
        return result

    def divide(self, x, y):
        if y != 0:
            # Performing division
            result = x / y
            # Recording the calculation in the specified format
            expression = f"{x} / {y}"
            self._record_calculation(expression, result)
            return result
        else:
            # making division by zero
            error_message = 'Error: Division by zero is undefined'
            self.calculations_history.append(error_message)
            print(error_message)
            return None

    def _record_calculation(self, expression, result):
        # We should use "Helper" method to record the calculation in the proper format
        calculation_string = f"Expression: {expression}, Result: {result}"
        self.calculations_history.append(calculation_string)

# Creating the instance for the MathCalculator
myCalculator = MathCalculator()

# processes of multiplying and dividing
result_multiply = myCalculator.multiply(5, 14)
result_divide = myCalculator.divide(30, 6)

# Printing our results
print("Result of multiplication:", result_multiply)
print("Result of division:", result_divide)

# Making the updated calculation history
print("Calculation History:")
for calculation in myCalculator.calculations_history:
    print(calculation)

#Add a new method print_history to the MathCalculator class. This method should print out the calculationsHistory list. Method does not take any parameters and does not return any value. It should be possible to call the object's method as following:
class MathCalculator:
    def __init__(self):
        # creaing an empty list to store for the calculation history
        self.calculations_history = []

    def add(self, x, y):
        # Performing our addition process
        result = x + y
        # Recording the calculation in the format form
        expression = f"{x} + {y}"
        self._record_calculation(expression, result)
        return result

    def subtract(self, x, y):
        # Performing subtraction
        result = x - y
        # Recording the outcome of calculation
        expression = f"{x} - {y}"
        self._record_calculation(expression, result)
        return result

    def multiply(self, x, y):
        # Perform multiplication proccess
        result = x * y
        # Recording the calculation
        expression = f"{x} * {y}"
        self._record_calculation(expression, result)
        return result

    def divide(self, x, y):
        if y != 0:
            # Performing division
            result = x / y
            # Recording the calculation in the good form
            expression = f"{x} / {y}"
            self._record_calculation(expression, result)
            return result
        else:
            # Making division by zero
            error_message = 'Error: Division by zero is undefined'
            self.calculations_history.append(error_message)
            print(error_message)
            return None

    def print_history(self):
        # Printing our calculations history
        print("Calculation History:")
        for calculation in self.calculations_history:
            print(calculation)

    def _record_calculation(self, expression, result):
        # We should use "Helper" method to record the calculation in the good format
        calculation_string = f"Expression: {expression}, Result: {result}"
        self.calculations_history.append(calculation_string)

# Creating an instance of MathCalculator
myCalculator = MathCalculator()

# Making multiplying and dividing methods
result_multiply = myCalculator.multiply(5, 14)
result_divide = myCalculator.divide(30, 6)

# SHowing the results
print("Result of multiplication:", result_multiply)
print("Result of division:", result_divide)

# Printing final the updated calculation history using the new method
myCalculator.print_history()