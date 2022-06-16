from cloud_logger import CloudLogger
from logger import Logger


def main():
    db1: Logger = CloudLogger("File")
    db2: Logger = CloudLogger("File2")

    if id(db1.message("Hello")) == id(db2.message("Wolrd")):
        print("Son de la misma instancia")
    else:
        print("Son diferentes")


main()
