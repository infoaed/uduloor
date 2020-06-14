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

Sinu pseudonüüm hääletamisel on:

* %s

Hääletus toimub aadressil

* https://etherpad.wikimedia.org/p/wmee-juhatus

Siiralt "jne"
Uduloor
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
hepatica
trollius
ranunculus
caltha
rosa
trifolium
melampyrum
syringa
solanum
ligularia
curcuma
antirrhinum
"""

pseudo_id = namedtuple('pseudo_id', ['pseudonym', 'code', 'cryptonym'])

voter_list = voters_in_text.strip().splitlines()
word_list = unique_words.strip().splitlines()

random_words = random.sample(word_list, len(voter_list))
random_keys = random.sample(range(100, 999), len(voter_list))

print("There is %d voters in upcoming election:\n" % len(voter_list))

for voter in voter_list:
  print(voter)

random.shuffle(voter_list)

print()

print("Distributing pseudonyms...\n")

pseudo = []

for i in range(len(voter_list)):
  current = pseudo_id(random_words[i], str(random_keys[i]), random_words[i] + str(random_keys[i]))
  pseudo.append(current)

i = -1

try:
    
  #server = smtplib.SMTP_SSL(url, port, context=ssl.create_default_context())
  #server.login(username, password)
  
  for i in range(len(voter_list)):

    receiver = voter_list[i].split()[0]
    message = message_template % (receiver, pseudo[i].cryptonym)
    
    print("*", pseudo[i].pseudonym)
    
    #server.sendmail(sender, receiver, message.encode("utf8"))
    
    time.sleep(1)
    
  #server.quit()
  
  print()
  
  print("Delivered %d pseudonyms." % (i+1))
  
except Exception as e:

  print("Delivered %d pseudonyms." % (i+1))
  
  print("ERROR:", e)

print()

print("Write 'end' to close voting and publish audit information.")

print()

while(input("> ") != "end"):
  pass

print()
print("Cryptonyms:")

print()

for i in range(len(voter_list)):
    print("*", pseudo[i].cryptonym)
