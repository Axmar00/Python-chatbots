# PORTFOLIO 1 - s341848 - Izen Asmar Nasar
# TCP server
import socket,threading,sys,time,argparse

# parser that checks if necessary arguments are provided
argParser = argparse.ArgumentParser(description='Start the chat server and listen for incoming connections. Example: server.py 4242')
argParser.add_argument('port', type=int, help='The port the server is running on (Integers only).')
args = argParser.parse_args()
port = args.port

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('localhost', port))
serverSocket.listen() # listen for connections
clients = []       # list of clients
clientNames = []   # list of the clients' names   


# function to broadcast a given message from a client to the other clients
def messageAll(message, client):
    for i in clients:
        # dont send the message back to the original sender
        if i is not client:   
            i.send(message)
          

# function to take care of the chatting inbetween the clients(host and bots)
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            msg = message.decode().split(": ")

            if(msg[1] == "SHUTDOWN"):                
                time.sleep(1)
                print("Disconnecting clients")
                for i in clients:
                    i.close()
                print("Server status: Down\nStopped listening to connections...")
                exit()
                
            else:
                time.sleep(0.5)
                messageAll(message, client) #send to all bots
            
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = clientNames[index]
            messageAll(f'{name} has disconnected from the chat room!'.encode('utf-8'), client)
            print(f'{name} disconnected from the chat room')
            clientNames.remove(name)
            break


# function to set server status and connect incoming clients to the server(chat room)
def receive():
    print('\nServer status: Running\nListening to connections...\n')
    while True:        
        client, address = serverSocket.accept()  # accept connection    

        client.send('name?'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        clientNames.append(name)
        clients.append(client)
        print(f'Successfully established a connection with {name} {str(address)}')
        messageAll(f'{name} has connected to the chat room'.encode('utf-8'), client)
        client.send('You are now connected to the chat room!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()