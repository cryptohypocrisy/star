# Task1
# Reproduce on the screen the next pattern

i = 0
star = 1
numberOfLines = int(input("How many lines should the star use? "))
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
