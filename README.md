Client & Server added, all that needs to be done is put a sleep function in the
client (1 line of code).

If you want to use the client and server for testing or something you can run
these on your location machine. 

run the server then run the client. when running on your local machine type
'python client.py 127.0.0.1' to connect to the server. Then in the client
type in the full path to the source file for the messages. Then the client will
send the messages to the server, and the server will print out the messages to
stdout & to '/tmp/messages.txt'. if there already is a messages.txt, it will 
overwrite it. There is no sleeping yet, since it would take forever to test, but 
it only takes 1 line of code to add it, so its not a big deal.

Simple man in the middle implementation added. look in the mitm.py file to see how to run
Just run this before you start doing any client server stuff.

Here is a link to the website where the nfqueue bindings for python is maintained. look in 
repository for examples (the documentation is very poor, its hard to find anything for this stuff,
even when looking for c libraries)

https://www.wzdftpd.net/redmine/projects/nfqueue-bindings

here is a little tutorial on iptables (its not too complicated)


https://help.ubuntu.com/community/IptablesHowTo
