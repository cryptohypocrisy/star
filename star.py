# Task1
# Reproduce on the screen the next pattern

i = 0
star = 1

while True:
    numberOfLines = int(input("How many lines should the star use? "))
    
    if numberOfLines < 3:
        print("Star height must be at least 3 lines...")
    else:
        break

space = numberOfLines // 2

while i < (numberOfLines + 1):
    while i < (numberOfLines // 2):
        print(space * " ", star * "*", sep="")
        space -= 1
        star += 2
        i += 1
    print(space * " ", star * "*", sep="")
    space += 1
    star -= 2
    i += 1
