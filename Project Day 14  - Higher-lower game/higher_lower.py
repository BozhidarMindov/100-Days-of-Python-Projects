from game_data import data
import art
import random

def get_random_person():
  return random.choice(data)

def format_data(person):
  name = person["name"]
  description = person["description"]
  country = person["country"]
  result = f"{name}, a {description}, from {country}"
  return result

def game():
  print(art.logo)
  
  score = 0
  person1 = get_random_person()
  person2 = get_random_person()
  game_end = False

  while game_end == False:
    person1 = person2
    person2 = get_random_person()

    while person1 == person2:
      person2 = random.chice(data)

    print(f"Compare A: {format_data(person1)}.")
    print(art.vs)
    print(f"Compare B: {format_data(person2)}.")

    guess = input("Guess who has more followers. Type 'A' or 'B': ").lower()

    correct_answer = ""
    if person1["follower_count"] > person2["follower_count"]:
      correct_answer = "a"
    else:
      correct_answer = "b"

  
    print(art.logo)
    
    if correct_answer == guess:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_end = True
      print(f"Sorry, that's wrong. Final score: {score}.")

game()
    