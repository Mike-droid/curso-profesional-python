# hola 3 -> HolaHolaHola
# Facundo 2 -> FacundoFacundo

def make_repeater_of(n: int):
  def repeater(string: str):
    assert type(string) == str, "Sólo puedes utilizar cadenas"
    return string * n
  return repeater

def run():
  repeat_5 = make_repeater_of(5)
  print(repeat_5("Hola"))
  repeat_10 = make_repeater_of(10)
  print(repeat_10("Platzi"))

if __name__ == '__main__':
  run()