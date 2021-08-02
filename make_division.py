def make_division_by(n: float):
  """This closure returns a function that returns the division
  of an x number by n
  """
  def division(x: float)-> float :
    try:
      return x / n
    except ZeroDivisionError:
      print("You can't divide by 0")
  return division


def run():
  division_by_3 = make_division_by(3)
  print(division_by_3(18)) # Expected output is 6

  division_by_5 = make_division_by(5)
  print(division_by_5(100)) # Expected output is 20

  division_by_18 = make_division_by(18)
  print(division_by_18(54)) # Expected output is 3

  division_by_0 = make_division_by(0)
  print(division_by_0(100)) # Expected output is Exception


if __name__ == '__main__':
  run()