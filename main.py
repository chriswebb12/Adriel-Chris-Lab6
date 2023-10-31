# Adriel Poon

def encode(password):
    # take in an 8-digit password in string format containing only integers.x
    # After passing the password into the encoder, the encoder stores the encoded password to a new
    # variable, with each digit being shifted up by 3 numbers
    encoded_password = ''
    for digit in password:
        # Shift the digit up by 3 numbers
        encoded_digit = str((int(digit) + 3))
        encoded_password += encoded_digit

    return encoded_password




def menu_display():
    # Displays Menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print('3. Quit')


def main():
    global password
    while True:
        menu_display()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Enter the password to encode: ')
            password = encode(password)
            print("Your password has been encoded and stored!")
        if menu_option == 2:
            print(f"The encoded password is {password} and the original password is {decode(password)}")
        if menu_option == 3:
            break


if __name__ == '__main__':
    main()





