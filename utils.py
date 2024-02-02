def check_packages():
    try:
        import requests
        import pystyle
    except ModuleNotFoundError:
        import os
        os.system("pip install requests")
        os.system("pip install pystyle")
        os.system("pip3 install requests")
        os.system("pip3 install pystyle")
        os.system(f"python {__file__}")

check_packages()

from pystyle import *
from functions import *
import os
import threading
import json
import webbrowser
import requests

def get_global_var(name):
    return json.loads(open("globals.json", "r").read())[name]

def load_scripts(folder_path):
    customs_scripts = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Remove the ".py" extension
            module_path = f"{folder_path}.{module_name}"
            content = open(f"{folder_path}/{filename}", "r").read()

            try:
                customs_scripts.append(content)
                pbprint(f"[+] Added {filename} to the customs scripts")
            except Exception as e:
                pbprint(f"[!] Error adding script {module_name}: {e}")

    return customs_scripts

def run_scripts(folder_path):
    customs_scripts = load_scripts(folder_path)

    globals = {
        "client": Selfbot(get_global_var('TOKEN'), get_global_var('CHANNEL'), ".").send_message("lol", get_global_var('CHANNEL')),
        "command": None
    }

    while True:
        for i in customs_scripts:
            exec(i, globals)

def displayNotification(message,title=None,subtitle=None,soundname=None):
    """
        Display an OSX notification with message title an subtitle
        sounds are located in /System/Library/Sounds or ~/Library/Sounds
    """
    titlePart = ''
    if(not title is None):
        titlePart = 'with title "{0}"'.format(title)
    subtitlePart = ''
    if(not subtitle is None):
        subtitlePart = 'subtitle "{0}"'.format(subtitle)
    soundnamePart = ''
    if(not soundname is None):
        soundnamePart = 'sound name "{0}"'.format(soundname)

    appleScriptNotification = 'display notification "{0}" {1} {2} {3}'.format(message,titlePart,subtitlePart,soundnamePart)
    os.system("osascript -e '{0}'".format(appleScriptNotification))


def discord_selfbot():
    global customs_scripts

    token = get_global_var('TOKEN')
    prefix = get_global_var('PREFIX')
    CHANNEL = get_global_var('CHANNEL')
    
    client = Selfbot(token, CHANNEL, prefix)

    cls()
    print(intro)

    pbprint(f"[•] Running with account: {client.get_username()}")
    pbprint(f"[•] Use prefix \'{client.PREFIX}\' for commands")

    displayNotification(
        f"Connected as: {client.get_username()}",
        "Shitty Selfbot is running!"
    )

    namespace = {
        'client': client,
        'CHANNEL': CHANNEL
    }

    while 1:
        for i in customs_scripts:
            exec(i, namespace)

        @client.command("reboot")
        def reboot(s, command):
            s.delete_message(command.id, CHANNEL)

            cls()
            os.system(f"python3 \"{__file__}\"")




def pbprint(text): print(Colorate.Diagonal(Colors.purple_to_blue, text, 2))

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def init():
    if os.path.exists("globals.json"): 
        with open("globals.json", "r") as f:
            if json.loads(f.read())['AUTORUN']: discord.start()

        return "globals.json already created"
    else:
        f = open("globals.json", "wb")
        f.write(b"{}")

        token = Write.Input("Enter your discord token > ", Colors.purple_to_blue, interval=0.01)
        webhook = Write.Input("Enter your webook url (leave blank if none) > ", Colors.purple_to_blue, interval=0.01)
        prefix = Write.Input("Enter the prefix > ", Colors.purple_to_blue, interval=0.01)
        channel = Write.Input("Enter the channel id > ", Colors.purple_to_blue, interval=0.01)

        f = open("globals.json", "w")
        f.write(json.dumps({
            "TOKEN": token,
            "WEBHOOK_URL": webhook,
            "AUTORUN": False,
            "PREFIX": prefix,
            "CHANNEL": channel
        }))
        
        time.sleep(0.5)
        pbprint("[+] Loaded Sucsessfully, enjoy !")
        time.sleep(0.5)
        cls()
        print(intro)

        return "globals.json created successfully"
    
def handle_cmd_command(command):
    if command.startswith("set"):
        with open("globals.json", "r") as f: globals_var = json.loads(f.read())

        args = command.split(" ")[1:]

        if args[0] in ['TOKEN', 'WEBOOK_URL', 'AUTORUN', 'PREFIX', 'CHANNEL']:
            if args[0] == "AUTORUN": globals_var[args[0]] = not globals_var[args[0]]
            else: globals_var[args[0]] = args[1]
        else: pbprint("[!] Invalid global variable name")

        with open("globals.json", "w") as f:
            f.write(json.dumps(globals_var))

    elif command == "clear":
        cls()
        print(intro)

    elif command == "reboot":
        import os
        cls()
        os.system(f"python3 \"{__file__}\"")

    elif command == "discord":
        try:
            url = requests.get("https://raw.githubusercontent.com/bibalauber/Shitty-Selfbot/main/discord.txt")
            webbrowser.open(url.text)
        except: pbprint("[!] Failed to get the discord invite link :(")

    elif command == "run": discord.start()
    elif command == "stop":
        stop_thread = True
        discord.join()
    else: pbprint("[!] Invalid command: type \'help\' for help")


logo = f'''
███████ ██   ██ ██ ████████ ████████ ██    ██     ███████ ███████ ██      ███████ ██████   ██████  ████████ 
██      ██   ██ ██    ██       ██     ██  ██      ██      ██      ██      ██      ██   ██ ██    ██    ██    
███████ ███████ ██    ██       ██      ████       ███████ █████   ██      █████   ██████  ██    ██    ██    
     ██ ██   ██ ██    ██       ██       ██             ██ ██      ██      ██      ██   ██ ██    ██    ██    
███████ ██   ██ ██    ██       ██       ██        ███████ ███████ ███████ ██      ██████   ██████     ██


                =================== Press \'{get_global_var('PREFIX')}\' to execute commands ===================

                
'''
intro = Colorate.Diagonal(Colors.purple_to_blue, logo, 2)
discord = threading.Thread(target=discord_selfbot)
customs_scripts = load_scripts("Scripts")