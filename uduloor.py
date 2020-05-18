#!/usr/bin/python3

# https://myaccount.google.com/lesssecureapps

import smtplib, ssl
import time, random

from collections import namedtuple

url = "smtp.gmail.com"
port = 465
username = "boamaod"
password = "secret123"

sender = "pseudo@infoaed.ee"

message_template = """From: Uduloor <pseudo@infoaed.ee>
To: %s
Subject: Uduloor

Sinu pseudonüüm hääletamisel on %s.
"""

voters_in_text = """tramm@infoaed.ee
boamaod@gmail.com
tramm@p6drad-teel.net
tramm@wikimedia.ee
"""

unique_words = """narcissus
taraxacum
tulipa
rhododendron
papaver
mimosa
iris
asparagus
anemone
alcea
"""

Pseudonym = namedtuple('Pseudonym', ['public', 'private'])

voter_list = voters_in_text.strip().splitlines()
word_list = unique_words.strip().splitlines()

random_words = random.sample(word_list, len(voter_list))
random_keys = random.sample(range(100, 999), len(voter_list))

print("There is %d voters in upcoming election:\n" % len(voter_list))

for voter in voter_list:
  print(voter)

print()

print("Distributing pseudonyms...\n")

i = -1

try:
    
  server = smtplib.SMTP_SSL(url, port, context=ssl.create_default_context())
  server.login(username, password)
  
  for i in range(len(voter_list)):

    pseudonym = Pseudonym(random_words[i], random_words[i] + str(random_keys[i]))
    receiver = voter_list[i].split()[0]
    message = message_template % (receiver, pseudonym.private)
    
    print("*", pseudonym.public)
    #print(message)
    #print("===")
    
    server.sendmail(sender, receiver, message.encode("utf8"))
    
    time.sleep(1)
    
  server.quit()
  
  print()
  
  print("Delivered %d pseudonyms." % (i+1))
  
except Exception as e:

  print("Delivered %d pseudonyms." % (i+1))
  
  print("ERROR:", e)
