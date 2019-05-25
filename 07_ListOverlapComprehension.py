# Take two different list of different size
# Generate new list contains unique common numbers in both list.
import random

list_a = []
list_b = []
# Length of list can be anywhere between 10 digits to 20
length_list_a = random.randint(10,20)
length_list_b = random.randint(5,25)

# Get numbers randomly from 1 to 100 and add to the main_list
# Now main_list created and can be play around

while len(list_a) <= length_list_a:
    list_a.append(random.randint(1,25))

while len(list_b) <= length_list_b:
    list_b.append(random.randint(1,35))
print ("___________TWO LISTS WITH DIFFERENT LENGTH___________")
print ("FIRST LIST")
print (list_a)
print ("SECOND LIST")
print (list_b)
print()
overlap_list = [list_nums for list_nums in list_a if list_nums in list_b]
print ("List of unique numbers from both list:")
print (set(overlap_list))

