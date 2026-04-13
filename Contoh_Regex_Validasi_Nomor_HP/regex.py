import re

pattern = r'^08[0-9]{8,11}$'

nomor = input("Masukkan nomor HP: ")

if re.match(pattern, nomor):
    print("Nomor HP valid")
else:
    print("Nomor HP tidak valid")

