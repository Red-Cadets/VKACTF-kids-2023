## Отважные парни

| Событие | Название | Категория | Сложность |
| :------ | ---- | ---- | ---- |
| VKACTF kids 2023 | Отважные парни  | Crypto | Легкая |

  
### Описание


> Автор: Inssurg3nt
>
> Совсем недавно самые 'отважные' парни из нашего класса проникли в кабинет информатики, чтобы узнать пароль от папки CS на своих рабочих компьютерах. Но пароль оказался зашифрован...

### Решение

Посмотрев на [исходный код](./source.py), можно убедиться, что дана программа, шифрующая пароли. При этом используется шифр Атбаш, по сути, простая замена символов на зеркальные в алфавите. Написав обратный алгоритм, можно получить пароль, который и является флагом. 

```python 
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
print("флаг:", decrypted_text)


```


### Флаг

```
vka{cipher_has_been_defused}
```
