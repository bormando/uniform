import pytest
import requests


# noinspection SpellCheckingInspection
def pytest_generate_tests(metafunc):
    pairs = [
        "tBTCUSD",
        "tLTCUSD"
    ]
    metafunc.parametrize("pair", pairs)


class TestTradeGenerate:
    @pytest.mark.smoke
    def test_get_generated_trade_pairs(self, pair):
        request = requests.get(F"https://api-pub.bitfinex.com/v2/tickers?symbols={pair}")
        response = request.json()
        for item in response:
            name = item[0]
            assert name == pair, F"Got pair '{name}' instead of '{pair}"
            price = item[7]
            assert type(price) == float or type(price) == int, F"Wrong data type of last price"
