import random

main_list = []
# Length of list can be anywhere between 10 digits to 20
length_main_list = random.randint(10,20)

# Get numbers randomly from 1 to 100 and add to the main_list
# Now main_list created and can be play araound

while len(main_list) <= length_main_list:
    main_list.append(random.randint(1,100))

# Now main list is created and is in the memory
# _______________LIST COMPREHENSION__________
# Subset of all even numbers:
even_list = [num for num in main_list if num %2 ==0]
odd_list = [num for num in main_list if num %2 != 0]
doubles_list = [num*2 for num in main_list]

print ("_____MAIN LIST_____")
print (main_list)
print (f"\nList of even numbers: \n{even_list}")
print (f"\nList of odd numbers: \n{odd_list}")
print (f"\nList of doubles numbers: \n{doubles_list}")

