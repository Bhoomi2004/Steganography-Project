import cv2
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode

def encrypt_message(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode (for receiver to verify): ")

    # ✅ Load receiver's public key from file
    try:
        with open("public.pem", "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())
    except FileNotFoundError:
        print("Error: 'public.pem' not found. Make sure you have the receiver's public key.")
        return

    # ✅ Encrypt the message using the receiver's public key
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(msg.encode())  # Binary data

    # ✅ Base64 encode the encrypted message to embed safely
    encrypted_message_b64 = b64encode(encrypted_message).decode()

    # Create a dictionary mapping characters to ASCII values
    char_to_ascii = {chr(i): i for i in range(256)}

    # Check if image has enough space
    image_size = img.shape[0] * img.shape[1] * 3
    message_size = len(encrypted_message_b64) + 1  # +1 for null terminator
    if image_size < message_size:
        print(f"Encryption failed: {message_size} bytes needed but only {image_size} bytes available in image.")
        return

    # Embed the Base64 message into the image
    n, m, z = 0, 0, 0
    for char in encrypted_message_b64:
        img[n, m, z] = char_to_ascii[char]
        n += 1
        if n >= img.shape[0]:
            n = 0
            m += 1
        z = (z + 1) % 3

    # Add a null terminator to mark end of message
    img[n, m, z] = 0

    # Save output image
    cv2.imwrite(output_path, img)
    os.system(f"start {output_path}")
    print("Message successfully encrypted and embedded into image.")

    # Save the passcode
    with open("passcode.txt", "w") as f:
        f.write(password)

if __name__ == "__main__":
    image_path = r"C:\Users\bhoom\Downloads\Steganography-Project\mypic.png"
    output_path = "encryptedImage.png"
    encrypt_message(image_path, output_path)
