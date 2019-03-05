import os


class Config:
    class Game:
        MAP_HEIGHT = os.getenv("GAME_MAP_HEIGHT") or 1000
        MAP_WIDTH = os.getenv("GAME_MAP_WIDTH") or 1000
        BLINK_RANGE = os.getenv("BLINK_RANGE") or 20

    class Server:
        SECRET_KEY = os.getenv(
            "SECRET_KEY") or "SECREEEEEEET KEEEEEEEEEEY !!!!!!!! PJQWIN"
        DOMAIN = os.getenv("SHOOTER_HOST") or "localhost"
        PORT = int(os.getenv("SHOOTER_PORT", 0)) or 8000
        SCHEMA = os.getenv("SERVER_SCHEMA") or "ws"
