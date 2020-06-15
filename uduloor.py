#!/usr/bin/python3

# https://myaccount.google.com/lesssecureapps

import smtplib, ssl
import time, random

from collections import namedtuple

sender = "pseudo@infoaed.ee"
bulletin = "https://etherpad.wikimedia.org/p/psephos-demosia"

message_template = """From: Uduloor <%s>
To: %s
Subject: Your pseudonym for voting at the upcoming election

Your pseudonym for voting at the upcoming election is:

* %s

Voting takes place at:

* %s

Guidelines in nutshell:

* To cast your vote, please write down your pseudonym followed by your choice at the election.
* Make sure you write this information on a separate line at the bulletin board to avoid any confusion.
* To preserve your anonymity in this secret election you *should not* log in to the bulletin board.
* For extra caution you can use the private mode of your web browser or even special anonymity preserving browser.
* Before voting is closed, please make sure your vote is still correctly displayed at the bulletin board.
* After voting is closed you (or actually anyone) can tally the votes to make sure everything was done correctly.

Happy voting!

Sincereley "etc"
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

code_range = range(100, 999)

DRY_RUN = True

url = "smtp.gmail.com"
port = 465
username = "boamaod"
password = "secret123"

pseudo_id = namedtuple('pseudo_id', ['pseudonym', 'code', 'cryptonym'])

voter_list = voters_in_text.strip().splitlines()
word_list = unique_words.strip().splitlines()

random_words = random.sample(word_list, len(voter_list))
random_keys = random.sample(code_range, len(voter_list))

print("There are %d voters in upcoming election:\n" % len(voter_list))

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
  
  if not DRY_RUN:  
    server = smtplib.SMTP_SSL(url, port, context=ssl.create_default_context())
    server.login(username, password)
  
  for i in range(len(voter_list)):

    receiver = voter_list[i].split()[0]
    message = message_template % (sender, receiver, pseudo[i].cryptonym, bulletin)
    
    print("*", pseudo[i].pseudonym)
    
    if not DRY_RUN:
      server.sendmail(sender, receiver, message.encode("utf8"))
    
    time.sleep(1)
    
  if not DRY_RUN:
    server.quit()
  
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

print()

print("Thanks for taking digital democracy seriously!")
