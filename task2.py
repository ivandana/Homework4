import random

def multiplication_game():
    while True:
        (num1, num2) = random.randrange(0, 10), random.randrange(0, 10)
        output = int(input(f'How much is {num1} times {num2}? '))
    
        result = num1 * num2
        if result == output:
            print('Done.')
            break
        else:
            print(f'{num1} times {num2} is not {output}, please try again.' )  

multiplication_game()
