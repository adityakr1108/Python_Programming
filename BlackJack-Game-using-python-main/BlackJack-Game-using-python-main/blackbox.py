# this is the program where we are palying a game name as black box in which we have score less tahn 21

import random
import os

def deal_card():
    card=[1,2,3,4,5,6,7,8,9,10,11,10,10,10]
    return random.choice(card)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score,computer_score):

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has black jack"
    elif user_score == 0:
        return "Wins with a black jack"
    elif user_score > 21:
        return "Lose, Score is greater than 21"
    elif computer_score > 21:
        return "Wins, dealer score is greater than 21"
    else:
        if user_score > computer_score:
            return "Wins, with highest score"
        else:
            return "Lose..."
def play_game():
    print( """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    user_cards=[]
    computer_cards=[]
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over=False
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your Cards{user_cards}, Current Score: {user_score}\nComputer First Cards : {computer_cards[0]}")

        if computer_score == 0 or user_score==0 or user_score >21:
            is_game_over=True
        else:
            user_should_deal=input("Type Y to get another card and type N to pass: ").upper()
        if user_should_deal == 'Y':
            user_cards.append(deal_card())
            user_score=calculate_score(user_cards)
        elif user_should_deal == 'N':
            is_game_over = True
        else:
            print("You have enter wrong character")
            
    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score= calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Computer_score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want too play the game? Y / N ").upper() == 'Y':
    play_game()


