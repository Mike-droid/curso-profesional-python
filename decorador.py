def decorador(func):
  def envoltura(): #wrapper
    print("Esto se añade a mi función original")
    func()
  return envoltura


@decorador
def saludo():
  print("Hola")


saludo() # Esto se añade a mi función original - Hola