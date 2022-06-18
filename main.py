import traceback
from cloud_logger import CloudLogger
from logger import Logger


def main():
    db1: Logger = CloudLogger("File")
    db2: Logger = CloudLogger("File2")
    option: bool = True
    while option:
        try:
            db1.message("Enter a number.")
            db2.message("Enter a number.")
            numb: int = int(input('\n'))
            if numb > 0 or numb < 10:
                db1.warning("You must enter a number greater than zero and less than 10")
                db1.warning("You must enter a number greater than zero and less than 10")
            else:
                db1.success(f'Correct number = {numb}')
                db1.success(f'Correct number = {numb}')
                option = False

        except BaseException:
            db1.error("Enter a correct number = " + traceback.format_exc())
            db1.error("Enter a correct number = " + traceback.format_exc())


main()
