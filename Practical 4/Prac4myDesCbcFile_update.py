#!/usr/bin/env python3
from base64 import b64encode,b64decode 
from Cryptodome.Cipher import DES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad
 
#Main program starts here
BLOCK_SIZE = 8
print("Generating a 56-bit DES key ...")

#Generating a valid random DES Key and store it to key
key=get_random_bytes(8)
print("The key is generated.\n")

#Generating a valid random or static Initial Vector (IV) value
myIV=get_random_bytes(8)

#Create a DES cipher object with the specific key and CBC Mode and IV
cipher = DES.new(key, DES.MODE_CBC,myIV)

#Prepare the outfile, named 'encrypted.txt'
outf = open('encrypted.txt','w')

#Prompt for the file name
infname = input("Your file name =>")

#Now encrypt the text file and write the output to encrypted.txt
print()
print("--Original content--")
print()
with open(infname) as f:
    for ln in f:
        print(ln.strip())
        #Print()
        #Encrypt the current line and append the encrypted content to the encrypt.txt        
        encrypted_bytes = cipher.encrypt(pad(ln.strip().encode(),BLOCK_SIZE))
        enc_line = b64encode(encrypted_bytes).decode()
        print(enc_line,file=outf)
f.close()
outf.close()
"""************************************************
     *
     * Can you decrypt the file ?
     *
     ************************************************/
"""
#Create a new DES cipher object with the same key and cbc mode and IV  
cipher2 = DES.new(key, DES.MODE_CBC,myIV)
print()
print("--encrypted content--")
print()

#Open the encrypted.txt for reading
#Display the content of encrypted.txt to the terminal
with open("encrypted.txt","r") as f:
    for ln in f:
        print(ln.strip())
f.close() #Close then reopen the "encrypted.txt" for reading

print()
print("--Decrypted Content--")
print()

#Now decrypt the content of encrypted.txt  and display the output to the terminal
with open("encrypted.txt","r") as f:
    for ln in f:
        encrypted_bytes = b64decode(ln.strip().encode())
        decrypted_bytes = unpad(cipher2.decrypt(encrypted_bytes),BLOCK_SIZE)
        print(decrypted_bytes.decode())
f.close() #Finally close the file
 
