import time

def fibo_gen():
  n1 = 0
  n2 = 1
  counter = 0
  sumatory = 0
  limit = int(input("Limit of Fibonacci: "))
  while sumatory < limit:
    sumatory = n1 + n2
    if counter == 0:
      yield n1
    elif counter == 1:
      yield n2
    else:
      aux = n1 + n2
      n1, n2 = n2, aux
      yield aux

    counter += 1


if __name__ == "__main__":
  fibonacci = fibo_gen()
  for element in fibonacci:
    print(element)
    time.sleep(1)