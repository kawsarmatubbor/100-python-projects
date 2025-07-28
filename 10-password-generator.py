import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*()_-+=[]{}|;:,.<>?"
all_chars = lowercase + uppercase + digits + special

password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special)
]

for i in range(4):
    password.append(random.choice(all_chars))

final_password = ''.join(password)

print(f"Password : {final_password}")