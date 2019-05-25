import random
import string

def pass_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

pass_length = int(input("Enter length of password in number: "))
print (pass_gen(pass_length))