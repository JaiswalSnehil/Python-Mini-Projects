# Simple Caesar Cipher File Encryptor

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def save_to_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)


def read_from_file(filename):
    with open(filename, "r") as f:
        return f.read()


def main():
    print("=== Caesar Cipher File Encryptor ===")
    print("1. Encrypt and Save")
    print("2. Read and Decrypt")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter shift value: "))

        encrypted_text = encrypt(text, shift)
        print("Encrypted:", encrypted_text)

        filename = input("Enter filename to save: ")
        save_to_file(filename, encrypted_text)
        print("Saved successfully!")

    elif choice == "2":
        filename = input("Enter filename to read: ")
        shift = int(input("Enter shift value used earlier: "))

        encrypted_text = read_from_file(filename)
        decrypted_text = decrypt(encrypted_text, shift)

        print("Decrypted:", decrypted_text)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()