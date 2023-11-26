def atbash_decipher(encrypted_text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{}_"
    reversed_alphabet = alphabet[::-1]
    
    result = ""
    for char in encrypted_text:
        if char in alphabet:
            index = reversed_alphabet.index(char)
            result += alphabet[index]
        else:
            result += char
    return result

encrypted_text = "HScCaUNVYLAVcKAbYYPAZYXIKYZB"
decrypted_text = atbash_decipher(encrypted_text)
print("Расшифрованный текст:", decrypted_text)
