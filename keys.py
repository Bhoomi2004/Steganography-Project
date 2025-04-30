import rsa

def generate_keys():
    public_key, private_key = rsa.newkeys(2048)  # You can increase size if needed

    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key.save_pkcs1())

    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key.save_pkcs1())

    print("RSA Key Pair generated successfully!")

if __name__ == "__main__":
    generate_keys()
