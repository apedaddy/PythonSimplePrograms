print("__________THIS PROGRAM PRINT DIVISOR OF GIVEN NUMBERS__________")
print()
num = int(input("Enter your number: "))
    # Get a copy to print at the end of line
bak = num
    # List will have no numbers at first
divisor_list = []
    # Start from 2 to half of the numbers to discard 1 and number itself.

for divisor_check in range (2, int(num/2)+1):
    check = num % divisor_check
    if check == 0:
        divisor_list.append(divisor_check)
print (f"\nGiven number: {bak} is divided by following numbers")
print(divisor_list)