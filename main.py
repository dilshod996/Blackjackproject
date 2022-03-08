import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if 11 in cards and 10 in cards and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  elif user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
 
  
    
def start_game():
  print(logo)
  user_card = []
  computer_card = []
  is_game_over = False
  
  for x in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"   Your score: {user_card}, current score: {user_score}")
    print(f"   Computer's first card: {computer_card[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      get_next_card = input("Type 'y' to get another card or type 'n' to pass: ")
      if get_next_card =="y":
        user_card.append(deal_card())
      else:
        is_game_over = True
  while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)
  
  print(f"Your final card {user_card}, final score: {user_score}")
  print(f"Computer's final card: {computer_card}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play Blackjack game? Type 'y' or 'n':"):
  clear()
  start_game()