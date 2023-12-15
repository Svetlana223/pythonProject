from sys import argv
import logging
logging.basicConfig(filename="../hm_5/log",
                    level=logging.INFO,
                    encoding='utf-8',
                    format='{levelname:<5}, asctime.now(), time:{asctime}, {msg}',
                    style='{')
logger = logging.getLogger()
def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        logger.info(f'{date} {month} {year} >>> should be date(1-31), month(1-12), and year(1-9999)')
        return False
    if month in (4, 6, 9, 11) and date > 30:
        logger.info(f'This day is not in {month} month')
        return False
    if month == 2 and is_leap(year) and date > 29:
        logger.info(f'This day is not in {month} month')
        return False
    if month == 2 and not is_leap(year) and date > 28:
        logger.info(f'This day is not in {month} month')
        return False
    return True

date_to_prove = '29.33.2023'
if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove))