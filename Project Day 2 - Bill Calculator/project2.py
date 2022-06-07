print("Welcome to the tip calcualtor")
bill = float(input("What was the total bill?"))

tip = int(input("What percentage tip would you like to give? 10%, 12% or 15%?"))

if tip == 10 or tip == 12 or tip ==15:
  tip = tip
else:
  print("Wrong tip, asking again")
  tip = int(input("What percentage tip would you like to give? 10%, 12% or 15%?"))

people = int(input("How many people to split the bill?"))

totalBill = round(tip/100 * bill + bill, 2)
print(f"The total bill is ${totalBill}")

billPerPerson = round(totalBill/people, 2)

print(f"Each person should pay ${billPerPerson}")