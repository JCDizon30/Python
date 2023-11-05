import random
num = random.randrange(1,100)
answer = int(input("Enter Number: "))
while num != answer:
    if answer == num:
        break
    elif answer < num:
        print("Lower")
        answer = int(input("Try again: "))
    elif answer > num:
        print("Higher")
        answer = int(input("Try again: "))
print("You Guess It!")

#coded by: Lance Pagcu Chincuanco and John Carlo Dizon