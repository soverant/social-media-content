import asyncio
import telegram


async def main():
    bot = telegram.Bot("7409828464:AAFTgeEpiL7ffQKbdOi47U8HtZ3lNE7Zby8")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())