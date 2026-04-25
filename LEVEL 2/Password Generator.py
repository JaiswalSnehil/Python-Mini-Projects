import random
import string

def generate_strong_password(length):
    if length < 4:
        return "Password length should be at least 4."

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    all_chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password += random.choices(all_chars, k=length-4)

    random.shuffle(password)

    return ''.join(password)


length = int(input("Enter password length: "))
print("Generated Password:", generate_strong_password(length))