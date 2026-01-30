import logging
from pathlib import Path

logger = logging.getLogger(__name__)


log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

log_file = log_dir / f"{__name__}.log"
file_handler = logging.FileHandler(log_file, mode="w")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(funcName)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает её маску"""
    if isinstance(card_number, int):
        card_number_string = str(card_number)
        if len(card_number_string) == 16:
            card_number_list = list(card_number_string)
            card_number_list[6:12] = ["*", "*", "*", "*", "*", "*"]
            card_number_list.insert(4, " ")
            card_number_list.insert(9, " ")
            card_number_list.insert(14, " ")
            card_number_string_new = "".join(card_number_list)
            logger.info("Функция выполнена успешно")
            return card_number_string_new
        logger.error("Неправильная длина карты")
    logger.error("Неверные данные")
    return "Неверные данные, только номер карты. Пример :1234567890123456"


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску"""
    if isinstance(account, int):
        account_string = str(account)
        if len(account_string) == 20:
            account_list = list(account_string)
            account_list[:-4] = ["*", "*"]
            account_list_new = "".join(account_list)
            logger.info("Функция выполнена успешно")
            return account_list_new
        logger.error("Неправильная длина счёта")
    logger.error("Неверные данные")
    return "Неверные данные, только номер счёта. Пример :12345678901234567890"
