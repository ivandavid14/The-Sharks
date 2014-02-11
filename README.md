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
