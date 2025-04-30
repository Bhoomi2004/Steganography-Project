import cv2
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from Crypto.Random import get_random_bytes

def encrypt_message(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Generate RSA keys (or load existing keys)
    key = RSA.generate(2048)  # Generate a new RSA key pair (public + private)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    # Save private and public keys to files
    with open("private.pem", "wb") as private_file:
        private_file.write(private_key)
    with open("public.pem", "wb") as public_file:
        public_file.write(public_key)

    # Encrypt the message using the public key
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_message = cipher.encrypt(msg.encode())  # Encrypt the message

    # Base64 encode the encrypted message to safely embed it in the image
    encrypted_message_b64 = b64encode(encrypted_message).decode()

    # Create a dictionary mapping characters to their ASCII values
    char_to_ascii = {chr(i): i for i in range(255)}

    # Ensure the image has enough space to store the message
    image_size = img.shape[0] * img.shape[1] * 3  # Total number of pixels in the image.
    message_size = len(encrypted_message_b64) + 1  # Include null terminator

    if image_size < message_size:
        print(f"Encryption failed: {message_size} bytes needed for message, but there is only space for {image_size} bytes.")
        return

    n, m, z = 0, 0, 0

    # Embed the encrypted message in the image
    for char in encrypted_message_b64:
        img[n, m, z] = char_to_ascii[char]
        n += 1
        if n >= img.shape[0]:  # Move to next row when reaching the end of a row.
            n = 0
            m += 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    # Add a null terminator (ASCII 0) to the end of the message
    img[n, m, z] = 0

    # Save the image with the embedded message
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")  # Open the encrypted image
    print("Message successfully encrypted into image.")

    # Save the passcode for decryption
    with open("passcode.txt", "w") as file:
        file.write(password)

if __name__ == "__main__":
    image_path = r"C:\Users\bhoom\Downloads\Steganography-Project\mypic.png"
    output_path = "encryptedImage.png"
    encrypt_message(image_path, output_path)

    
