
import hashlib

p = 61
q = 53
n = p * q
e = 17
d = 2753

def hash_message(message):
    sha = hashlib.sha256(message.encode()).hexdigest()
    h = int(sha, 16) % n
    return h

def sign(message):
    h = hash_message(message)
    signature = pow(h, d, n)
    return signature, h

def verify(message, signature):
    h = hash_message(message)
    h_decrypted = pow(signature, e, n)
    if h == h_decrypted:
        return True
    else:
        return False

msg = "Transfer $1000 to Mark"
sig, h_val = sign(msg)

print("Message:", msg)
print("Hash:", h_val)
print("Signature:", sig)
print("Public Key (e,n):", e, ",", n)
print("Private Key (d,n):", d, ",", n)
print("Verification Original:", verify(msg, sig))

fake_msg = "Transfer $1000 to Oscar"
print("Verification Fake:", verify(fake_msg, sig))