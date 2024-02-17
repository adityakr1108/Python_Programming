from art import logo, vs
from game_data import data
import random
from replit import clear
print(logo)
score = 0
game_should_continue = True
account_b=random.choice(data)
while game_should_continue:
  account_a=account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)
  
  def format_data(account):
    account_name=account['name']
    account_description=account['description']
    account_country=account['country']
    
    return f'{account_name},{account_description} from {account_country}'
  print(f'Compare A: {format_data(account_a)}')
  print(vs)
  print(f'Against B: {format_data(account_b)}')
  
  guess = input("Which has more follower: Type 'A' or 'B' ").lower()
  
  a_follower=account_a['follower_count']
  b_follower=account_b['follower_count']
  def check(guess,a_follower,b_follower):
    if a_follower > b_follower:
      return guess == 'a'
    else:
      return guess == 'b'

  clear(
    
  )
  is_correct = check(guess,a_follower,b_follower)
  if is_correct == True:
    score+=1
    print(f"Wow you are right.Your current score is {score}")
  else:
    game_should_continue = False
    print(f"Sorry, you guessed wrong.Your final score is {score}")
  
   
   
  
  




