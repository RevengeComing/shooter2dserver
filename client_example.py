import asyncio
from shooter2d.client import Shooter2DClinet


client = Shooter2DClinet("http://sepehr.hamzehlouy.com:8000/login", "sepehr")


try:
    while True:
        asyncio.get_event_loop().run_until_complete(client.login())
except KeyboardInterrupt:
    print("Bye Bye")
