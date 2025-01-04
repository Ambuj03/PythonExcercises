import random

Pmove = input("""Welcome to Rock, Paper Scissors Game
                 Choose your move('R' for Rock, 'P' for paper,
                                  'S' for Scissors):""")

rand = random.randint(1,4)

print("Your Move : ", Pmove)

# 1 - rock, 2- paper, 3 scissors
if(rand == 1):
    Cmove = 'R'
elif(rand == 2):
    Cmove = 'P'    
else:
    Cmove = 'S' 

print("Computer's Move : ", Cmove)

if Pmove == Cmove:
    print("Draw....")

if(Cmove == 'R' and Pmove =='S'):
    print("You lost...")
elif(Cmove == 'P' and Pmove =='R'):
    print("You lost...")
elif(Cmove == 'S' and Pmove =='P'):
    print("You lost...")

if(Cmove == 'S' and Pmove =='R'):
    print("You Win...")
elif(Cmove == 'R' and Pmove =='P'):
    print("You Win...")
elif(Cmove == 'P' and Pmove =='S'):
    print("You Win...")