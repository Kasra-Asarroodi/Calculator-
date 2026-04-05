def simple_calculator(): 
   print ('Simple calculator')
 
 
   while True:
    try:
     num1 = float(input("Enter first number: "))
     break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
   while True:
    operator = input("Enter your operator (+, -, *, /): ")
    if operator in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operator. Please enter +, -, *, or /.")

   while True:    
    try:
     num2 = float(input("Enter second number: "))
     break
    except ValueError:
        print("Invalid input. Please enter a valid number.") 
    
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
           