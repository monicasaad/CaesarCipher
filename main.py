# import logo
from art import logo

print(logo)


# create list with all letters off the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# define function to encrypt/ decrypt text
def cipher(mode, plain_text, shift_amount):
    # create empty string to add coded text
    coded_text = ""
    # account for if shift is greater than number of letters in alphabet
    shift_amount %= 26
    for character in plain_text:
        if character in alphabet:
            if mode == "encode":
                coded_text += alphabet[alphabet.index(character) + shift_amount]
            elif mode == "decode":
                coded_text += alphabet[alphabet.index(character) - shift_amount]
        # if character is a space/number/symbol add as is
        else:
             coded_text += character
    print(f"The {mode}d text is \"{coded_text}\".")


# create variable for whether user wants to continue or not
continue_coding = True


while continue_coding:
    # Get user inputs for message and cipher
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # call cipher function
    cipher(mode=direction, plain_text=text, shift_amount=shift)

    # check if user wants to stop
    run = input("Type 'yes' if you would like to go again. Otherwise type 'no'.\n").lower()

    # exit if user types no
    if run == "no":
        print("Goodbye.")
        continue_coding = False
