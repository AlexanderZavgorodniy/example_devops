# API калькулятора

Модуль `calculator.py` — четыре арифметические операции.

## `add(a, b)`

Сложение. Возвращает `a + b`.

```python
from calculator import add
add(2, 3)  # 5
```

## `subtract(a, b)`

Вычитание. Возвращает `a - b`.

```python
from calculator import subtract
subtract(5, 3)  # 2
```

## `multiply(a, b)`

Умножение. Возвращает `a * b`.

```python
from calculator import multiply
multiply(4, 3)  # 12
```

## `divide(a, b)`

Деление. Возвращает `a / b`.

При `b == 0` выбрасывает `ValueError`.

```python
from calculator import divide
divide(10, 2)  # 5.0
```

## Тесты и покрытие

```bash
pytest
```

Отчёт: `htmlcov/index.html`
