from flask import Flask, render_template, request                    #request → Identifies which client sent the message.
from flask_socketio import SocketIO, send                           #render_template → Loads the HTML page (index.html).
from ecc_crypto import *                                             #ecc_crypto → Contains ECC functions for key generation, encryption, and decryption.
                                                                    #Flask → Creates the web application.
                                                                    #SocketIO → Enables real-time 
                                                                    #send() → Sends messages to connected and get input
                                                                    
                                                                    

app = Flask(__name__)                                                # Flask server create kiya gaya hai.
app.config['SECRET_KEY'] = 'secret!'                                   #SECRET_KEY use kiya hai security ke liye


socketio = SocketIO(
    app,                                                              #SocketIO Flask ko real-time communication ki capability deta hai.
    cors_allowed_origins="*",
    async_mode='threading'
)

# Generate ECC key pairs
private1, public1 = generate_key_pair()
private2, public2 = generate_key_pair()

# Generate shared secret and derived key
secret = generate_shared_secret(private1, public2)                      #shared secret key ko secure 
key = derive_key(secret)


@app.route('/')                                                         #http://127.0.0.1:5000 open then Flask 
def home():
    return render_template("index.html")


@socketio.on('message')                                                 # message bhejta hai then function 
def handle_message(msg):


    # Encrypt message
    encrypted = encrypt_message(msg, key)                               #convert message in encrypt me
    print("\n==============================")
    print("Original Message :", msg)
    print("Encrypted Message:", encrypted)

    # Decrypt message
    decrypted = decrypt_message(encrypted, key)
    print("Decrypted Message:", decrypted)

    print("Shared Secret:", secret)
    print("Derived Key:", key)
    print("==============================\n")

    # Send everything to webpage
    send({                                                             #request.sid sender ka unique ID hota hai
        "sender": request.sid,
        "message": decrypted,

        # ECC Details
        "public_key_1": str(public1),
        "public_key_2": str(public2),
        "shared_secret": str(secret),
        "key": str(key),

        # Encryption Details
        "encrypted": str(encrypted),
        "decrypted": str(decrypted)

    }, broadcast=True)                                                #check the connect and msg send

if __name__ == '__main__':
    socketio.run(
        app,
        host='0.0.0.0',
        port=5000,
        debug=True
    )