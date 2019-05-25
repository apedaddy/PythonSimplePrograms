import random
# Generate a random list
length = random.randint(3,10)
original_list = random.sample(range(1,30),length)
print ("Original list:")
print(original_list)

def list_first_last(any_list):
    return [any_list[0],any_list[-1]]

print ("\nList of first and end value of original list")
print (list_first_last(original_list))