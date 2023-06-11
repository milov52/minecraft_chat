import asyncio
import logging
from datetime import datetime

import aiofiles

from config import configure_reader_argument_parser

DATE_TIME_FORMAT = '[%d.%m.%y %H:%M] '


async def read_chat(params):
    reader, _ = await asyncio.open_connection(params.server, params.port)

    while True:
        try:
            chat_data = await reader.readuntil()

            if not chat_data:
                break

            now = datetime.now()
            chat_data = now.strftime(DATE_TIME_FORMAT) + chat_data.decode()
            async with aiofiles.open(params.file_path, "a") as myfile:
                await myfile.write(chat_data)
            print(chat_data.strip())
        except asyncio.TimeoutError:
            print("Превышено время ожидания")

if __name__ == '__main__':
    arg_parser = configure_reader_argument_parser()
    params = arg_parser.parse_args()
    logging.debug(f"Аргументы командной строки {params}")
    asyncio.run(read_chat(params))
