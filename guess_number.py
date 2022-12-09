# A number checking game
import random

number_limit = input("Enter a number ")
if not number_limit.isdigit():
    print("Enter a number next time")
    quit()
else:
    number_limit = int(number_limit)
print("Now guess a number between 1 &", number_limit, "until you win")

random_number = random.randint(1, number_limit)
c = 0
s = number_limit
while True:
    player_number = int(input("Enter your guess "))
    if player_number > number_limit:
        print("Enter a number between 1 &", number_limit)
    elif player_number == random_number:
        print("You win!!!")
        print("It took you", c, "number of tries")
        break
    else:
        c += 1
        print("You lose", "Come on keep going, You still have", s-c, "numbers to try")
