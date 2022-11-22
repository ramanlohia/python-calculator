from  art import logo

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  print(logo)
  to_continue = True
  num1=float(input("Enter the first number: "))
  for key in operations:
    print(key, end=" , ")
    
  while to_continue == True:
    operation_symbol=input("\nPick an operation:\n")
    num2=float(input("Enter the another number: "))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ")
    if choice=='y':
      num1=answer
    else:
      to_continue=False
      calculator()

calculator()