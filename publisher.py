import asyncio
import nats

async def run_publisher():
    nc = await nats.connect("127.0.0.1:4222")
    compteur = 0

    try:
        while True:
            compteur += 2
            message = compteur
            await nc.publish("compteur", str(message).encode())
            print(message)
            await asyncio.sleep(10)
    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        await nc.close()

if __name__ == '__main__':
    asyncio.run(run_publisher())
