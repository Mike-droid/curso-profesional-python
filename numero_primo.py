def es_primo(n: int) -> bool:
  if n < 2:
    return False
  else:
    divisors = [i for i in range(2, n) if n % i == 0]
    return len(divisors) == 0


def run():
  print(f'El número 3 es primo: {es_primo(3)}')
  print(f'El número 4 es primo: {es_primo(4)}')
  print(f'El número 5 es primo: {es_primo(5)}')
  print(f'El número 6 es primo: {es_primo(6)}')
  print(f'El número 7 es primo: {es_primo(7)}')
  print(f'El número 8 es primo: {es_primo(8)}')
  print(f'El número 9 es primo: {es_primo(9)}')
  print(f'El número 10 es primo: {es_primo(10)}')
  print(f'El número 11 es primo: {es_primo(11)}')


if __name__ == '__main__':
  run()