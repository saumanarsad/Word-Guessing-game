import random
name = input ("What is your name")
print("Good luck %s !" % name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print("Guess the characters ")
turns = 12
count = 0
while turns !=0:
    guess = input("Enter your guess")
    if guess not in word:
        print("Wrong guess, You have %d tries remaining" % turns)
        turns-=1
    else:
        print("Correct guess , keep going")
        count +=1
else:
    print("Bad luck you lost")
if count == len(word):
    print("You win")

    

