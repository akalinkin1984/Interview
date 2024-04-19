import pytest

from task_1_2 import check_brackets


@pytest.mark.parametrize(
    'param, expected',
    (
        ['(((([{}]))))', 'Сбалансированно'],
        ['[([])((([[[]]])))]{()}', 'Сбалансированно'],
        ['{{[()]}}', 'Сбалансированно'],
        ['}{}', 'Несбалансированно'],
        ['{{[(])]}}', 'Несбалансированно'],
        ['[[{())}]', 'Несбалансированно'],
        ['((((()', 'Несбалансированно']
    )
)
def test_check_brackets(param, expected):
    actual = check_brackets(param)
    assert actual == expected
