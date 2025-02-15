import cv2
import os

def decrypt_message(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    # Read the stored passcode.
    if not os.path.exists("passcode.txt"):
        print("Error: No passcode file found.")
        return

    with open("passcode.txt", "r") as file:
        saved_password = file.read().strip()

    pas = input("Enter passcode for decryption: ")
    if pas != saved_password:
        print("YOU ARE NOT AUTHORIZED.")
        return

    ascii_to_char = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    message = ""

    # Read characters until a null termination (ASCII 0) is encountered.
    while True:
        char_code = img[n, m, z]
        if char_code == 0:  # Stop at the null terminator.
            break
        message += ascii_to_char[char_code]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    print("Decryption successful! Hidden message:", message)

if __name__ == "__main__":
    image_path = "encryptedImage.png"
    decrypt_message(image_path)
