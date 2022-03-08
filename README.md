<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Logo" width="120"/> 

# Python-chatbots

*This was an individual portfolio assignment in the course "DATA2410 - Networking and cloud computing" at OsloMet.* <br />
*We were tasked with creating a Python chat room with bots and a host that could talk to each other through a TCP socket.* <br />

- - - 
## How to run:
1. Start by running the server.py in a terminal window with the port as the argument.

2. The server will then go in listen-mode and wait for connections and let us know if somebody connects.
3. Open up at least one terminal for a bot, or as many as you see fit. Keep in mind that there are only 3 bots to choose from: Ash, Misty and Brock
4. One must also open one terminal for the host-client, aka. the user. More hosts are allowed, but only one is recommended for optimized use.
5. Start client.py in the new terminals with 3 arguments: IP-address, port and name. The name decides whether you're a bot or a host.
6. The chatroom should now be intact. The user can write whatever he/she desires, and the bot(s) will respond accordingly.
7. The bots will have seperate responses for a set of given verbs. 
8. To disconnect, one can simply close the terminal windows. The host can also write "SHUTDOWN" to disconnect all clients and stop the server. The server will notify the clients    when somebody disconnects.
- - - 

  - **server.py: Hosts the chat room.**
    - Requires port number as argument:
      ```console
      python3 server.py 4242
      ```
    - Type **server.py -h** for more info:
      ```console
      usage: server.py [-h] port

      Start the chat server and listen for incoming connections. Example: server.py 4242

      positional arguments:
      port        The port the server is running on (Integers only).

      optional arguments:
      -h, --help  show this help message and exit

      ```
  - **client.py: Bots and host**
    - Requires IP address/hostname, port number and client name as arguments. The client name can be anything, but will become a bot if a bot name is given.
      ```console
      python3 client.py localhost 4242 Steven
      ```
    - Type **client.py -h** for more info:
      ```console
      usage: client.py [-h] IP port name

      Connect to the chat room. Example: client.py localhost 4242 Steven

      positional arguments:
      IP          IP address of the server the client is connecting to.
      port        The port the client is connecting to (Integers only).
      name        The name of the client. Connect as a host or a bot(Ash, Misty or Brock)

      optional arguments:
      -h, --help  show this help message and exit
      ```
