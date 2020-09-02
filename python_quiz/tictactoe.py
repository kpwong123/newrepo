dim = int(input("Please indicate the dimensions of the game board: "))

for _ in range(dim):
    for x in range(dim):
        print(" ---", end = "")
    print()
    for y in range(dim + 1):
        print("|   ", end = "")
    print()
for z in range(dim):
    print(" ---", end = "")