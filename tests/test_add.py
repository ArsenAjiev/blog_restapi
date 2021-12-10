import pytest
from blog.sample import add


def test_add():
    assert add(3, 2) == 5


if __name__ == '__main__':
    pytest.main()
