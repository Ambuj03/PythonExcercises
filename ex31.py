word = "EVAPORATED"
clueWord = word[0:len(word) // 2 - 1]

wordList = list(word)
idx = len(word)//2 - 1
idxIncrement = idx

print(clueWord)

while(True):

    gLetter = input("Guess the word letter by letter:")
    if(gLetter == wordList[idxIncrement]):
            print("Right guess")
            idxIncrement += 1
    else:
          print("Wrong guess, try again!")

    if(idxIncrement == len(wordList)):
          print("Congrats, the words was {}".format(word))
          break