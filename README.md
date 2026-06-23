# 🔐 Encryption and Decryption Program

## Overview

This is a simple Python-based Encryption and Decryption program that uses a Caesar Cipher-style shifting technique. Users can encrypt text, decrypt text, or perform both operations in a single execution. The program supports uppercase letters, lowercase letters, digits, spaces, and special characters.

## Features

- Encrypt text using a custom shift value
- Decrypt encrypted text using the same shift value
- Perform encryption and decryption together
- Supports:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters and spaces
- Input validation for shift values

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/encryption-decryption-program.git
```

2. Navigate to the project folder:

```bash
cd encryption-decryption-program
```

3. Run the program:

```bash
python encryption_decryption.py
```

## Usage

When the program starts, you will see:

```
Type 0 to Perform Encryption
Type 1 to Perform Decryption
Type 2 to Perform Both
```

### Encryption Example

Input:

```
Choice: 0
Text: Hello123
Shift: 3
```

Output:

```
Khoor456
```

### Decryption Example

Input:

```
Choice: 1
Text: Khoor456
Shift: 3
```

Output:

```
Hello123
```

## How It Works

### Encryption

- Letters are shifted forward by the specified number.
- Numbers are shifted cyclically using modulo 10.
- Special characters remain unchanged.

### Decryption

- Letters are shifted backward by the specified number.
- Numbers are shifted backward cyclically using modulo 10.
- Special characters remain unchanged.

## Project Structure

```
encryption-decryption-program/
│
├── encryption_decryption.py
└── README.md
```

## Limitations

- This project uses a basic Caesar Cipher technique.
- It is intended for educational purposes and not for securing sensitive information.

## Future Enhancements

- GUI version using Tkinter
- File encryption and decryption
- Password protection
- Advanced encryption algorithms

## Author

**Nagarajan M**

Python Encryption and Decryption Project
