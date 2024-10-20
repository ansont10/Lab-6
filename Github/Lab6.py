# Anson Tran
def encode():
    user_input = input()
    encoded_res = ""
    if len(user_input) == 8 and user_input.isdigit():      
        for char in user_input:
            encoded_digits = (int(char) + 3) % 10
            encoded_res += str(encoded_digits)
        return encoded_res
    else:
        return "Invalid input, please enter an 8 digit password."
        
         
encoded_password = encode()
print(encoded_password)