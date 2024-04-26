from replit import clear
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount):
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if direction == "encode":
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]
        print(f"The decoded text is {cipher_text}")
    else:
        print("it is do not valid")



end_encrypt = True
while end_encrypt:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(plain_text=text, shift_amount=shift)
    clear()
    final_res = input("type 'yes' if you want to go again. Otherwise type 'no':").lower()
    if final_res == "yes":
        end_encrypt = True
    elif final_res == "no":
        end_encrypt = False
        print("Goodbye")


# ----------My own code--------
# letters = list(text)
# number_of_letters = len(letters)
# alphabet_number = len(alphabet)
# text_encrypt = []
# def encrypt():
#    for x in range(0,number_of_letters):
#        for s in range(0,alphabet_number):
#            if letters[x] == alphabet[s]:
#                vari = shift + s
#                if vari >= alphabet_number:
#                    num = len(alphabet[s])
#                text_encrypt.append(alphabet[vari])
#    print(f"{''.join(text_encrypt)} == {text}")



# def encrypt(plain_text, shift_amount):
#    cipher_text = ""
#    for letter in plain_text:
#        position = alphabet.index(letter)
#        new_position = position + shift_amount
#        cipher_text += alphabet[new_position]
#    print(f"The encoded text is {cipher_text}")


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
#    cipher_text = ""
#    for letter in plain_text:
#        position = alphabet.index(letter)
#        new_position = position - shift_amount
#        cipher_text += alphabet[new_position]
#    print(f"The decoded text is {cipher_text}")

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# e.g.
# cipher_text = "mjqqt"
# shift = 5
# plain_text = "hello"
# print output: "The decoded text is hello"


# TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == "encode":
#    encrypt(plain_text = text, shift_amount = shift)
# elif direction == "decode":
#    decrypt(plain_text=text,  shift_amount=shift)
# else:
#   print("it is do not valid")
