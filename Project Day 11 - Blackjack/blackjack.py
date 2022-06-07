from art import logo
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return (random.choice(cards))

def calculate_score(card_list):
  if sum(card_list) == 21 and len(card_list) == 2:
    return 0  #blackjack

  ace = 11
  if ace in card_list and sum(card_list) > 21:
    card_list.remove(ace)
    card_list.append(1)
  return sum(card_list)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose!"
  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "You lose, opponent has a Blackjack!"
  elif user_score == 0:
    return "You win with a Blackjack!"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Opponent went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

def play_game():
  print(logo)

  game_end = False
  user_cards = []
  computer_cards = []

  user_cards.append(deal_card())
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())

  while game_end == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")

    if user_score == 0 or user_score > 21 or computer_score == 0:
      game_end = True
    else:
      user_input = input("Do you want to get another card? Type 'y' to get another card. Type 'n' to pass:")
      if user_input == "y":
        user_cards.append(deal_card())
      else:
        game_end = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" The Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  play_game()
