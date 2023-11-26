# Бруталити

| Cобытие       | Название       | Категория | Сложность |
|:-------------:|:-------------: |:---------:|:---------:|
| VKAСTF Kids 2023 | Бруталити | Forensics | Hard |

## Описание

>Автор [0xR1st0]
>
>Когда один говорит БРУТ, все кричат ФОРС. Когда один говорит РОК, все подхватывают Ю. Когда один сказал ВЕРА, все 11 человек вдруг замолчали.

[Mega](https://mega.nz/file/v74CiboY#qCbJ5m9_0uIO1XgFHfovsQdFoIRXtHHP2hSBp_0xBNc)
[DropMeFiles](https://dropmefiles.com/WbSMl)

# Решение

Нам дан зашифрованный архив и исходя из названия и описания надо его взломать.
Устанавливаем утилиту fcrackzip и rockyou.txt, взламываем архив по словарю.
Пароль - cobedangyeu3012.
Детельная инструкция по пользованию утилитой - https://bookflow.ru/fcrackzip-tool-vzlom-parolya-zip-fajla-v-kali-linux/?ysclid=lp7ibomyy5839566414.
Далее перед нами образ, зашифрованный veracrypt.
И также исходя из описания взламываем пароль методом брутфорса.
Детальные инструкции - https://ru.linux-console.net/?p=16426&ysclid=lp7eoe9dum206912750 https://codeonby.com/2022/01/19/brute-force-veracrypt-encryption/.
Пароль от образа - 13372190861.
Внутри образа заманчивый файл.
Расшифруем данную строку через привычный нам метод brute force, но уже с xor.

### Флаг
```
vka{BruT4l_bRut_l4b}
```
