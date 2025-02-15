# Steganography-Project
# Secure Data Hiding in image using Steganography

A Python-based steganography project that hides a secret message and passcode in an image using Least-Significant-Bit (LSB) encoding, ensuring secure and undetectable data concealment.

## Overview

This project implements robust LSB steganography to securely embed a secret message along with a passcode into an image. It includes two Python scripts with a user-friendly GUI built using Tkinter for seamless encryption and decryption.

## Features

- **Encryption:**  
  Embeds a secret message and passcode into `mypic.png` and saves the result as `encrypted.png`.

- **Decryption:**  
  Retrieves the hidden message from `encrypted.png` when the correct passcode is provided.

- **User-Friendly GUI:**  
  Easy-to-use interfaces for both encryption and decryption processes.

- **Robust Data Storage:**  
  Uses a header to store the lengths of the passcode and message for accurate extraction.

## Requirements

- Python 3.x  
- OpenCV  
- os  
- string

## Installation

1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install opencv-python numpy
3. Place an image mypic.png in project directory
