import argparse

SERVER_HOST = 'minechat.dvmn.org'
SERVER_PORT = 5000
FILE_PATH = 'minechat.history'


def configure_argument_parser():
    parser = argparse.ArgumentParser(
        description="Асинхронный микросервис для парсинга чата")

    parser.add_argument(
        "--port",
        help="Порт сервера чата",
        default=SERVER_PORT
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
