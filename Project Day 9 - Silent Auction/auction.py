from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program")
end = False
bidders_dictionary = {}

while end == False:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))

  bidders_dictionary[name] = bid

  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
  
  if more_bidders == "no":
    end = True
  elif more_bidders == "yes":
    clear()

highest = 0
for bidder in bidders_dictionary:
  current_bid = bidders_dictionary[bidder]
  if current_bid > highest:
    highest = current_bid
    winner = bidder

print(f"The winner is {winner} with a bid of ${highest}.")

                      
