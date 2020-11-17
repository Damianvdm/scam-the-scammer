import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://videeosviralesma.tk//acesofacebook.php?api=1&lan=facebooknew&ht=2&counter0=5icgkwqeq8'

names = json.loads(open('namelist.json').read())

# for name in names:
#     name_extra = ''.join(random.choice(string.digits))

#     username = name.lower() + name_extra + '@gmail.com'
#     pass_len = random.randint(4,9)
#     password = ''.join(random.choice(chars) for i in range(pass_len))
#     payload={
#         'ua': '',
#         'state': '',
#         'username': 'USERNAME',
#         'email': username,
#         'pass': password,
#         'login': 'Log In',
#         'country': 'New Zealand',
#         'Country': 'New Zealand',
#         'pais': 'New Zealand',
#         'Pais': 'New Zealand '
#     }

#     r = requests.post(url, allow_redirects=False, data=payload)
#     print(r.headers)
#     print(f"sending username {username} and password {password}")
while True:
    rand_len = random.randint(1,4)
    if random.randint(0,1) == True:
            name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1,4)))
    else:
        name_extra = ''

    if random.randint(0,1) == True:
        rand_user = ''.join(random.choice(string.ascii_letters.lower()) for i in range(random.randint(1,4)))
    else:
        rand_user = ''

    username = names[random.randint(0,999)].lower() + rand_user + name_extra + '@gmail.com'


    password = ''.join(random.choice(chars) for i in range(random.randint(6,12)))
    payload={
        'ua': '',
        'state': '',
        'username': 'USERNAME',
        'email': username,
        'pass': password,
        'login': 'Log In',
        'country': 'New Zealand',
        'Country': 'New Zealand',
        'pais': 'New Zealand',
        'Pais': 'New Zealand '
    }

    r = requests.post(url, allow_redirects=False, data=payload)
    print(f"sending username {username} and password {password}")