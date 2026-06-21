import random
import string

print("Welcome to the Password Generator!")
n = input("How many letters would you like in your password? ")
random_lists = random.choices(string.ascii_letters, k = int(n))

m = int(input("How many symbols would you like? "))
random_lists1= random.choices(string.punctuation, k=m)

l = int(input("How many numbers would you like? "))
random_lists2= random.choices(string.digits, k=l)

final_list = random_lists + random_lists1 + random_lists2

random.shuffle(final_list)
final = ''.join(final_list)
print(final)