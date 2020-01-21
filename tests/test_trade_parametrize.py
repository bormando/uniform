import pytest
import requests


class TestTrade:
    @pytest.mark.smoke
    @pytest.mark.parametrize("pair", ["tBTCUSD", "tLTCUSD"])
    def test_get_parametrized_trade_pairs(self, pair):
        request = requests.get(F"https://api-pub.bitfinex.com/v2/tickers?symbols={pair}")
        response = request.json()
        for item in response:
            name = item[0]
            assert name == pair, F"Got pair '{name}' instead of '{pair}"
            price = item[7]
            assert type(price) == float or type(price) == int, F"Wrong data type of last price"
