import cv2
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode

def decrypt_message(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    # Read the stored passcode
    if not os.path.exists("passcode.txt"):
        print("Error: No passcode file found.")
        return

    with open("passcode.txt", "r") as file:
        saved_password = file.read().strip()

    pas = input("Enter passcode for decryption: ")
    if pas != saved_password:
        print("YOU ARE NOT AUTHORIZED.")
        return

    # Ask the user for the private key input method
    key_method = input("Would you like to provide the private key from a file or paste the key as text? (file/text): ").strip().lower()

    if key_method == "file":
        # Ask for the private key file path
        private_key_file = input("Enter the path to the private key file (e.g., private.pem): ").strip()

        if not os.path.exists(private_key_file):
            print("Error: Private key file not found.")
            return

        with open(private_key_file, "rb") as f:
            private_key = RSA.import_key(f.read())

    elif key_method == "text":
        # Ask the user to paste the private key
        private_key_text = input("Please paste your private key: ").strip()

        try:
            private_key = RSA.import_key(private_key_text)
        except ValueError:
            print("Error: Invalid private key format.")
            return
    else:
        print("Invalid option. Please choose 'file' or 'text'.")
        return

    # Create a dictionary mapping ASCII values to characters
    ascii_to_char = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    encrypted_message_b64 = ""

    # Extract the encrypted message from the image
    while True:
        char_code = img[n, m, z]
        if char_code == 0:  # Stop at the null terminator.
            break
        encrypted_message_b64 += ascii_to_char[char_code]
        n += 1
        if n >= img.shape[0]:  # Move to the next row when reaching the end of a row.
            n = 0
            m += 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    # Decode the Base64 encoded encrypted message
    encrypted_message = b64decode(encrypted_message_b64.encode())

    # Decrypt the message using RSA
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()

    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    image_path = "encryptedImage.png"
    decrypt_message(image_path)
