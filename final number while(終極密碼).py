import random
a = 1
b = 100
number = random.randint(1,100)

while True:
    print('Now%d-%d'%(a,b))
    answer = int(input('Please enter nummber:'))
    if answer<a or answer>b:
        print('Please enter again.')
    elif answer>number:
        b=answer
    elif answer<number:
        a=answer
    elif answer==number:
        print('correct~~~!')
        break