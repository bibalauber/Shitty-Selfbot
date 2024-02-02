@client.command("spam")
def spam(s, command):
    for i in range(int(command.args[0])):
        s.send_message(command.args[1], CHANNEL)