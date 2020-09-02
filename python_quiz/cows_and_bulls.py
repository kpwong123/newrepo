import random

guess = int(input("Please make a guess on the 4-digit number: "))

ans = random.randint(1000, 9999)

guesslist = []
anslist = []

def addlist():
    for x in str(guess):
        guesslist.append(int(x))
    for y in str(ans):
        anslist.append(int(y))

addlist()

attempts = 0
while guesslist != anslist:
    print(guesslist)
    attempts += 1
    cowcount = 0
    for z in range(4):
        if guesslist[z] == anslist[z]:
            cowcount += 1
            anslist[z] = "m"
            guesslist[z] = "mm"

    # print(anslist)
    bullcount = 0
    for zz in range(4):
        for zzz in range(4):
            if guesslist[zz] == anslist[zzz]:
                anslist[zzz] = "n"
                guesslist[zz] = "nn"
                bullcount += 1

    # print(anslist)
    guesslist.clear()
    anslist.clear()
    print("number of cows: ", cowcount)
    print("number of bulls: ", bullcount)
    guess = int(input("Please Try Again: "))
    addlist()
else:
    print("Congratulations! You've tried", attempts, "times")    