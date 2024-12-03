import pytest
from praktikum.bun import Bun

class TestBun:

    def test_bun_initialization(self):
        bun = Bun("white", 50)
        assert bun.get_name() == "white"
        assert bun.get_price() == 50

    def test_bun_initialization_with_negative_price(self):
        bun = Bun("black", -10)
        assert bun.get_name() == "black"
        assert bun.get_price() == -10

    def test_bun_initialization_with_zero_price(self):
        bun = Bun("red", 0)
        assert bun.get_name() == "red"
        assert bun.get_price() == 0

    def test_bun_price(self):
        bun = Bun("blue", 100)
        assert bun.get_price() == 100

    def test_bun_name(self):
        bun = Bun("green", 150)
        assert bun.get_name() == "green"
