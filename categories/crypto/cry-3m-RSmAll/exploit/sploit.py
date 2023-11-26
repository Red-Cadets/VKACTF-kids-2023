import requests
import json
from Crypto.Util.number import inverse, long_to_bytes
from sage.all import *

URL_encrypted_key = "http://localhost:8000/rsa_rsa/get_encrypted_key/"
URL_decrypt_FLAG = "http://localhost:8000/rsa_rsa/decrypt/{key}/"

def get_encrypted_key():
    r = requests.get(URL_encrypted_key)
    json_ans = json.loads(r.text)
    return json_ans

def get_decrypt_FLAG(key):
    r = requests.get(URL_decrypt_FLAG.format(key=key))
    json_ans = json.loads(r.text)
    return json_ans['FLAG']

data = get_encrypted_key()
p_0 = int(data['main_p'])
N = int(data['n'])
e = int(data['e'])

enc_key = int(data['enc_key'], 16)
p, q = int((str(factor(N)).split(" * "))[0]), int((str(factor(N)).split(" * "))[1])

print(f"p = {p}", f"q = {q}")
d = inverse(e, (p - 1) * (q - 1))
secret = pow(enc_key , d, N)
secret = long_to_bytes(secret)
print(f"Secret : {secret.decode()}")

FLAG = get_decrypt_FLAG(secret.hex())
print(FLAG)
