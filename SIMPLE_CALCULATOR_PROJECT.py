#calculator with basic features

print("------Welcome to the Simple Calculator--------")
print("""Select options 1/2/3/4/5/6/7/8/9
       1. for addition
       2. for subtraction
       3. for multiplication
       4. for square        
       5. for root        
       6. for cube
       7. for cuberoot
       8. for division
       9. for exit  """)

while True:
      try:
           a = float(input("Enter a first number:"))
           choice = int(input("Enter your choice:"))
           b = float(input("Enter a second number:"))
           if choice == 1:
               result = (a+b)
               print(f"{a}+{b} = {result}")
        
           elif choice == 2:
               result = (a-b)
               print(f"{a}-{b} = {result}")
           elif choice == 3:
                result = (a*b)
                print(f"{a}*{b} = {result}")
           
           elif choice == 4:
                result = (a*a)
                print(f"{a}^{2} = {result}")
           elif choice == 5:
                result = (a**(1/2))
                print(f"{a}^{1/2} = {result}")
           elif choice == 6:
                result = (a*a*a)
                print(f"{a}^{3} = {result}")
           elif choice == 7:
                result = (a**(1/3))
                print(f"{a}^{1/3} = {result}")
           elif choice == 8:
                if b == 0:
                      raise ZeroDivisionError("Cannot divide by zero!")
                result = a /b
           else:
                raise ValueError("Invalid operator. Use +, -, *, /")
           print(f"{a}/{b} : {result}")
      except ValueError as ve:
            print(f"Value Error: {ve}\n")
      except ZeroDivisionError as zde:
            print(f"Math Error: {zde}\n")
      except Exception as e:
            print(f"Something went wrong: {e}\n")
      again = input("Do you want to perform another calculation? (yes/no): ").lower()
      if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break



    
    
  




