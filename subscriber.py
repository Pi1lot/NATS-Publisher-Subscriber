import asyncio
import nats

async def message_handler(msg):
    data = msg.data.decode()
    print(data)

async def run_subscriber():
    nc = await nats.connect("127.0.0.1:4222")

    await nc.subscribe("compteur", cb=message_handler)

    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(run_subscriber())
