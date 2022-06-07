import random
from art import logo
from replit import clear

def choose_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return 10
  else:
    return 5

def play_game():
  print(logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  attempts_count = choose_difficulty()
  
  answer = random.randint(0, 101)
  end_game = False
  print(f"You have {attempts_count} attempts to guess the number.")
  
  while end_game == False:
    user_choice = int(input("Make a guess: "))
    if user_choice > answer:
      print(f"Too high!")
      attempts_count-= 1
    elif user_choice < answer:
      print("Too low!")
      attempts_count-= 1
    elif user_choice == answer:
      print(f"You got it! The answer was {answer}.")
      end_game = True
  
    if attempts_count == 0:
      print("You have no more guesses. You lose!")
      end_game = True
  if input("Do you want to play again? Type 'yes' or 'no': ") == "yes":
    clear()
    play_game()
    
play_game()
