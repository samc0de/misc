# Determine buying and selling a stock to maximize profit over a given range
# of dates. Conditions: Sell should be after buy, both occur at the start of
# day.
# Note: If accessing next element is problematic, previous element can be
# remembered.
# Note: Works with non zero values only.
from __future__ import print_function
import sys


def stock_broker(values):
    buy_at = sell_at = possible_buy = int(values[0])
    diff, buy_index, possible_buy_index = 0, 0, 0
    length = len(values)
    for index, current_value in enumerate(values[:-1]):
        current_value = int(current_value)
        next_val = int(values[index + 1])
        if next_val > current_value:
            if current_value < buy_at:
                possible_buy = current_value
                possible_buy_index = index
                if not diff:
                    buy_at = current_value
                    buy_index = index
            if next_val > sell_at:
                sell_at = next_val
                sell_index = index + 1
                if possible_buy_index > buy_index:
                    buy_at = possible_buy
                    buy_index = possible_buy_index
                diff = sell_at - buy_at
            if possible_buy and next_val - possible_buy > diff:
                buy_at = possible_buy
                buy_index = possible_buy_index
                sell_at = next_val
                sell_index = index + 1
                diff = sell_at - buy_at
    if diff:
        msg = ('Buy at price {buy_at} (day{buy_day}), and sell at {sell_at}'
                '(day{sell_day}).').format(
                        buy_at=buy_at, sell_at=sell_at, buy_day=buy_index + 1,
                        sell_day=sell_index + 1)
        print(msg)



if __name__ == '__main__':
    stock_broker(sys.argv[1:])
