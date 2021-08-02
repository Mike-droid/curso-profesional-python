from datetime import datetime

def execution_time(func):
  def wrapper(*args, **kwargs):
    initial_time = datetime.now()
    func(*args, **kwargs)
    final_time = datetime.now()
    time_elapsed = final_time - initial_time
    print(f'It has passed {time_elapsed.total_seconds()} seconds')
  return wrapper


@execution_time
def random_func():
  for _ in range(1, 1000000):
    pass


@execution_time
def suma(a: int, b: int)-> int:
  print(a+b)


@execution_time
def saludo(nombre = "Miguel")-> str:
  print(f'Hola {nombre}')

def run():
  random_func()
  suma(3,6)
  saludo()
  saludo('Jose')


if __name__ == '__main__':
  run()