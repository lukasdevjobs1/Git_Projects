"""Secure Password Generator with Encryption Support.

A command-line tool for generating cryptographically secure passwords
with optional encryption and file storage capabilities.
"""

import secrets
import string
import argparse
import os
from cryptography.fernet import Fernet

def generate_password(length=12, include_special_chars=False):
    """Generate a cryptographically secure random password.
    
    Args:
        length (int): Length of the password to generate. Defaults to 12.
        include_special_chars (bool): Whether to include special characters.
                                    Defaults to False.
    
    Returns:
        str: A randomly generated secure password.
    
    Example:
        >>> password = generate_password(16, True)
        >>> len(password)
        16
    """
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def save_password(password, filename='passwords.txt'):
    """Save an encrypted password to a file.
    
    Args:
        password (str): The password to encrypt and save.
        filename (str): The filename to save to. Defaults to 'passwords.txt'.
                       Path traversal attempts are sanitized.
    
    Returns:
        bytes: The encryption key used to encrypt the password.
    
    Note:
        Each password is encrypted with a unique key. Store the key safely
        as it's required to decrypt the password later.
    """
    key = Fernet.generate_key()
    f = Fernet(key)
    
    # Validate filename to prevent path traversal
    if os.path.sep in filename or '..' in filename:
        filename = 'passwords.txt'
    
    with open(filename, 'ab') as file:
        file.write(f.encrypt(password.encode()) + b'\n')
    return key

def main():
    """Main function to handle command-line interface and password generation.
    
    Parses command-line arguments and generates passwords based on user input.
    Optionally saves encrypted passwords to a file with encryption keys.
    """
    parser = argparse.ArgumentParser(description='Password Generator')
    parser.add_argument('--length', type=int, default=12, help='Length of the password')
    parser.add_argument('--include-special-chars', action='store_true', help='Include special characters')
    parser.add_argument('--save', action='store_true', help='Save the generated password to a file')
    
    args = parser.parse_args()
    password = generate_password(args.length, args.include_special_chars)
    print(f'Generated password: {password}')
    
    if args.save:
        key = save_password(password)
        print('Password saved to file (encrypted)')
        print(f'Encryption key (keep safe): {key.decode()}')

if __name__ == '__main__':
    main() 