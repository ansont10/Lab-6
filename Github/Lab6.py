def encode(password):
    user_input = input()
    encoded_res = ""
    for char in user_input:
        if char.isdigit():
            encoded_digits = (int(char) + 3) % 10
            encoded_res += str(encoded_digits)
        else:
            encoded_res += char
    return encoded_res
         
encoded_password = encode("password")
print(encoded_password)