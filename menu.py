import os
import json
from settings import*

def save_game():
    with open("game_state.json", "w") as f:
        json.dump(game_state, f)

def load_game():
    global game_state
    if os.path.exists("game_state.json"):
        with open("game_state.json", "r") as f:
            game_state = json.load(f)
    else:
        print("No file")
