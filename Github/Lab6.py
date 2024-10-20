# Anson Tran

def encode():
    user_input = input("Enter an 8 digit password to encode: ")
    encoded_res = ""
    if len(user_input) == 8 and user_input.isdigit():      
        for char in user_input:
            encoded_digits = (int(char) + 3) % 10
            encoded_res += str(encoded_digits)
        return encoded_res
    else:
        return "Invalid input, please enter an 8 digit password."
    print(encoded_res)
def decode():
    decoded_res = ""
    for char in encoded_password:
        decoded_digits = (int(char) - 3) % 10
        decoded_res += str(decoded_digits)
    return decoded_res

program_continue = True
while program_continue:
    print("\nMenu\n1. Encode\n2. Decode\n3. Exit")
    try:
        menu_selection = int(input("Select an option: "))
        if menu_selection == 1:
            encoded_password = encode()
            print(encoded_password)
        elif menu_selection == 2:
            decoded_password = decode()
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif menu_selection == 3:
            program_continue = False
        else:
            print("Invalid selection, please select one of the options")
    except ValueError:
        print("Invalid input, please select one of the options.")