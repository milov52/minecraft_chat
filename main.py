import asyncio
import aiofiles
from datetime import datetime

SERVER_HOST = 'minechat.dvmn.org'
SERVER_PORT = 5000
DATE_TIME_FORMAT = '[%d.%m.%y %H:%M] '

async def read_chat():
    reader, writer = await asyncio.open_connection(
        SERVER_HOST, SERVER_PORT)


    while True:
        chat_data = await reader.read(200)
        now = datetime.now()
        chat_data = now.strftime(DATE_TIME_FORMAT) + chat_data.decode()
        async with aiofiles.open("test.txt", "a") as myfile:
            await myfile.write(chat_data)
        print(chat_data, end='')

if __name__ == '__main__':
    asyncio.run(read_chat())