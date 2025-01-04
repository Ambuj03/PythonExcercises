import random

word = []
with open('sowpods.txt') as f:
   for line in f: 
        word.append(line)
    
   rand_idx = random.randint(0,len(word))

nGuesses = 0 #Total are 6

word = str(word[rand_idx])
clueWord = word[0:len(word)//2]

wordList = list(word)
idx = len(word)//2

print(clueWord)

while(True):

    gLetter = input("Guess the word letter by letter:")
    if(gLetter == wordList[idx]):
            print("Right guess")
            idx += 1
    else:
          nGuesses+=1
          
          if(nGuesses == 6):
               print("You've ran out of chances..")
               break
          
          else :
               print("Wrong guess, try again!, No. of guesses left is {}" .format(6-nGuesses))
      

    if(idx == len(wordList)-1):
          print("Congrats, the words was {}".format(word))
          break