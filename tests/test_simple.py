"""
Простые тесты для ознакомления с GitHub Actions (ЛР 3).
Покрывают классические примеры: деление на ноль и чётность/нечётность.
"""


def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("деление на ноль")
    return a / b


def is_even(n):
    return n % 2 == 0


def test_division_by_zero_raises():
    """Деление на ноль должно вызывать ZeroDivisionError."""
    try:
        safe_divide(10, 0)
    except ZeroDivisionError:
        assert True
        return
    assert False, "Ожидалось ZeroDivisionError"


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5.0


def test_even_numbers():
    assert is_even(2) is True
    assert is_even(4) is True


def test_odd_numbers():
    assert is_even(3) is False
    assert is_even(7) is False
