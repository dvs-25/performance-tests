import logging


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Проверяем, есть ли уже добавленные обработчики у логгера.
    # Это необходимо, чтобы избежать дублирования логов, особенно в тех случаях,
    # когда логгер уже был сконфигурирован внешней системой, например Locust или pytest.
    # Без этой проверки обработчик StreamHandler будет добавляться каждый раз заново,
    # из-за чего каждое лог-сообщение будет выводиться по два и более раза.
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
