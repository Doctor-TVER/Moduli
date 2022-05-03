"""
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
"""


from math import pi, sqrt, pow, hypot


def test_sqrt():
    assert sqrt(9) == 3

def test_pow():
    assert pow(2, 0) == 1
    assert pow(2, 3) == 8


def test_pi():
    assert pi == 3.141592653589793


def test_hypot():
    assert hypot(1, 1) == 1.4142135623730951


numbers = [1, 2, 3, 4, ]


def test_map():
    m_result = list(map(lambda x: x % 2 == 0, numbers))
    print('!!!!!!!!!!!!!!!!!!!!!', m_result)
    assert m_result == [False, True, False, True]


def test_filter():
    assert list(filter(lambda x: x % 2 == 0, numbers)) == [2, 4]
    assert list(filter(lambda x: x % 2 == 0, numbers)) == [2, 4]


def test_sorted():
    assert sorted(numbers) == [1, 2, 3, 4, ]

