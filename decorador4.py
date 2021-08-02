def make_pokemon_stronger(func):
  def wrapper(*args, **kwargs):
    func(*args, **kwargs)
    print(f'{args[0]} has now a strength of {args[1] + 100} 💪 and speed of {args[2] + 100} 🤙 ❗')
  return wrapper


@make_pokemon_stronger
def pokemon_name_stats(pokemon_name: str, strength: int, speed: int)-> str:
  print(f'{pokemon_name} has a strength of {strength} points and speed of {speed}')


def run():
  pokemon_name_stats('Pikachu', 20, 100)
  pokemon_name_stats('Charmander', 35, 40)


if __name__ == '__main__':
  run()