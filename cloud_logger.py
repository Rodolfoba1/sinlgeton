from logger import Logger
from firebase import FireBase

class CloudLogger(Logger):
    def __init__(self, name: str):
        self.__BD: FireBase = FireBase(name)

    def message(self, msg: str):
        self.__BD.write(msg, "Info")

    def success(self, success_msg: str):
        self.__BD.write(success_msg, "Success")

    def warning(self, warning_msg: str):
        self.__BD.write(warning_msg, "Warning")

    def error(self, error_msg: str):
        self.__BD.write(error_msg, "Error")
