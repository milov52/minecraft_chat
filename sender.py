import asyncio
import json

import aiofiles

from config import configure_sender_argument_parser, logging


async def register(reader, writer):
    data = await reader.readline()
    logging.debug(data.decode().strip())

    nickname = input()
    writer.write(nickname.encode() + b'\n')
    await writer.drain()

    register_data = await reader.readline()
    register_data = json.loads(register_data)
    logging.debug(register_data)

    async with aiofiles.open("hash.txt", "w") as myfile:
        await myfile.write(register_data["account_hash"])

    data = await reader.readline()
    logging.debug(data.decode().strip())


async def authorise(reader, writer):
    data = await reader.readline()

    if json.loads(data) is None:
        logging.error("Неизвестный токен. Проверьте его или зарегистрируйте заново")
        raise

    data = await reader.readline()
    logging.debug(data.decode().strip())


async def submit_message(writer, reader):
    while True:
        message = ''
        while True:
            input_data = input()
            message += input_data + '\n'

            if not input_data:
                break

        writer.write(message.encode())
        await writer.drain()

        chat_data = await reader.readuntil(b'\n')
        logging.debug(chat_data.decode().strip())


async def main(params):
    reader, writer = await asyncio.open_connection(params.host, 5050)
    data = await reader.readline()
    logging.debug(data.decode().strip())

    token = input()
    writer.write(token.encode() + b'\n')
    await writer.drain()

    if token == '':
        await register(reader, writer)
    else:
        await authorise(reader, writer)

    await submit_message(writer, reader)


if __name__ == '__main__':
    arg_parser = configure_sender_argument_parser()
    params = arg_parser.parse_args()
    logging.info(f"Аргументы командной строки {params}")
    asyncio.run(main(params))
