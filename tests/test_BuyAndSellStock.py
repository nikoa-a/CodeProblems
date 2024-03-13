import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from problems.BuyAndSellStock.BuyAndSellStock import BuyAndSellStock

def test_buy_and_sell_stock():
    bass_instance = BuyAndSellStock()

    # Test case 1
    prices = [7,1,5,3,6,4]
    expected = 5
    assert bass_instance.buyAndSellStock(prices) == expected

    # Test case 2
    prices = [7,6,4,3,1]
    expected = 0
    assert bass_instance.buyAndSellStock(prices) == expected
    