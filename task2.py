import random

# Function to generate tuple of two random numbers.
def random_tuple_gen():
    #generates a single digit number from 0 to 9
    tup_num = (random.randrange(1, 10), random.randrange(1, 10))
    return tup_num

#Function to validate user input unless he enters right value.
def multiplication_game(num1, num2):
    while True:
        output = int(input(f'How much is {num1} times {num2}? '))
        result = num1 * num2
        if result == output:
            print('Done.')
            break
        else:
            print(f'{num1} times {num2} is not {output}, please try again.' )  

#Calling Function random_tuple_gen and storing the tuple in variable. 
tuple_num = random_tuple_gen()
multiplication_game(tuple_num[0], tuple_num[1])
