import os
import boto3
import botocore.exceptions
import hmac
import hashlib
import base64

def get_secret_hash(clientid, clientsecret, username):
    msg = username + clientid
    dig = hmac.new(str(clientsecret).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2