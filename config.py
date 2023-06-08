import argparse
import logging

SERVER_HOST = 'minechat.dvmn.org'
SERVER_PORT_READER = 5000
SERVER_PORT_SENDER = 5000
FILE_PATH = 'minechat.history'

logging.basicConfig(level=logging.DEBUG)

def configure_reader_argument_parser():
    parser = argparse.ArgumentParser(
        description="Асинхронный микросервис для парсинга чата")

    parser.add_argument(
        "--port",
        help="Порт сервера чата",
        default=SERVER_PORT_READER
    )

    parser.add_argument(
        "--host",
        help="Адрес сервера чата",
        default=SERVER_HOST
    )

    parser.add_argument(
        "--history",
        help="Путь к файлу для сохранения результатов",
        default=FILE_PATH
    )
    return parser

def configure_sender_argument_parser():
    parser = argparse.ArgumentParser(
        description="Асинхронный микросервис для отправки сообщений в чат")

    parser.add_argument(
        "--port",
        help="Порт сервера чата",
        default=SERVER_PORT_SENDER
    )

    parser.add_argument(
        "--host",
        help="Адрес сервера чата",
        default=SERVER_HOST
    )

    parser.add_argument(
        "--history",
        help="Путь к файлу для сохранения результатов",
        default=FILE_PATH
    )
    return parser