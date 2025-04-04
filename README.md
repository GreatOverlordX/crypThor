# Password Management with crypThor

I have created this Python tool, so you can
store your passwords in `SHA256` hashing, 
encrypting thanks to a secret key,
and then decrypt your stored hashed-password.

Very easy to set, and use!

## Setting up with virtual environment

For this tool, you'd have to have the `cryptography` and `dotenv` library.

If you're using `xyz` linux distro, you might encounter
the error `Error: externally-managed-environment`.
You'd have to create an `venv` directory, for example:

```zsh

python3 -m venv ~/venv

```

Then you can proceed with:

```zsh
~/venv/bin/pip install cryptography

```

You repeat the same step with `dotevent`.

You might need to upgrade pip, and you can achieve this with:

```zsh
~/venv/bin/python3 -m pip install --upgrade pip

```

The cryptography library includes _Fernet Symmetric Encryption_.
This'll allow to store the values securely, and decrypt them in
memory when you need to use them.

_Symmetric encryption_ means we will have a secret key which we
can store in our environment variables, and use to decrypt stored values.

Create your `.env` file.
Then run an inline python command to generate the Fernet secret key.

```zsh
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"
```

The output after you run the command, will be your secret key.
The secret key might be in-between ('') like this: 'secret_key',
however, you'll store it in your `.env` file, without it.
Make sure to store it on your `.env` file as such:

```.env
SECRET_KEY=[THE SECRET KEY]
```

## Other methods for pip install on Arch

You can use other methods to install pip, and libraries needed
for any other projects you might have.
`https://linuxcraze.com/install-pip-arch-linux/` explains it better.
Read carefully, and use cautiously!

## Usage

Initially created not "scriptable", however, I tried my best to make it
"scriptable" so you could run the command `decrypt`, and specify
what file (where you have stored your hashed password) you want to decrypt.

### Encrypt password

```zsh
~/venv/bin/python3 crypthor.py
```

### Decrypt password

```zsh
~/venv/bin/python3 crypthor.py decrypt filename.txt
```

### Project & Mentions

This was a project aiming toward building a secure application for
storing passwords.

This project was inspired and tweaked around:
[https://dev.to/dpills/python-secure-password-management-hashing-and-encryption--1246]
