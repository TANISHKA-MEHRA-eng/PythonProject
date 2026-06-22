import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

print('Welcome to Password Generator!')
n_letters = int(input('How many letters would you want in your password?\n'))
n_symbols = int(input('How many symbols would you want in your password?\n'))
n_numbers = int(input('How many numbers would you want in your password?\n'))
password = []

for i in range(n_letters):
    password += random.choice(letters)
for i in range(n_symbols):
    password += random.choice(symbols)
for i in range(n_numbers):
    password += random.choice(numbers)
random.shuffle(password)
print(password)
pass1 = ""
for i in password:
    pass1 += i
print(pass1)