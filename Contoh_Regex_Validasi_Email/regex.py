import re

email = input("Masukkan email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Email valid")
else:
    print("Email tidak valid")
    
