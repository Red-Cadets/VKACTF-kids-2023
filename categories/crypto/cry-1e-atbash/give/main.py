def atbash_cipher(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}_"
    reversed_alphabet = alphabet[::-1]
    
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result += reversed_alphabet[index]
        else:
            result += char
    return result

flag = ???
encrypted_text = atbash_cipher(flag)
print("Зашифрованный пароль:", encrypted_text)