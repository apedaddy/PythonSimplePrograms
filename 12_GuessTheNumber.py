# This is a guess number game using random function

from random import *

print ('Hello, what is your name?')
name = input()
secNo = randint(1,20)

print('Okay, '+name+', I have number in my head from 1 to 20')
count = 1
for yourTurn in range(1,7):
    print('Take a guess.')
    count +=1
    guess = int(input())
    if guess < secNo:
        print ('Your guess is low')
    elif guess >= secNo:
        print ('Your guess is higher')
    else:
        break

if guess == secNo:
    print ('Good job ' + name+ ' you made it right in '+ str(count)+ ' time(s)')
else:
    print
    print ('Sorry, '+name+', try later' + '\nThe number was '+ str(secNo))


