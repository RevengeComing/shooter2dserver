import asyncio
import random
import math

from shooter2d.client import Shooter2DClinet

clients = []
for i in range(80):
    client = Shooter2DClinet(
        "http://localhost:8000/login", "sepehr%d" % i)
    clients.append(client)


async def main():
    for c in clients:
        await c.login()

    while True:
        for c in clients:
            movement = [random.randint(-1, 1), random.randint(-1, 1)]
            if movement[0] ** 2 == 1 and movement[1] ** 2 == 1:
                movement[0] = movement[0] * math.cos(45 * math.pi / 180)
                movement[1] = movement[1] * math.sin(45 * math.pi / 180)
            await c.move(movement)
        await asyncio.sleep(0.1)

try:
    asyncio.get_event_loop().run_until_complete(main())
except KeyboardInterrupt:
    print("Bye Bye")
