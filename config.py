import argparse
import logging

import os
from dotenv import load_dotenv
load_dotenv()


SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT_READER = os.getenv("SERVER_PORT_READER")
SERVER_PORT_SENDER = os.getenv("SERVER_PORT_SENDER")
FILE_PATH = os.getenv("FILE_PATH")
TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.DEBUG)

def configure_reader_argument_parser():
    parser = argparse.ArgumentParser(
        description="Асинхронный микросервис для парсинга чата")

    parser.add_argument(
        "-s",
        "--server",
        help="Адрес сервера чата",
        default=SERVER_HOST
    )

    parser.add_argument(
        "-p",
        "--port",
        help="Порт сервера чата",
        default=SERVER_PORT_READER
    )

    parser.add_argument(
        "-f",
        "--file_path",
        help="Путь к файлу для сохранения результатов",
        default=FILE_PATH
    )
    return parser

def configure_sender_argument_parser():
    parser = argparse.ArgumentParser(
        description="Асинхронный микросервис для отправки сообщений в чат")

    parser.add_argument(
        "-m",
        "--message",
        required=True,

        help="Текст сообщения"
    )

    parser.add_argument(
        "-p",
        "--port",
        help="Порт сервера чата",
        default=SERVER_PORT_SENDER
    )

    parser.add_argument(
        "-s",
        "--server",
        help="Адрес сервера чата",
        default=SERVER_HOST
    )

    parser.add_argument(
        "-t",
        "--token",
        help="Токен зарегистрированного пользователя",
        default=TOKEN
    )

    parser.add_argument(
        "-u",
        "--username",
        help="Имя пользователя для регистрации",
        default="new_user"
    )

    return parser