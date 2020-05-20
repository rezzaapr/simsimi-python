import requests, json
import os, sys

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
banner = a+"""
                        _________
                        [       ] Simsimi Bot
                        | 0   0 | by : Simple Python Programming
                      //|   °   |\\
                     $  [__###__]  $
                        | |   | |
                        ---   ---
 """

print(banner)
while True:
    us = input(b+'# Masukan Pesan : ')
    url = 'https://wsapi.simsimi.com/190410/talk/'
    body = {
      'utext': us, 
      'lang': 'id',
      'country': ['ID'],
      'atext_bad_prob_max': '0.7'
      }
    headers = {
       'content-type': 'application/json', 
       'x-api-key': 'YZ-HmRMvULkmLzlFw5jXt9vVdN2ZVmsrQDeLTT3C'
     }
    r = requests.post(url, data=json.dumps(body), headers=headers)
    js = r.json()['atext']
    print(a+'# Simi : '+ js)

