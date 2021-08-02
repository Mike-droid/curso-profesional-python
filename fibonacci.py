import time

class FiboIter():

  def __init__(self, max_number: int):
    self.max_number = max_number


  def __iter__(self):
    self.n1 = 0
    self.n2 = 1
    self.counter = 0
    self.sum = 0
    return self


  def __next__(self):
    if self.counter == 0:
      self.counter += 1
      return self.n1
    elif self.counter == 1:
      self.counter += 1
      return self.n2
    else:
      while self.sum < self.max_number:
        self.sum = self.n1 + self.n2
        self.n1, self.n2 = self.n2, self.sum # swapping in python
        self.counter += 1
        return self.sum
      if self.sum >= self.max_number:
        raise StopIteration


if __name__ == "__main__":
  fibonacci = FiboIter(21)
  for element in fibonacci:
    print(element)
    time.sleep(1) #* pause for 1 second