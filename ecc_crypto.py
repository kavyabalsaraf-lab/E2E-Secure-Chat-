from cryptography.hazmat.primitives.asymmetric import ec            #ec → Elliptic Curve Cryptography operations ke liye.
from cryptography.hazmat.primitives import hashes                   
from cryptography.hazmat.primitives.kdf.hkdf import HKDF            #HKDF → Shared secret se secure key generate karne ke liye.
from cryptography.fernet import Fernet                              #Fernet → Symmetric encryption aur decryption ke liye.
import base64                                                       #base64 → Key ko Fernet-compatible format me convert karne ke liye.


# Generate ECC key pair
def generate_key_pair():
    private_key = ec.generate_private_key(ec.SECP256R1())           #standard 256-bit ECC curve hai jo high security provide karti hai.
    public_key = private_key.public_key()
    return private_key, public_key

# Generate shared secret
def generate_shared_secret(private_key, public_key):                #ECDH algorithm se common shared secret generate karte hain 
    return private_key.exchange(ec.ECDH(), public_key)              #bina secret ko network par bheje



# Create encryption key from shared secret
def derive_key(shared_secret):                                     #shared key ko 32-byte encryption key convert
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,                                                  #HKDF/SHA-256 ki help se shared secret ko encrypt key  convert
        salt=None,
        info=b'chat-app',
    ).derive(shared_secret)

    return base64.urlsafe_b64encode(derived_key)                   


# Encrypt message
def encrypt_message(message, key):                                 #Message bytes me convert and encrypt ho jata hai.
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())


# Decrypt message
def decrypt_message(ciphertext, key):                               #Receiver side par same secret key use karke encrypted message ko decrypt kiya jata hai.
    cipher = Fernet(key)
    return cipher.decrypt(ciphertext).decode()
