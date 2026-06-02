import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

space = " "
layout = "=" * 44
print(layout)
print(f"{space * 11}HASHING DEMO (SHA256)")
print(layout)

message1 = "Hello Deloitte"
message2 = "Hello Deloitte!"

hash1 = hashlib.sha256(message1.encode()).hexdigest()
hash2 = hashlib.sha256(message2.encode()).hexdigest()

print(f"Input 1: {message1}")
print(f"Hash 1: {hash1}")
print()
print(f"Input 2: {message2}")
print(f"Hash 2: {hash2}")
print()
print(f"Same hash? {hash1 == hash2}")
print()
print(layout)
print(f"{space}SYMMETRIC ENCRYPTION DEMO (AES via Fernet)")
print(layout)

key = Fernet.generate_key()
cipher = Fernet(key)
original = "This is a secret message"

encrypted = cipher.encrypt(original.encode())
decrypted = cipher.decrypt(encrypted).decode()

print(f"Original:  {original}")
print(f"Key:       {key.decode()}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
print(f"Match? {original == decrypted}")

print()
print(layout)
print(f"{space * 6}ASYMMETRIC ENCRYPTION DEMO (RSA)")
print(layout)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = "Secret session key: abc123".encode()

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Original:  {message.decode()}")
print(f"Encrypted: {encrypted.hex()[:60]}...")
print(f"Decrypted: {decrypted.decode()}")
print(f"Match? {message == decrypted}")