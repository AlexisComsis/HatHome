import json
import os

class constructor:
    # Create the file config
    def config_txt():
        config = {}
        config["config"] = {"width": "1600","height": "900","volume": "0.2","character": "0"}
        data = json.dumps(config)
        with open("Alterable\Config.txt", "w") as file:
            file.write(data)
    # Create the file player
    def player_txt():
        player = {}
        player["player"] = {"position": "0"}
        player["inventory"] = {"slot number": "4"}
        data = json.dumps(player)
        with open("Alterable\Player.txt", "w") as player:
            player.write(data)
    # Create the file monders
    def monders_txt():
        monders = {}
        monders["johnson"] = {"slots": "6","endurance": "6","strength": "2","vision": "2"}
        data  = json.dumps(monders)
        with open("Alterable\Monders.txt", "w") as monders:
            monders.write(data)
    # Creation du fichier options
    def options_txt():
        data = {"options": {"width": "1920", "height": "1080", "volume": "0.2", "character": "0"}}
        data = json.dumps(data)
        with open("Alterable\Options.txt", "w") as options:
            options.write(data)

if not os.path.exists(os.curdir+"\Alterable"):
    os.mkdir("Alterable")
if not os.path.exists(os.curdir+"Alterable\Monders.txt"):
    constructor.monders_txt()
if not os.path.exists(os.curdir+"Alterable\Player.txt"):
    constructor.player_txt()
if not os.path.exists(os.curdir+"Alterable\Config.txt"):
    constructor.config_txt()
if not os.path.exists(os.curdir+"Alterable\Options.txt"):
    constructor.options_txt()
