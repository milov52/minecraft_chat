import asyncio
import json

# import logging

from config import configure_argument_parser, logging

DATE_TIME_FORMAT = '[%d.%m.%y %H:%M] '
logging.basicConfig(level=logging.INFO)
TOKEN = '5161ea5a-0482-11ee-ad76-0242ac110002'


async def auth(reader, writer):
    data = await reader.readline()
    logging.debug(data.decode().strip())

    token = input("Input token\n")
    writer.write(token.encode() + b'\n')
    await writer.drain()

    data = await reader.readline()
    if json.loads(data) is None:
        logging.debug("Неизвестный токен. Проверьте его или зарегистрируйте заново")
        return

    data = json.loads(data)
    logging.debug(data)

    data = await reader.readline()
    logging.debug(data.decode().strip())


async def write_to_chat(writer, reader):
    while True:
        message = input()
        writer.write(message.encode()+b'\n\n')
        await writer.drain()

        chat_data = await reader.readuntil(b'\n')
        logging.debug(chat_data.decode().strip())


async def main(params):
    reader, writer = await asyncio.open_connection(params.host, 5050)
    await auth(reader, writer)
    await write_to_chat(writer, reader)


if __name__ == '__main__':
    arg_parser = configure_argument_parser()
    params = arg_parser.parse_args()
    logging.info(f"Аргументы командной строки {params}")
    asyncio.run(main(params))
