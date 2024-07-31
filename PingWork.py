import os
import requests
def ping(hostname):
    param = '-n' if os.sys.platform().lower()=='win32' else '-c'
    PINGresponse = os.system(f"ping {param} 1 {hostname}")
    return PINGresponse
def POST(version,username,password,url):
    
    # Replace these with your actual username and password

    data = {
        'user': username,
        'password': password,
        'version': version
    }

    response = requests.post(url, data=data)

    return response.text
def Parse(session_string):

    session_id = session_string.split(':')[3]

    return session_id
