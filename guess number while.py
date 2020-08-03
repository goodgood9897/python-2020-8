import random
number = random.randint(1,10)
while True:
    usernumber = int(input('Please enter 1~10.'))
    if usernumber == number:
        print('Good!!')
        break
    else:
        print('Errow!')