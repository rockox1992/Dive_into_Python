"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""
import sys
from datetime import datetime


def date_validate(date_text: str):
    try:
        value = datetime.strptime(date_text, "%d.%m.%Y").date()
        print("GOOD DATA")
    except:
        print("BAD DATA")


def _leap_info(date_text: str):
    year = int(date_text.split(".")[-1])
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("GOOD DATA leap")
    else:
        print("BAD DATA leap")


if __name__ == '__main__':
    #date_validate("25.05.1992")
    #_leap_info("25.05.1992")
    date_validate(sys.argv[1])
    _leap_info(sys.argv[1])
