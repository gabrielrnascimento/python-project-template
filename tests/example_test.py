from src.example import add
from tests.helper import generate_string


class TestExample:

    def test_add(self) -> None:
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(-1, -1) == -2

    def test_string(self) -> None:
        assert generate_string() == "hello"
