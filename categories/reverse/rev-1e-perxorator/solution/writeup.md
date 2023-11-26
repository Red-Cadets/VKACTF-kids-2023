## perXORator

| Событие | Название | Категория | Сложность |
| :------ | ---- | ---- | ---- |
| VKACTF kids 2023 | perXORator | Reverse engineering | Легкая |


### Описание


> Автор: [b3rcut7]
>
> Анжела позвонила нам и рассказала, что кто-то занимается эксфильтрацией данных.
>
>Нам удалось перехватить часть скрипта который шифрует информацию. Разберёшься?
>


### Решение


Попробуем узнать что такое s_box и как оно работает. Изучаем интернет и понимаем, что это матрица перестановки которая переводит наши значения из encoded_flag в какую-то новую последовательность. Назовём её new_s_box:
```python
for i in range(len(encoded_flag)):
    x = int("0x"+encoded_flag[i][0],16)
    y = int("0x"+encoded_flag[i][1],16)
    new_box.append(s_box[x][y])
```
Название задания отсылает нас на операцию исключающего ИЛИ (XOR). Применим на нашу новую последовательность данный нам ключ key:
```python
flag=""
for j in range(len(key)):
    flag+=binascii.hexlify(pwn.xor(new_box[j], binascii.unhexlify(key[j]))).decode()
print(binascii.unhexlify(flag))
```
Получаем флаг!

### Флаг


```
vka{this_is_the_real_flag_man_trust_me}
```
