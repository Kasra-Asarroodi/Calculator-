def simple_calculator():
    print(" SIMPLE CALCULATOR") 
    try:
        num1 = float(input("Enter first number: ")) 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    operator = input("Enter your operator (+, -, *, /): ")
    try:
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    if operator == "+":
        print(f"Results: {num1 + num2}")
    elif operator == "-":
     print(f"Results: {num1 - num2}")
    elif operator == "*":
     print(f"Results: {num1 * num2}")
    elif operator == "/":
     if num2 == 0:
        print("Error: Division by zero is not allowed.")
     else:
        print(f"Results: {num1 / num2}")
    else:
      print("Invalid operator. Please try again.")
      
    
    
   
        
        

def main():
    while True :
        simple_calculator()
        Answer = input("Do you want to perform another calculation? (yes/no): ")
        if Answer.lower() == "no":
            print("Thank you for using the simple calculator. Goodbye!")
            break
        elif Answer.lower() == "yes":
            print(" welcome back!'.")
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
           



if __name__ == "__main__":   
    main()
            