#!/usr/bin/env python3
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

def chk_eight(num):
    num1 = num % 8
    if not num1 : return True
    return False

#Main program starts here
BLOCK_SIZE = 8
original_text='Hello123Hello123Hello123'
print("Original text: {0}\n".format(original_text))

#Generate a random IV and print out the IV
myIV=get_random_bytes(8)
print("IV :",end=" ")
for b in myIV:
    print("{0:02x}".format(b),end=" ")
print()

#Convert UTF 8 encoded string to bytes. original_text stores 3 blocks of 8 bytes plain text
text_in_bytes = original_text.encode()

#Generate random key.  Total size of the key is 8 bytes, but only use 56-bit
print("Generating a 56-bit DES key ...")
key=get_random_bytes(8) 
print("The key is generated.\n")

#Print out the Plaintext (of the original_text) in bytes in Dec
print("Plaintext:")
ct=0
for b in text_in_bytes:
    print("{0:3d}".format(b),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")

#Create a DES cipher object with the specific key, Mode and IV
cipher = DES.new(key, DES.MODE_CBC,myIV)

#Now encrypt the text
cipher_text_bytes = cipher.encrypt(pad(text_in_bytes,BLOCK_SIZE))
print("Ciphertext:")
ct=0
for b in cipher_text_bytes:
    print("{0:3d}".format(b),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")
print("Ciphertext (Hex):")
ct=0
for b in cipher_text_bytes:
    print("{0:02x}".format(b),end="")
    ct=ct+1
    if chk_eight(ct): print()
print("\n")

"""************************************************
     *
     * Can you decrypt the message?
     *
     ************************************************/
"""
#Create a new DES cipher object with the same key and mode  
my_cipher = DES.new(key,DES.MODE_CBC,myIV)

#Now decrypt the text using your new cipher
decrypted_text_bytes = unpad(my_cipher.decrypt(cipher_text_bytes),BLOCK_SIZE)

#Print the message in UTF8 (normal readable way)
decrypted_text = decrypted_text_bytes.decode()
print("Decrypted text: {0}\n".format(decrypted_text))
