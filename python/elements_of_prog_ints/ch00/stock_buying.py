# Determine buying and selling a stock to maximize profit over a given range
# of dates. Conditions: Sell should be after buy, both occur at the start of
# day.
from __future__ import print_function
import click
import sys


def stock_broker(values):
    buy_at, sell_at, diff = None, None, 0
    length = len(values)
    for index, current_value in enumerate(values):
        if index < length - 1:
            next_val = values[index + 1]
            if next_val >= current_value:
                # Delay buying as much as possible so <=.
                if buy_at is None or current_value <= buy_at:
                    buy_at = current_value
                    buy_index = index
                # Sell as soon as possible so >.
                if sell_at is None or next_val > sell_at:
                    sell_at = next_val
                    sell_index = index + 1
    if buy_at is not None:
        msg = ('Buy at price {buy_at} (day{buy_day}), and sell at {sell_at}'
                '(day{sell_day}).').format(
                        buy_at=buy_at, sell_at=sell_at, buy_day=buy_index + 1,
                        sell_day=sell_index + 1)
        print(msg)



if __name__ == '__main__':
    stock_broker(sys.argv[1:])
