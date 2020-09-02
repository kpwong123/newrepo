import random

words =[]
with open("dict.txt") as f:
    line = f.readline().strip
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)

ans = random.choice(words).lower()

guess = str(input("Please input an alphabet to play Hangman!: "))

anslist = []
for x in ans:
    anslist.append(x)

print(anslist)

count = 6
while anslist != []:
    if guess == anslist[0]:
        if len(anslist) == 1:
            print("Congrats! You win!")
            break
        else:
            guess = str(input("Correct! You have " + str(count) + " chances left. Please guess the next alphabet: "))
            anslist.pop(0)
    elif guess != anslist[0]:
        if count == 1:
            print("Sorry! You lose!")
            break
        else:
            count -= 1
            guess = str(input("Incorrect! You have " + str(count) + " chances left. Guess again: "))