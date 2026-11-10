"""ЛР №1, вариант 2: учебный Python-проект для демонстрации Git."""


def greeting(name: str) -> str:
    """Вернуть приветствие для пользователя."""
    return f"Привет, {name}!"


if __name__ == "__main__":
    print(greeting("Герман"))
