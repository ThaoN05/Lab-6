def encode(password):
    if len(password) != 8 or not password.isdigit():
        raise ValueError("Password must be an 8-digit string containing only integers.")
    encoded_password = ''.join([str((int(digit) + 3) % 10) for digit in password])
    return encoded_password


def decode(encoded_password):
    # sofi's decode function
    decoded_password = ''.join([str((int(digit) + 7) % 10) for digit in encoded_password])
    return decoded_password


def main():
    while True:
        # Display menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # Get user input
        choice = input("Please enter an option: ")

        if choice == '1':
            # Encode password
            password = input("Please enter your password to encode: ")
            try:
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            except ValueError as e:
                print(e)

        elif choice == '2':
            # add decode function and remove "pass"
            decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        elif choice == '3':
            # Quit program
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 to Encode or 2 to Quit.")


if __name__ == '__main__':
    main()
 jj
 jj