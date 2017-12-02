import random
secret = random.randint(1,10)
temp = input('please guess a number:')
guess = int(temp) 
while guess != secret:
    if guess > secret:
        print('that is so bigger')
    else:
        print('that is too small')
    temp = input("please try again:\n")
    guess = int(temp)

print('Wow, you are so clever')
print('but you do not have prize')       
print('game over')
