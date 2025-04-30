# **Steganography-Project**  
## **Secure Data Hiding in Image Using Steganography with LSB Encoding**

A Python-based steganography tool that securely hides a secret message and passcode in an image using **Least-Significant-Bit (LSB) encoding**, ensuring secure and undetectable data concealment.

---

## 🔐 **Overview**

This project uses **LSB steganography** combined with **RSA encryption** and a **user-defined passcode** to embed sensitive messages into images. The message is first encrypted using RSA encryption and then embedded into the image using the Least-Significant-Bit (LSB) encoding technique. The project offers high security by requiring both the **private key** and the **passcode** to retrieve the hidden message.

---

## 🚀 **Features**

- **LSB Encoding:**  
  The secret message is hidden in the least significant bits of the image's RGB values, making the message undetectable to the human eye.

- **RSA Encryption:**  
  The message is encrypted using **RSA (2048-bit)** before embedding, ensuring strong cryptographic security.

- **Passcode Protection:**  
  An additional layer of access control using a user-supplied passcode.

- **Custom Key Management:**  
  RSA keys are saved as `private.pem` and `public.pem`. Users can choose to provide the private key file or paste the key during decryption.

- **Error Handling:**  
  Informative messages and checks ensure smooth usage and help prevent incorrect decryption or overwriting.

---

## 📦 **Requirements**

- Python 3.x  
- OpenCV (`cv2`)  
- PyCryptodome

Install dependencies using:
```bash
pip install opencv-python pycryptodome
```

---

## 📁 **Files**

- `encrypt.py` — Embeds an RSA-encrypted secret message into the image using LSB encoding.
- `decrypt.py` — Extracts and decrypts the message using the private RSA key and passcode.
- `keys.py` — Generates the `private.pem` and `public.pem` RSA keys required for encryption and decryption.
- `private.pem` — Automatically generated private RSA key (keep secure).
- `public.pem` — Automatically generated public RSA key.
- `passcode.txt` — Stores the encryption passcode securely (excluded from Git using `.gitignore`).
- `encryptedImage.png` — The output image containing the hidden encrypted message.

---

## 🛠️ **Setup Instructions**

Follow these steps to set up the project and use the steganography scripts:

### Step 1: Clone the Repository
Clone the repository to your local machine:
```bash
git clone <your-repository-url>
```

### Step 2: Install Dependencies
Make sure you have Python 3.x installed, then install the necessary dependencies:
```bash
pip install opencv-python pycryptodome
```

### Step 3: Generate Keys
Before you can use the encryption and decryption scripts, you must generate the public and private RSA keys. Run the `keys.py` script to generate these keys:
```bash
python keys.py
```
This will generate:
- `private.pem` (private key for decryption)
- `public.pem` (public key for encryption)

Make sure to securely store the private key (`private.pem`).

### Step 4: Place Your Image
Place the image file (e.g., `mypic.png`) in the project directory.

---

## 🖼️ **Usage**

### 🔐 **Encryption**

1. Run the encryption script:
    ```bash
    python encrypt.py
    ```
2. **Input:**
   - Enter your secret message.
   - Enter a passcode for encryption.
   
3. The script will generate:
   - `private.pem` (private key for decryption)
   - `public.pem` (public key for encryption)
   - `passcode.txt` (the passcode used for encryption)
   - `encryptedImage.png` (the image with the hidden encrypted message)

### 🔓 **Decryption**

1. Run the decryption script:
    ```bash
    python decrypt.py
    ```
2. **Input:**
   - Enter the passcode for decryption (must match the original passcode).
   - Provide the private key file (`private.pem`) or paste the private key as text.

3. The script will print the decrypted message to the console.

---

## 🚫 **Sensitive Files**

The following files are ignored using `.gitignore` for security:
```
private.pem
public.pem
passcode.txt
encryptedImage.png
```

---
