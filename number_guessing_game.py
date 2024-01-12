from random import randint
from art import guess_logo

EASY_LEVEL=10
HARD_LEVEL=5

def difficulty():
    level=input("Enter the difficulty level : Type 'easy' or 'hard'").lower()
    if level=="easy":
        return EASY_LEVEL 
    elif level=='hard':
        return HARD_LEVEL 
    
def check_answer(answer,guess,turn):
 if guess < answer:
  print(f"Guesss is too high")
  return turn-1
 elif guess > answer:
  print(f"Guess is too low.")
  return turn-1
 elif guess==answer:
  print(F"Yo got it!  The answer was {answer}")        

        
def game():
 print(guess_logo)
 print("Welcome to the number guessing game\n")
 print("I'm thinking of number between 1 to 100")
    
 answer= randint(1, 100)
 turn= difficulty()
 guess= 0
 while guess!=answer:
  print(f"Remaing guess chance is {turn}")
  guess=int(input("Make a guess:\n"))
  turn=check_answer(guess,answer,turn)
  if turn==0:
    print("You are out of move,you lose")
    print(f"Guess number is {answer}")
    play_again=input("Doyou want to play again?type 'yes' or 'no'").lower()
    if play_again=="yes":
        return game()
    else:
        return 
       
game()