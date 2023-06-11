import asyncio
import contextlib
import json

import aiofiles

from config import configure_sender_argument_parser, logging


async def register(reader, writer, username):
    writer.write(b'\n')
    await writer.drain()

    data = await reader.readline()
    logging.debug(data.decode().strip())

    writer.write(username.encode() + b'\n')
    await writer.drain()

    register_data = await reader.readline()
    register_data = json.loads(register_data)
    logging.debug(register_data)

    async with aiofiles.open("hash.txt", "w") as myfile:
        await myfile.write(register_data["account_hash"])

    data = await reader.readline()
    logging.debug(data.decode().strip())


async def authorise(reader, writer, token):
    writer.write(token.encode() + b'\n')
    await writer.drain()

    data = await reader.readline()

    if not json.loads(data):
        logging.error("Неизвестный токен. Проверьте его или зарегистрируйте заново")
        raise

    data = await reader.readline()
    logging.debug(data.decode().strip())


async def submit_message(writer, reader, message):
    message = message.replace("\\n", "\n")
    text = message + '\n\n'

    writer.write(text.encode())
    await writer.drain()

    chat_data = await reader.readline()
    logging.debug(chat_data.decode().strip())


@contextlib.asynccontextmanager
async def open_connection(params):
    reader, writer = await asyncio.open_connection(params.server, params.port)
    try:
        yield reader, writer
    finally:
        writer.close()
        await writer.wait_closed()

async def main(params):
    async with open_connection(params) as (reader, writer):
        data = await reader.readline()
        logging.debug(data.decode().strip())

        token = params.token

        if not token:
            await register(reader, writer, params.username)
        else:
            await authorise(reader, writer, token)

        await submit_message(writer, reader, params.message)



if __name__ == '__main__':
    arg_parser = configure_sender_argument_parser()
    params = arg_parser.parse_args()
    logging.info(f"Аргументы командной строки {params}")
    asyncio.run(main(params))
