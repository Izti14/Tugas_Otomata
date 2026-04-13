import re

password = input("Masukkan password: ")
pattern = r'^(?=.*[A-Z])(?=.*[0-9]).{8,}$'

if re.match(pattern, password):
    print("Password kuat")
else:
    print("Password lemah")
    