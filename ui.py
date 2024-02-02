from pystyle import *
from functions import *
from utils import *
import threading
import json
import time


logo = f'''
███████ ██   ██ ██ ████████ ████████ ██    ██     ███████ ███████ ██      ███████ ██████   ██████  ████████ 
██      ██   ██ ██    ██       ██     ██  ██      ██      ██      ██      ██      ██   ██ ██    ██    ██    
███████ ███████ ██    ██       ██      ████       ███████ █████   ██      █████   ██████  ██    ██    ██    
     ██ ██   ██ ██    ██       ██       ██             ██ ██      ██      ██      ██   ██ ██    ██    ██    
███████ ██   ██ ██    ██       ██       ██        ███████ ███████ ███████ ██      ██████   ██████     ██


                =================== Press \'{get_global_var('PREFIX')}\' to execute commands ===================

                
'''
anim = f'''
███████ ██   ██ ██ ████████ ████████ ██    ██     ███████ ███████ ██      ███████ ██████   ██████  ████████ 
██      ██   ██ ██    ██       ██     ██  ██      ██      ██      ██      ██      ██   ██ ██    ██    ██    
███████ ███████ ██    ██       ██      ████       ███████ █████   ██      █████   ██████  ██    ██    ██    
     ██ ██   ██ ██    ██       ██       ██             ██ ██      ██      ██      ██   ██ ██    ██    ██    
███████ ██   ██ ██    ██       ██       ██        ███████ ███████ ███████ ██      ██████   ██████     ██


                            =================== Press Enter ===================

                
'''
logostatic = Colorate.Vertical(Colors.purple_to_blue, logo, 2)
stop_thread = False
cls()
print(intro)
init()


time.sleep(1)
#Anime.Fade(Center.Center(anim), Colors.purple_to_blue, Colorate.Vertical, interval=0.1, enter=True)
#print(logostatic)

#Selfbot(get_global_var('TOKEN'), get_global_var('CHANNEL'), ".").send_message("lol", get_global_var('CHANNEL'))

#threading.Thread(target=run_scripts, args=("Scripts", )).start()

while 1: 
    command = input(Colorate.Diagonal(Colors.purple_to_blue, "> ", 2))
    handle_cmd_command(command)