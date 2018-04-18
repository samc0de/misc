"""Check differences in different algos for checking if a string is palindrome.

Mainly used %timeit from ipython shell for this.
"""


def palindrome(string):
  """Loop approach."""
  for idx in range(len(string) / 2):
    if string[idx] != string[-idx - 1]:
      return False
  return True


def palindrome_seq_matcher(string):
  length = len(string)
  # This does not work for all the cases!!!
  return string[:length / 2 + 1] == string[length:(length+1) / 2 - 2:-1]


# Interestingly both show pretty much the same efficiency.
# The first approach uses short circuiting, so it seems that the string matching
# uses it as well.
# The string matching version doesn't work! Fails for 'a' and 'aa'.

