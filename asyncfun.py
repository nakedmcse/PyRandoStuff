# Async Python
import asyncio


async def dragon():
    raise Exception("Dragon beat Tiger")


async def tiger():
    task = asyncio.create_task( dragon() )
    print("Tiger beat Dragon")


async def main():
    try:
        await tiger()
    except Exception as e:
        print(e)


asyncio.run(main())