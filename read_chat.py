import argparse
import asyncio
import aiofiles
import logging

from datetime import datetime

from config import configure_argument_parser

DATE_TIME_FORMAT = '[%d.%m.%y %H:%M] '
logging.basicConfig(level=logging.INFO)
TOKEN = '5161ea5a-0482-11ee-ad76-0242ac110002'

async def read_chat(params):
    reader, _ = await asyncio.open_connection(params.host, params.port)

    while True:
        chat_data = await reader.readline()
        if not chat_data:
            break

        now = datetime.now()
        chat_data = now.strftime(DATE_TIME_FORMAT) + chat_data.decode()
        async with aiofiles.open(params.history, "a") as myfile:
            await myfile.write(chat_data)
        print(chat_data, end='')

if __name__ == '__main__':
    arg_parser = configure_argument_parser()
    params = arg_parser.parse_args()
    logging.info(f"Аргументы командной строки {params}")
    asyncio.run(read_chat(params))