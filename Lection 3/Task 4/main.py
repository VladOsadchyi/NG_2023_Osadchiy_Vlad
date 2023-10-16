import hashlib
import itertools
provided_hash = 'e186022d0931afe9fe0690857e32f85e50165e7fbe0966d49609ef1981f920c6'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
all_combinations = [''.join(p) for p in itertools.product(alphabet, repeat=4)]
for password in all_combinations:
    calculated_hash = hashlib.sha256(password.encode()).hexdigest()
    if calculated_hash == provided_hash:
        print("Your password: ", password)