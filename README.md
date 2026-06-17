# ECC Secure Chat

A real-time secure chat application developed using **Flask**, **Socket.IO**, and **Elliptic Curve Cryptography (ECC)** to demonstrate secure end-to-end communication.

## Features

* Real-time messaging using Socket.IO
* ECC public and private key generation
* Shared secret generation using ECC Diffie-Hellman
* Symmetric key derivation from the shared secret
* Message encryption and decryption
* Interactive web interface
* Optional security panel displaying:

  * Public keys
  * Shared secret
  * Derived key
  * Encrypted message
  * Decrypted message

## Technologies Used

* Python
* Flask
* Flask-SocketIO
* Cryptography Library
* HTML
* CSS
* JavaScript

## Project Structure

```text
E2E Chat/
├── server.py
├── ecc_crypto.py
├── templates/
│   └── index.html
└── README.md
```

## Installation

1. Install Python 3.10 or later.

2. Install the required dependencies:

```bash
pip install flask flask-socketio cryptography
```

3. Navigate to the project directory:

```bash
cd "D:\kavya\E2E Chat"
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

1. ECC key pairs are generated for communication participants.
2. Public keys are exchanged securely.
3. A shared secret is generated using ECC Diffie-Hellman.
4. The shared secret is converted into a symmetric encryption key.
5. Messages are encrypted before transmission.
6. Received messages are decrypted using the derived key.

## Security Note

This project displays cryptographic information in the user interface for educational and demonstration purposes. In a production environment, private keys and sensitive cryptographic data must never be exposed.

## Author

Kavya Balsaraf
