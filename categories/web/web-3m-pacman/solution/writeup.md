## Ва-Банк

| Событие | Название | Категория | Сложность |
| :------ | ---- | ---- | ---- |
| VKACTF kids 2022 | Ва-Банк  | Web | Средняя |

  
### Описание


> Автор: [ vChuk ]
>
> Открылся [новый банк](http:/some/site), за вход дают бонус! Связи с другими банками нет, но мы уже предлагаем интересные товары


### Решение

Ошибка заключается в проверке пересылаемого баланса. На сервере происходит проверка только, чтобы отсылаемое количество денег не превышало текущее, а затем вычитает из текущего баланса отсылаемое количество денег. Если отсылаемое количество денег отрицательное, то проверка на превышение денег пройдет и у отправителя баланс увеличится (минус на минус даёт плюс))

```python
if sendMoney > senderUser.money:
    return ("Недостаточно средств на счету", "danger")
else:
    try:
        senderUser.money -= sendMoney
        receiverUser.money += sendMoney
```

Необходимо зарегестрировать 2 аккаунта, затем совершить перевод денег, а во время пересылки успеть скопировать ссылку на переходной странице. В параметре `trmoney` поменять число на большое отрицательное. Затем перейти в магазин и купить флаг

### Флаг

```
vka{check_negative_values}
```