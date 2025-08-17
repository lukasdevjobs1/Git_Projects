# 🔐 Secure Password Generator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Security](https://img.shields.io/badge/Security-Cryptographically%20Secure-green.svg)](https://docs.python.org/3/library/secrets.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **A command-line tool for generating cryptographically secure passwords with optional encryption and file storage capabilities.**

## 🚀 Features

- **🔒 Cryptographically Secure**: Uses Python's `secrets` module for true randomness
- **⚙️ Customizable Length**: Generate passwords from 1 to any length
- **🎯 Special Characters**: Optional inclusion of symbols and punctuation
- **🔐 Encryption Support**: Save passwords encrypted with Fernet symmetric encryption
- **🛡️ Security Hardened**: Path traversal protection and input validation
- **📝 Well Documented**: Comprehensive docstrings and type hints
- **🖥️ CLI Interface**: Easy-to-use command-line interface

## 📋 Requirements

```bash
Python 3.8+
cryptography>=3.0.0
```

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/lukasdevjobs1/Git_projects.git
cd Git_projects
```

2. **Install dependencies**:
```bash
pip install cryptography
```

3. **Run the generator**:
```bash
python passwords_generator.py
```

## 💻 Usage

### Basic Usage

```bash
# Generate a 12-character password (default)
python passwords_generator.py

# Generate a 16-character password
python passwords_generator.py --length 16

# Generate password with special characters
python passwords_generator.py --include-special-chars

# Generate and save encrypted password
python passwords_generator.py --save
```

### Advanced Examples

```bash
# Strong 20-character password with symbols, saved encrypted
python passwords_generator.py --length 20 --include-special-chars --save

# Quick 8-character password for simple use
python passwords_generator.py --length 8

# Help and all options
python passwords_generator.py --help
```

## 📖 Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--length` | Length of the password | 12 |
| `--include-special-chars` | Include special characters (!@#$%^&*) | False |
| `--save` | Save encrypted password to file | False |
| `--help` | Show help message | - |

## 🔐 Security Features

### Cryptographic Security
- Uses `secrets.choice()` for cryptographically secure random generation
- Implements Fernet symmetric encryption for password storage
- Each saved password gets a unique encryption key

### Input Validation
- Path traversal protection prevents malicious file paths
- Filename sanitization ensures safe file operations
- Secure defaults for all parameters

### Best Practices
- No password logging or console history exposure
- Encryption keys displayed only when saving
- Binary file operations for encrypted data

## 📁 File Structure

```
passwords_generator.py          # Main application
passwords.txt                   # Encrypted passwords (created when --save used)
README_passwords_generator.md   # This documentation
```

## 🔧 Code Structure

### Functions

#### `generate_password(length=12, include_special_chars=False)`
Generates a cryptographically secure random password.

**Parameters:**
- `length` (int): Password length (default: 12)
- `include_special_chars` (bool): Include symbols (default: False)

**Returns:** `str` - Generated password

#### `save_password(password, filename='passwords.txt')`
Encrypts and saves password to file with unique key.

**Parameters:**
- `password` (str): Password to encrypt
- `filename` (str): Target file (default: 'passwords.txt')

**Returns:** `bytes` - Encryption key

#### `main()`
Handles command-line interface and orchestrates password generation.

## 📊 Example Output

```bash
$ python passwords_generator.py --length 16 --include-special-chars --save
Generated password: rRCP9y@1YdzfaIJ-
Password saved to file (encrypted)
Encryption key (keep safe): 9ekmF0-kxZwkBjIXqL3Me4jEIuDnFoMOsW68BH7OBt4=
```

## 🔄 Recent Updates

### Version 2.0 - Security & Functionality Overhaul
- ✅ **Fixed Critical Bugs**: Corrected typos causing NameError
- ✅ **Security Hardening**: Added path traversal protection
- ✅ **Performance Optimization**: Single `parse_args()` call
- ✅ **Functionality Implementation**: `--save` argument now works
- ✅ **Code Quality**: Added comprehensive docstrings
- ✅ **Structure Improvement**: Fixed indentation and module structure
- ✅ **Import Optimization**: Removed unnecessary imports

### Security Improvements
- 🛡️ **CWE-22 Prevention**: Path traversal vulnerability fixed
- 🔒 **CWE-200 Mitigation**: Reduced sensitive information exposure
- 🔐 **Encryption Enhancement**: Proper binary file handling

## 🧪 Testing

The application has been thoroughly tested with:

```bash
# Test basic functionality
python passwords_generator.py

# Test with all options
python passwords_generator.py --length 20 --include-special-chars --save

# Test help system
python passwords_generator.py --help
```

**Test Results:** ✅ All tests passing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [To-Do List Application](./to_do_list.py) - Task management with Streamlit
- [Hangman Game](./hangman_game.py) - Word guessing game with API integration
- [Unit Converter](./unit_converter.py) - Temperature and distance converter

## 📞 Support

For support, email luk.devjobs@gmail.com or open an issue on GitHub.

---

⭐ **Star this repository if you find it helpful!**

*Part of the [Daily Coding Projects](./README.md) portfolio*
