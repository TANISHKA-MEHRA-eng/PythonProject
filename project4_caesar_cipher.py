String = 'abcdefghijklmnopqrstuvwxyz'
def encrypt (plaintext, shift   ):
    ciphertext = ""
    for i in plaintext:
        x = String.find(i)
        if x == -1:
            ciphertext += i
        else:
            ciphertext += String[(x + shift) % 26]
    print(f"Here's the encrypted result : {ciphertext}")

def decrypt (ciphertext, shift):
    plaintext = ""
    for i in ciphertext:
        x = String.find(i)
        index = (x - shift) % 26
        if index < 0 :
            index += 26
        if x == -1:
            plaintext += i
        else:
            plaintext += String[index]
    print(f"Here's the decrypted result : {plaintext}")

p = 'True'
while p == 'True':
    ed = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n")
    message = input("Type your message:\n")
    key = int(input("Type the shift number:\n"))

    if ed == "encrypt":
        encrypt(plaintext = message, shift = key)
    elif ed == "decrypt":
        decrypt(ciphertext = message, shift = key)
    p1 = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if p1 == 'yes':
        p = 'True'
    else :
        p = 'False'