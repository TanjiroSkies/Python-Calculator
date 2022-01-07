def addition(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x,y):
    return x/y    

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
print("5.Exit")


while True:

     choice = input("Enter Choice (1/2/3/4/5): ")

     if choice in ('1', '2', '3', '4', '5'):

        
        num1 = float(input("Insert First Number: "))
        num2 = float(input("Insert Second Number:"))
         
        if choice == '5':
            break

        elif choice == '1':
        
         print(num1, "+", num2, "=", addition(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1,num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1,num2)) 
      
     next_calculation = input("Want another calculation? yes/no: ")
     if next_calculation == "no":
      break

