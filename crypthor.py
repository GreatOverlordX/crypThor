# Secure Password Manager - In SHA-256 
# crypThor - crypthor.py

import os
import sys

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY") # Retrieve the secret key from .env variable "SECRET_KEY"
assert SECRET_KEY  # Ensures secret key is not empty
FERNET = Fernet(SECRET_KEY) # Initialises the Fernet Encryption object with the secret key


# Check if the script is being run with the "decrypt" argument
if len(sys.argv) > 1 and sys.argv[1] == "decrypt":
    if len(sys.argv) > 2:
        file_name = sys.argv[2]
    # If "decrypt" argument is provided -> read the stored encrypted password from "file.txt"
        try:
            with open(file_name) as f:
                stored_password = f.read()
        except FileNotFoundError:
            print(f"File {file_name} not found :( ...")
            sys.exit(1)

        try:
    # Decrypt the stored password using the Fernet object
            stored_dec_password = FERNET.decrypt(stored_password.encode()).decode()
        except Exception as e:
            print(f"Error decrypting password! {e}")
            sys.exit(1)
        # Print the decrypted password
        print(f"Decrypted Password: {stored_dec_password}")
    else:
        print("Please provide a file name to decrypt.")
        sys.exit(1)
else:
    # If no "decrypt" argument is provided, prompt the user for a new password
    new_password = input("New Password: ")
    new_enc_password = FERNET.encrypt(new_password.encode()).decode()       # Encryption of new password using the Fernet object

    file_name = input("What file name you want to save the encrypted password into?: ")
    # If the filename does not have an extension, adds ".txt" by default
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Write the encrypted password to passw.txt
    with open(file_name, "w") as f:
        f.write(new_enc_password)

#    print(f"Encrypted Password Stored! -> {new_enc_password}")
    print(f"Encrypted Password Stored in {file_name}: {new_enc_password}")
