import random
import string
user = int(input('Enter the length of the password (atleast 8): '))
print()
guess = ''.join(random.choices(string.ascii_letters + string.digits, k=user))
# print(guess)
if user >= 8:
    for x in guess:
        print('*', end='')
else:
    print('Password should be of atleast 8 characters!')