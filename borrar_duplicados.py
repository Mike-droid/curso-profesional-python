import random

def remove_duplicates(some_list: list) -> list:
  return list(set(some_list))


def run():
  random_list = [random.randint(0, 10) for i in range(10)]
  print(f'Lista original: {random_list}')
  print(f'Elementos duplicados eliminados: {remove_duplicates(random_list)}')


if __name__ == '__main__':
  run()