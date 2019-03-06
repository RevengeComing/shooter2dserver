import asyncio
from shooter2d.client import Shooter2DClinet


client = Shooter2DClinet("http://sepehr.hamzehlouy.com:8000/login", "sepehr")


async def main():
    await client.login()
    await client.move([0, 1])
    while True:
        await asyncio.sleep(0.1)

try:
    asyncio.get_event_loop().run_until_complete(main())
except KeyboardInterrupt:
    print("Bye Bye")
