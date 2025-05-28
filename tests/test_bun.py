import pytest

from bun import Bun

class TestBun:

    @pytest.fixture
    def bun():
        return Bun('tralalelo tralala', 200.99)

    def test_get_bun_name(bun):
        assert bun.get_name() == 'tralalelo tralala', 'Имя булочки не соответствует ожидаемому'

    def test_get_bun_price(bun):
        assert bun.get_price() == 200.99, 'Цена булочки не соответствует ожидаемой'

    def test_get_bun_name_return_str(bun):
        assert isinstance(bun.get_name(), str), 'Метод get_name вернул не строку'

    def test_get_bun_price_return_float(bun):
        assert isinstance(bun.get_price(), float), 'Метод get_price вернул не число с плавающей точкой'

