import json
import os

class constructor:
    # Create the file config
<<<<<<< HEAD
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
=======
>>>>>>> 4ac6ae93605bb948d9d9c941ea52bfb50e3176ae
    def options_txt():
        options = {}
        options["Width"] = 1600
        options["Height"] = 900

        data = json.dumps(options)
        with open("Assets\Data\Options.txt", "w") as file:
            file.write(data)

if not os.path.exists(os.curdir+"Assets\Data"):
    os.mkdir("Assets\Data")
if not os.path.exists(os.curdir+"Assets\Data\Options.txt"):
    constructor.options_txt()
