import json
from pathlib import Path

DATA_DIRECTORY = Path.home() / "Library" / "Application Support" / "Pomodoro"
STATE_FILE = DATA_DIRECTORY / "state.json"

def load_state():
    if not STATE_FILE.exists():
        return {"status": "idle"}

    with STATE_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_state(state):
    DATA_DIRECTORY.mkdir(parents=True, exist_ok=True)

    with STATE_FILE.open("w", encoding="utf-8") as file:
        json.dump(state, file, indent=4)