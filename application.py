import logging
import os

from flask import Flask
from flask import request

import server_logic


application = Flask(__name__)

@application.route("/", methods=['GET'])
def handle_info():
    """
    This function is called when you register your Battlesnake on play.battlesnake.com
    See https://docs.battlesnake.com/guides/getting-started#step-4-register-your-battlesnake

    It controls your Battlesnake applicationearance and author permissions.
    For customization options, see https://docs.battlesnake.com/references/personalization

    TIP: If you open your Battlesnake URL in browser you should see this data.
    """
    print("INFO")
    return {
        "apiversion": "1",
        "author": "BOOM",  # TODO: Your Battlesnake Username
        "color": "#CE7575",  # TODO: Personalize
        "head": "evil",  # TODO: Personalize
        "tail": "curled",  # TODO: Personalize
    }


@application.route("/start", methods=['POST'])
def handle_start():
    """
    This function is called everytime your snake is entered into a game.
    request.json contains information about the game that's about to be played.
    """
    data = request.get_json()

    print(f"{data['game']['id']} START")
    return "ok"


@application.route("/move", methods=['POST'])
def handle_move():
    """
    This function is called on every turn of a game. It's how your snake decides where to move.
    Valid moves are "up", "down", "left", or "right".
    """
    data = request.get_json()

    # TODO - look at the server_logic.py file to see how we decide what move to return!
    move = server_logic.choose_move(data)

    return {"move": move}


@application.route("/end", methods=['POST'])
def end():
    """
    This function is called when a game your snake was in ends.
    It's purely for informational purposes, you don't have to make any decisions here.
    """
    data = request.get_json()

    print(f"{data['game']['id']} END")
    return "ok"


# if __name__ == "__main__":
#     logging.getLogger("werkzeug").setLevel(logging.ERROR)

#     print("Starting Battlesnake Server...")
#     port = int(os.environ.get("PORT", "8080"))
#     application.run(host="0.0.0.0", port=port, debug=True)
