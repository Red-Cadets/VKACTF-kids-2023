## RSmAll

| Событие | Название | Категория | Сложность |
| :------ | ---- | ---- | ---- |
| VKACTF kids 2023 | RSmAll v2   | Crypto | Средне |

## Описание

>Автор: Inssurg3nt
>
>Описание: На уроке информатики дали задание реализовать известную криптосистему. Это был мой первый подобный [проект](https://rsmall.vkactf.ru), и поэтому все получилось как-то странно и запутанно, но я все исправил!"

### Решение

Переходим на веб-сервис. По функционалу не густо, можем лишь получить зашифрованные даные.
Но модуль слишком мал и его можно просто напросто разложить (например при помощи функции factor() модуля sagemath) и расшифровать ключ.

Для расшифровки флага нужно отправить ключ в нужное поле.

Решение представлено на языке [Python](sploit.py).

### Флаг

Получаем наш флаг

```
vka{rsa_-_small_prime_edition!!}
```
