#! /usr/bin/python
import argparse


SIZE = 8
QUEEN_MARKER = '*'
EMPTY_MARKER = '_'
SEPARATOR = ' '


def get_empty_board(size=SIZE, absence=EMPTY_MARKER):
  '''Returns an empty board of given size with absence markers.'''
  return [SEPARATOR.join(absence * size)] * size


def draw_board(board):
  '''Draws current board on terminal.'''
  for line in board:
    pass


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('size', help='Size of the board.', default=SIZE)
  args = parser.parse_args()


if __name__ == '__main__':
  main()
