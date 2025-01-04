import random

word = []
with open('sowpods.txt') as f:
   for line in f: 
        word.append(line)
    
   rand_idx = random.randint(0,len(word))
   print(word[rand_idx])