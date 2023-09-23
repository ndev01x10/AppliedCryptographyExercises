#!/usr/bin/env python3
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

#Extra function to be called by main program
#If num = 8,16,32 return true, false otherwise
def chk_eight(num):
    num1 = num % 8 #In python, 0 is False, num1 is 0 when num=8 or 16 or 32..
    if not num1:
        return True
    else:
        return False

#Start of main program
BLOCK_SIZE = 16 #AES data block size 128 bits (16 bytes) "state"
keysize = 16 #16 bytes -> 128 bits. 32 bytes -> 256 bits
original_text='11111111111111111111111111111111111111111111111111' #Plain text
text_in_bytes = original_text.encode() #Convert UTF 8 encoded string to bytes
print("Generating a " + str(keysize*8) +  "-bits AES key ...") #16*8=>128 bits

key=get_random_bytes(keysize) #Generate randmom bytes array
print("The key is generated.")
print("AES key :",end=" ")

#--------> Your code here for myAesEcb1.py <-----------
#The "key" object is an array, use a for..loop to print
#Use end=" " in the print to print a space
#Use format(b, '02x') to print byte in hex string as 2 places, b is a variable 

for b in key:
    print(format(b,'02x'),end=" ")

#Print plaintext 50 '1' in base 10 - Decimal using a for loop
print("\n\n\nPlaintext: 50 '1' in base 10 - Decimal")
ct=0
for b in text_in_bytes:
    print(format(b, '3d'),end=" ")
    ct=ct+1
    if chk_eight(ct): print() #Print a new line

print("\n") #This print a new line

cipher = AES.new(key, AES.MODE_ECB) #New AES cipher using key generated
cipher_text_bytes = cipher.encrypt(pad(text_in_bytes,BLOCK_SIZE)) #Encrypt data

#Data is bytes (text_in_bytes), not strings
#Print Ciphertext in base 10 - Decimal using a for loop
print("\nCiphertext (in base 10 - Decimal):")
ct=0
for b in cipher_text_bytes:
    print(format(b, '3d'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
    
print("\n")

#Print Ciphertext in base 16 - Hex using a for loop
print("Ciphertext (in base 16 - Hex):")
ct=0
for b in cipher_text_bytes:
    print(format(b, '02x'),end=" ")
    ct=ct+1
    if chk_eight(ct): print()
    
print("\n")

#*********Decrypt message here *********
#Create a new AES cipher object with the same key and mode
my_cipher = AES.new(key,AES.MODE_ECB)

#Now decrypt the text using your new cipher
decrypted_text_bytes = unpad(my_cipher.decrypt(cipher_text_bytes),BLOCK_SIZE)

#Print the message in UTF8 (normal readable way)
decrypted_text = decrypted_text_bytes.decode()
print("Decrypted text: " ,  decrypted_text)
