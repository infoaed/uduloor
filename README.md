# uduloor
Identity pseudonymizer for conducting transparent and auditable secret voting on Internet

![Screenshot of a test run](uduloor-screenshot.png)

## How to use?

* Download the Python source.
* Add list of e-mails into source.
* Add list of words to choose pseudonyms from.
* Add configuration for e-mail server.
* Run the program on neutral computer with the oversight of observers, interested parties etc.
* Conduct voting on any reasonably neutral and independent collaborative text editor on Internet.
* Maybe require each voter to cast a vote as well as abstention.
* Maybe require each voter to check if the pseudonymous vote is cast correctly. 
* Publicly tally the votes cast in text editor.

This is for use in annual meetings of NGOs etc where you can presume certain amount of trust among participants, that is no false claims to annul the vote and sophisticated technical attacks on infrastructure like e-mail servers, server logs etc. The principle of the process is to make it as transparent and auditable as possible with simple means available to every user of Internet.

## TODO

* [x] Convert it into a [simple web service](https://github.com/infoaed/pseudovote) for testing.
* [ ] Design it to be recommended ballot delivery script for the web service, optional use of API.
* [ ] Resending bouncing e-mails to another address?
* [ ] Other delivery options besides e-mail.
* [ ] PGP encryption and signatures in parts of the process.
* [ ] Maybe add config files and some options for messages.
* [ ] Distributing pseudonyms for multiple rounds of voting.
* [ ] Countdown for publishing list of cryptonyms.
