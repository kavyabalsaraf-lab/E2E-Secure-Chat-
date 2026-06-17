# ECC Secure Chat

A real-time secure chat application built using **Flask**, **Socket.IO**, and **Elliptic Curve Cryptography (ECC)**.

## Features

* Real-time messaging using Socket.IO
* ECC key pair generation
* Shared secret generation using ECC Diffie-Hellman
* Symmetric key derivation from the shared secret
* Message encryption and decryption
* Live display of:

  * Public keys
  * Shared secret
  * Derived key
  * Encrypted message
  * Decrypted message

## Technologies Used

* Python
* Flask
* Flask-SocketIO
* HTML
* CSS
* JavaScript
* Cryptography library

## Project Structure

```text
e2e-chat-backend/
├── server.py
├── ecc_crypto.py
├── templates/
│   └── index.html
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ecc-secure-chat.git
```

2. Navigate to the project folder:

```bash
cd ecc-secure-chat
```

3. Install dependencies:

```bash
pip install flask flask-socketio cryptography
```

4. Run the application:

```bash
python server.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. Two ECC key pairs are generated.
2. Public keys are exchanged between users.
3. A shared secret is derived using ECC Diffie-Hellman.
4. The shared secret is converted into a symmetric key.
5. Messages are encrypted before transmission.
6. Messages are decrypted at the receiver side.

## Note

For educational purposes, the application displays cryptographic details in the user interface. In a production system, private keys and sensitive information should never be exposed.

## Author

Ansh Adkane
