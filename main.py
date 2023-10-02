import asyncio
from utils import loggers


async def main():
    from client.main import main as client_start
    await asyncio.gather(client_start())

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        loggers.root.info('Interrupted while running. Exiting...')
