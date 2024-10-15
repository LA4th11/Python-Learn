# Class for performing addition operation
class Addition:
    def case_addition(self, first_number, second_number):
        # Adds two numbers and returns the result
        return first_number + second_number

# Class for performing subtraction operation
class Subtraction:
    def case_subtraction(self, first_number, second_number):
        # Subtracts second number from the first and returns the result
        return first_number - second_number

# Class for performing multiplication operation
class Multiplication:
    def case_multiplication(self, first_number, second_number):
        # Multiplies two numbers and returns the result
        return first_number * second_number

# Class for performing division operation
class Division:
    def case_division(self, first_number, second_number):
        # Divides the first number by the second and returns the result
        return first_number / second_number

# Main block to run the calculator logic
if __name__ == "__main__":
    # Creating instances of each class
    addition_instance = Addition()
    subtraction_instance = Subtraction()
    multiplication_instance = Multiplication()
    division_instance = Division()
    
    # Variable to store the result of the operation
    result = 0
    # Variable to control the while loop for repeated operation
    user_reply = True
    # Variable to store the mathematical operator for display
    math_sign = ""
    
    # Loop to keep the program running until user decides to stop
    while(user_reply):
        # Displaying operation choices
        print("SELECT:\n1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n")
    
        # Taking user input for the operation choice and numbers
        user_input = input("Enter your choice: ")
        first_number = float(input("Enter your first number: "))  # Converts the input to a float
        second_number = float(input("Enter your second number: "))  # Converts the input to a float
        
        # Check user input and perform the corresponding operation
        if user_input == '1':
            math_sign = "+"  # Assigning operator symbol for addition
            result = addition_instance.case_addition(first_number, second_number)  # Performing addition
        
        elif user_input == '2':
            math_sign = "-"  # Assigning operator symbol for subtraction
            result = subtraction_instance.case_subtraction(first_number, second_number)  # Performing subtraction
        
        elif user_input == '3':
            math_sign = "*"  # Assigning operator symbol for multiplication
            result = multiplication_instance.case_multiplication(first_number, second_number)  # Performing multiplication
        
        elif user_input == '4':
            math_sign = "/"  # Assigning operator symbol for division
            result = division_instance.case_division(first_number, second_number)  # Performing division
        
        else:
            print("ERROR INPUT")  # Error message for invalid choice
        
        # Displaying the result in a formatted manner
        print(f"----------------\n{first_number} {math_sign} {second_number} = {result}\n----------------\n")
        
        # Asking user if they want to continue
        user_answer = input("Do you want to continue Y/N?: ").upper()  # Converts input to uppercase
        
        # Exit the loop if the user enters 'N'
        if user_answer == 'N':
            print("Thank you!")
            user_reply = False  # Stops the loop
