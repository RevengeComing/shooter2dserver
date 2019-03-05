import os


class Config:
    class Game:
        MAP_HEIGHT = int(os.getenv("GAME_MAP_HEIGHT", 0)) or 100000
        MAP_WIDTH = int(os.getenv("GAME_MAP_WIDTH", 0)) or 100000

        BLINK_RANGE = os.getenv("BLINK_RANGE") or 20

        BULLET_SPEED = os.getenv("BULLET_SPEED") or 2
        BULLET_TTL = os.getenv("BULLET_TTL") or 5

        PLAYER_SPEED = float(os.getenv("PLAYER_SPEED", 0)) or 0.5

    class Server:
        SECRET_KEY = os.getenv(
            "SECRET_KEY") or "SECREEEEEEET KEEEEEEEEEEY !!!!!!!! PJQWIN"
        DOMAIN = os.getenv("SHOOTER_HOST") or "localhost"
        PORT = int(os.getenv("SHOOTER_PORT", 0)) or 8000
        SCHEMA = os.getenv("SERVER_SCHEMA") or "ws"
        SERVER_FPS = int(os.getenv("SERVER_FPS", 0)) or 20
