#!/usr/bin/ python3

from binascii import unhexlify
from Crypto.Util.number import bytes_to_long, getPrime , long_to_bytes

intro = ("""   

          !GPPPPPPPP?                                                                   
          P@@@@@@@@@#                                                                   
       @@@7      ^!~J@@@@@@P                                                            
   .!!7PGG~      :^:!###GPGY!!!                                                         
   J@@@   .^:::::::::^^^   ~@@@.                                                        
G##J^^^::::^:!#&&7:^^~~~:..:^^^G###########BB#########BBB##########BB###!               
@@@J   ^^^~7!?&&&Y!7!~~~^:^.   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&@Y...            
&@@J   :::G@@&   G@@&~~~^::::::^~~^::^^~^~~~~~~~^:^^^^^^~~^::::^^.      ?@@&            
&@@5 ..:::G@@#   G@@&~~~^:::^^^^^^^^^^^~~^^^^^^^^^^:::::^:!P55^:::......5@@@            
&@@P::::::G@@#   G@@&~~~^::^^^^^~^~!!!!!!^::::::^~~^::::::?@@@!::^~^~!!~G@@@            
@@@G:^^:::^!~7&&&J~!~^^^:::^~~~&@@@@@@@@@@&@@@@@&&@#777#&&G...B&@P:::777B@@@            
G##P???^:::::~&&&7::::::^^^~YJJB################@@@&7?7&@@B   &@@B^^^7?7B@@@            
   J@@@~^^::::::::::::::^~~5@@@.                G@@&777&@@B   &@@#77777!B@@@            
   .!!7B##?^^^^^^^^^7BBB###P!!!                 :!!?#&&J!!^   ^!!Y&&&&&&5!!~            
       &@@P!7777777!Y@@@@@@5                       .@@@:         !@@@@@@?               
          P@@@@@@@@@#                                                                   
          !GPPPPPPPP?                                                                   
          
          """)

print(intro)

FLAG = open("SuperSecretflag.txt" , "rb").read()
KEY = open("SuperSecretkey.txt" , "rb").read()

class Cipher():
    def __init__(self):
        self.p = getPrime(256)
        self.q = getPrime(256)
        self.e_1 = getPrime(256)
        self.e_2 = getPrime(256)
        self.N = self.p * self.q
        print(f"N: {self.N}")
        print()

    def encrypt(self, pt):
        if len(pt) == 0:
            return 0
        ct_1 = b""
        ct_2 = b""
        pt_num = bytes_to_long(pt)
        
        ct_1 = long_to_bytes(pow(pt_num , self.e_1 , self.N))
        ct_2 = long_to_bytes(pow(pt_num , self.e_2 , self.N))

        return ct_1, ct_2
 
    def decrypt(self,ct):
        return self.encrypt(ct)
    
def check_input(phrase):
    while True:
        try:
            your_input = int(input(phrase))
            break
        except:
            print("Invalid int format")
    return your_input

def check_input_hex(phrase):
    while True:
        try:
            your_input = unhexlify(input(phrase))
            break
        except:
            print("Invalid hex format")
    return your_input.hex()

cipher = Cipher()

while True:

    print()
    print("[1] - Зашифровать текст")
    print("[2] - Расшифровать текст")
    print("[3] - Получить флаг")
    print("[4] - Получить зашифрованный ключ")
    print("[0] - Выход")
    print()

    your_input = check_input("Выберите действие: ", )
    print()

    if your_input == 1:

        pt = check_input_hex("Введите исходный текст в hex-формате: ")

        ct_1, ct_2 = cipher.encrypt(bytes.fromhex(pt))
        print(f"Шифротекст первый: {ct_1.hex()}") 
        print(f"Шифротекст второй: {ct_2.hex()}")  

    elif your_input == 2:

        ct = check_input_hex("Введите зашифрованный текст в hex-формате: ")
        pt_1, pt_2 = cipher.decrypt(bytes.fromhex(ct))
        print(f"Исходный текст: {pt_1.hex()}")

    elif your_input == 3:
        input_password = input("Введите ключ: ")

        if input_password.encode() == KEY:
            print(FLAG)
        else:
            print("Ключ неверный!")    

    elif your_input == 4:
        print("Ключ:")
        enc_key_1, enc_key_2 = cipher.encrypt(KEY)
        print(enc_key_1.hex())
        print("Ну или...")
        print(enc_key_2.hex())

    elif your_input == 0:
        print("Игра окончена . . .")
        exit()

