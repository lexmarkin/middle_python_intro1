# """Генератор приветствий."""


def greeting(name: str) -> str:
    # """Возвращает текст приветствия.
    #
    # Args:
    #     name: Имя пользователя
    #
    # Returns:
    #     int: Текст приветствия
    # """
    capitalize_name = ' '.join([arg.capitalize() for arg in name.split()])
    return ''.join(['Привет, ', capitalize_name])
