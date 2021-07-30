def is_palindrome(string: str) -> bool:
  reversed = list(string)
  return True if reversed == reversed[::-1] else False


def run():
  print(is_palindrome("ana"))
  print(is_palindrome("no soy palindrome"))
  print(is_palindrome(1000))


if __name__ == "__main__":
  run()