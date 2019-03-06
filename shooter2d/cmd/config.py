import os


class Config:
    class Game:
        MAP_HEIGHT = int(os.getenv("GAME_MAP_HEIGHT", 0)) or 100000
        MAP_WIDTH = int(os.getenv("GAME_MAP_WIDTH", 0)) or 100000

        BLINK_RANGE = int(os.getenv("BLINK_RANGE", 0)) or 20

        BULLET_SPEED = int(os.getenv("BULLET_SPEED", 0)) or 2
        BULLET_RADIUS = int(os.getenv("BULLET_RADIUS", 0)) or 5
        BULLET_TTL = int(os.getenv("BULLET_TTL", 0)) or 5
        BULLET_PAIN = int(os.getenv("BULLET_PAIN", 0)) or 30
        BULLET_DURATION = int(os.getenv("BULLET_DURATION", 0)) or 2

        PLAYER_SPEED = float(os.getenv("PLAYER_SPEED", 0)) or 0.5
        PLAYER_RADIUS = int(os.getenv("PLAYER_RADIUS", 0)) or 10

    class Server:
        SECRET_KEY = os.getenv(
            "SECRET_KEY") or "SECREEEEEEET KEEEEEEEEEEY !!!!!!!! PJQWIN"
        DOMAIN = os.getenv("SHOOTER_HOST") or "localhost"
        PORT = int(os.getenv("SHOOTER_PORT", 0)) or 8000
        SCHEMA = os.getenv("SERVER_SCHEMA") or "ws"
        SERVER_FPS = int(os.getenv("SERVER_FPS", 0)) or 20
