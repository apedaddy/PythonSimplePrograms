import random
comp_num = random.randint(1,9)
print (comp_num)
user_num = 0
attempt = 0

while user_num != comp_num or gameon == 'n':
    user_num = int(input("Enter your number: "))
    attempt +=1
    if (user_num <1 and user_num>9):
        print ("not valid number")
        break
    elif (user_num == comp_num):
        print(f"\nCongratulations your number {user_num} is a correct guess")
        print (f"You made it correct guess in total {attempt} attempt")
        break

    else:
        print ("\nWrong entry!")

    gameon = str.lower(input("Play Again! (Y/N)"))
    if gameon == 'n':
        break
    elif gameon == 'y':
        continue
    else:
        print ("Please enter valid choices Y or N")
        break
print ("\nGood Bye!")



