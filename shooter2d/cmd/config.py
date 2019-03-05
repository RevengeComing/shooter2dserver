import os


class Config:
    class Game:
        MAP_HEIGHT = os.getenv("GAME_MAP_HEIGHT") or 1000
        MAP_WIDTH = os.getenv("GAME_MAP_WIDTH") or 1000

    class Server:
        SECRET_KEY = os.getenv(
            "SECRET_KEY") or "SECREEEEEEET KEEEEEEEEEEY !!!!!!!! PJQWIN"
