import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger


@pytest.fixture
def mock_burger():
    bun = Bun("white", 50)
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 20)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    return burger


class TestBurger:

    def test_set_buns(self, mock_burger):
        assert mock_burger.bun.get_name() == "white"
        assert mock_burger.bun.get_price() == 50

    def test_add_ingredient(self, mock_burger):
        assert len(mock_burger.ingredients) == 2
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mayo", 10)
        mock_burger.add_ingredient(new_ingredient)
        assert len(mock_burger.ingredients) == 3
        assert mock_burger.ingredients[-1].get_name() == "mayo"
        assert mock_burger.ingredients[-1].get_price() == 10

    def test_remove_ingredient(self, mock_burger):
        assert len(mock_burger.ingredients) == 2
        mock_burger.remove_ingredient(0)
        assert len(mock_burger.ingredients) == 1
        assert mock_burger.ingredients[0].get_name() == "cutlet"

    def test_move_ingredient(self, mock_burger):
        assert mock_burger.ingredients[0].get_name() == "hot sauce"
        assert mock_burger.ingredients[1].get_name() == "cutlet"
        mock_burger.move_ingredient(0, 1)
        assert mock_burger.ingredients[0].get_name() == "cutlet"
        assert mock_burger.ingredients[1].get_name() == "hot sauce"

    def test_get_price(self, mock_burger):
        assert mock_burger.get_price() == 50 * 2 + 20 + 100
