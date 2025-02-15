import cv2
import os
from decrypt import decrypt_message  # Import decryption function

def encrypt_message(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Create a dictionary mapping characters to their ASCII values.
    char_to_ascii = {chr(i): i for i in range(255)}
    
    n, m, z = 0, 0, 0

    # Embed each character from the message.
    for char in msg:
        img[n, m, z] = char_to_ascii[char]
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    # Add a null termination character (ASCII 0) to mark the end of the message.
    img[n, m, z] = 0

    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # Open the encrypted image
    print("Message successfully encrypted into image.")

    # Save the passcode for decryption.
    with open("passcode.txt", "w") as file:
        file.write(password)

if __name__ == "__main__":
    image_path = r"C:\Users\pc\Desktop\intenship project\mypic.png"
    output_path = "encryptedImage.png"
    encrypt_message(image_path, output_path)

    # Ask the user if they want to decrypt immediately.
    choice = input("Do you want to decrypt the message now? (y/n): ").strip().lower()
    if choice == "y":
        decrypt_message(output_path)
    else:
        print("You can run decrypt.py later to decrypt the message.")
