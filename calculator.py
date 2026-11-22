"""Простой калькулятор для демонстрации Jenkins."""


def add(a, b):
    """Сложение: возвращает a + b."""
    return a + b


def subtract(a, b):
    """Вычитание: возвращает a - b."""
    return a - b


def multiply(a, b):
    """Умножение: возвращает a * b."""
    return a * b


def divide(a, b):
    """Деление: возвращает a / b.

    Raises:
        ValueError: если b равен нулю.
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def pow(a, b):
    return a ** b