#PORTFOLIO 1 - s341848 - Izen Asmar Nasar
#TCP client
import socket,random,threading,sys,time,argparse

bots=["ash","misty","brock"]

# parser that checks if necessary arguments are provided
argParser = argparse.ArgumentParser(description='Connect to the chat room. Example: client.py localhost 4242 Steven')
argParser.add_argument('IP', type=str, help='IP address of the server the client is connecting to.')
argParser.add_argument('port', type=int, help='The port the client is connecting to (Integers only).')
argParser.add_argument('name', type=str, help='The name of the client. Connect as a host or a bot(Ash, Misty or Brock)')
args = argParser.parse_args()
IP = args.IP
port = args.port
name = args.name

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, port))

# list of good and bad actions
good_things=["sing", "play", "walk", "read", "train", "sleep"]
bad_things=["shout", "fight", "hack", "bicker", "complain", "steal"]


# all bot functions
def ash(verb):
    if verb in good_things:
        altAnswers = [
        "{}: Did you say {}? That'd be amazing!".format(name,verb + "ing"),
        "{}: I think {} sounds great!".format(name,verb + "ing"),
        "{}: Finally we can start {}!".format(name,verb + "ing")
    ]
        return random.choice(altAnswers)

    elif verb in bad_things:
        altAnswers2 = [
        "{}: {}? You must be out of your mind!".format(name,verb + "ing"),
        "{}: I'm not a fan of {}, sorry.".format(name,verb + "ing"),
        "{}: Yeah I don't know about {}...".format(name,verb+"ing")
    ]
        return random.choice(altAnswers2)

    else:
        return "{}: Sorry, but that's just boring..".format(name)

def misty(verb):
    altAnswers3 = [
        "{}: {}...? You can't be serious..".format(name,verb + "ing"),
        "{}: {} sounds really boring..".format(name,verb + "ing"),
        "{}: I've got better things to do than {}..".format(name,verb+"ing")
    ]

    if verb in bad_things or verb in good_things:
        return random.choice(altAnswers3)

    else:
        altAnswers4 = [
        "{}: Nope. Not doing that.".format(name),
        "{}: You really expect me to do that?".format(name),
        "{}: I don't want to do that.".format(name)
    ]
        return random.choice(altAnswers4)

def brock(verb):
    if verb in bad_things:
        altAnswers5 = [
        "{}: {}?? I am not mentally prepared for that yet.".format(name,verb+"ing"),
        "{}: You know how I feel about {}...".format(name,verb + "ing"),
        "{}: Ooh {}? Meh..".format(name,verb+"ing")
    ]
        return random.choice(altAnswers5)

    elif verb in good_things:
        altAnswers6 = [
        "{}: {}?? Sure, why not?".format(name,verb+"ing"),
        "{}: {} it is then.".format(name,verb + "ing"),
        "{}: I mean.. I guess {} isn't that bad.".format(name,verb+"ing")
    ]
        return random.choice(altAnswers6)

    else:
        return "{}: I am uncertain...".format(name)

# function that handles the messages received from other clients
def clientReceive():
    while True:
        msg = clientSocket.recv(1024).decode('utf-8')

        if msg == "name?":
            clientSocket.send(name.encode('utf-8'))

        else:
            if ":" in msg:

                msgSplit = msg.split(": ")

                if msgSplit[0] not in bots:
                    v=""
                    i=0
                    while i<len(bad_things):
                        if bad_things[i] in msg.lower():
                            v=bad_things[i]

                        if good_things[i] in msg.lower():
                            v=good_things[i]
                        i+=1

                    botmsg=""
                    if name.lower() == "ash":
                        botmsg=ash(v)

                    elif name.lower() == "misty":
                        botmsg=misty(v)

                    elif name.lower() == "brock":
                        botmsg=brock(v)

                    print(msg)
                    clientSend(botmsg)

                else:
                    time.sleep(0.5)
                    print(msg)

            else:
                print(msg)


def clientSend(msg):
    print(msg)
    clientSocket.send(msg.encode('utf-8'))

# function that forwards a host-client's message
def clientMessager():
    while True:
        try:
            msg = f'{name}: {input()}'
            split = msg.split(": ")
            if(split[1].isspace() or split[1] == ""):
                print("Can't send an empty string. Please write something!")
                continue
            else:
                time.sleep(0.4)
                print(msg)
                clientSocket.send(msg.encode('utf-8'))
        except:
            print("\nYou have disconnected from the chat room\n")
            sys.exit()
            break
            

receive_thread = threading.Thread(target=clientReceive)
receive_thread.start()

if name not in bots:
    send_thread = threading.Thread(target=clientMessager)
    send_thread.start()