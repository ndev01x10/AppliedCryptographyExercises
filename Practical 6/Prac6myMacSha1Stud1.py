#!/usr/bin/env python3
#IT8084 - ACG Practical - myMacSha1Stud1.py
# take in a file name or an input phrase 
from Cryptodome.Random import get_random_bytes
import hmac
import base64
import sys
# main program starts here
argc = len(sys.argv)
content=""
if argc > 2:
    print("Usage : {0} [file name]".format(sys.argv[0]))
    exit(-1)
elif argc == 2:
    try:
     with open(sys.argv[1]) as f:
        content=f.read()
    except:
        print("Invalid file argument!")
        exit(-1)
else:
    content=input("Your input please =>")
try:    
    print("A simple Program on HmacSHA1")
    keysize=hmac.HMAC.blocksize
    print("key size {0}".format(keysize))
    # insert your code here to generate a random key
    key=get_random_bytes(keysize)
    # display the key in base64 encoded bytes in UTF8 format
    print("key : {0}".format(base64.b64encode(key).decode()))
    # insert your code here to instantiate a sha1 hmac object, hma
    hma = hmac.new(key,digestmod="sha1")
    # insert your code here to display the HMAC digest in base64 encoded bytes in UTF8 format
    hma.update(content.encode())
    print("MAC: {0}".format(base64.b64encode(hma.digest()).decode()))
except:
    print("Invalid file argument!")
