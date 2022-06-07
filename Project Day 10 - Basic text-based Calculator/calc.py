from art import logo
from replit import clear

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print (logo)

  n1 = float(input("What's the first number you want to enter?: "))
  
  for item in operations:
    print(item)

    to_continue = False

  while to_continue == False:
    operator = input("Pick an operation: ")
    n2 = float(input("What's the second number you want to enter?: "))
    calc_func = operations[operator]
    result = calc_func(n1, n2)
    print(f"{n1} {operator} {n2} = {result}")

    go_next = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if go_next  == 'y':
        n1 = result
    else:
      to_continue == True
      clear()
      calculator()
        
calculator()
