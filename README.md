<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Logo" width="120"/>

# Python-chatbots

This was an individual portfolio assignment in the course "DATA2410 - Networking and cloud computing" at OsloMet. <br />
We were tasked with creating a Python chat room with bots and a host that could talk to each other through a TCP socket.

## How to run:
This project contains two python files:
  - **server.py: Hosts the chat room.**
    - Requires port number as argument:
      ```console
      python3 server.py 4242
      ```
    - Type **server.py --h** for more info:
      ```console
      usage: server.py [-h] port

      Start the chat server and listen for incoming connections. Example: server.py 4242

      positional arguments:
      port        The port the server is running on (Integers only).

      optional arguments:
      -h, --help  show this help message and exit

      ```
  - **client.py: Bots and host**
    - Requires IP address/hostname, port number and bot name as arguments. The bot name can be whatever you want.
      ```console
      python3 client.py localhost 4242 Bob
      ```
    - Type **client.py --h** for more info:
      ```console
      usage: client.py [-h] IP port name

      Connect to the chat room. Example: client.py localhost 4242 Steven

      positional arguments:
      IP          IP address of the server the client is connecting to.
      port        The port the client is connecting to (Integers only).
      name        The name of the client. Connect as a host or a bot(Ash, Misty or Brock)

      optional arguments:
      ```
