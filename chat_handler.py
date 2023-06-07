import asyncio
import logging

from config import configure_argument_parser

DATE_TIME_FORMAT = '[%d.%m.%y %H:%M] '
logging.basicConfig(level=logging.INFO)
TOKEN = '5161ea5a-0482-11ee-ad76-0242ac110002'


async def auth(reader, writer):
    data = await reader.readline()
    print(data.decode(), end='')

    token = TOKEN.encode()
    writer.write(token + b'\n')
    await writer.drain()

    data = await reader.readline()
    print(data.decode(), end='')
    data = await reader.readline()
    print(data.decode(), end='')


async def write_to_chat(writer, reader):
    while True:
        message = input()
        writer.write(message.encode()+b'\n\n')
        await writer.drain()

        chat_data = await reader.readuntil(b'\n')
        print(chat_data.decode(), end='')


async def main(params):
    reader, writer = await asyncio.open_connection(params.host, 5050)
    await auth(reader, writer)
    await write_to_chat(writer, reader)


if __name__ == '__main__':
    arg_parser = configure_argument_parser()
    params = arg_parser.parse_args()
    logging.info(f"Аргументы командной строки {params}")
    asyncio.run(main(params))
