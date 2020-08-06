import random
a = 1
b = 1000
num = random.randint(a,b)

while True:
    print('Now number:%d-%d'%(a,b))
    answer = int(input('Please enter the number:'))
    if answer > b or answer < a:
        print('Errow! Please enter number again.')
    elif answer > num:
        b = answer
    elif answer < num:
        a = answer
    elif answer == num:
        print('Congratlatins~!')
        break
    