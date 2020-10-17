import random

def is_prime(integer):
    if integer <= 1:
        return False
    for i in range(2,integer):
        if integer % i==0:        
            return False
    return True

for i in range(6):
    number = random.randint(1, 100)  #randint generates a number from an inclusive range.
    result = is_prime(number)
    if result == False:
        print(f'The random number {number} is not a prime number.')
    else:
        print(f'The random number {number} is a prime number.')



     
