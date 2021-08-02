# Curso profesional de Python

## Introducción

### ¿Qué necesitas saber para tomar el curso?

- [Curso básico de Python](https://platzi.com/clases/python/)
- [Curso profesinal de Git y Github](https://platzi.com/clases/git-github/)
- [Curso intermedio de Python](https://platzi.com/clases/python-intermedio/)
- [Curso de POO](https://platzi.com/clases/oop/)

### ¿Cómo funciona Python?

- Compilado; ejemplo C++

```cpp
void main() {
  cout<<"Hola mundo";
}
```

Esto se transforma en binario.

- Interpretado; ejemplo Python

```python
def my_func():
  print("Hola mundo")
```

Esto es leido por un intérprete y luego por una máquina virtual. Esta puede ser ejecutada en diferentes sistemas operativos.

¿Los lenguajes interpretados son más lentos? Todos dicen que sí, pero no es importante hasta que intentes codificar un programa para Dios.

Python tiene algo llamado "Garbage Collector" que elimina las variables que no se usan.

¿Qué es la carpeta __pycache__? Es el bytecode de Python.

### Cómo organizar las carpetas de tus proyectos

#### Módulo

Un módulo es cualquier archivo de Python (o sea que termina con `.py`). Generalmente, contiene código que puedes reutilizar.

#### Paquete

Una carpeta que contiene módulos. Siempre posee el archivo `__init__.py`. (Se lee dunder init doy py).

| Paquetes |        |
| -------- | ------ |
| Módulo   | Módulo |
| Módulo   | Módulo |
| Módulo   | Módulo |

| exploracion_espacial |                  |
| -------------------- | ---------------- |
| `nave.py`            | `destino.py`     |
| `plataforma.py`      | `lanzamiento.py` |
| `tests.py`           | `validacion.py`  |

Estructura de proyecto:

- README -> Explica cómo funciona el proyecto
- .gitignore -> Cosas que no se subirán al repo
- venv -> entorno virtual de Python
- exploracion_espacial -> Paquete, dentro de él, los módulos
  - `__init__.py`
  - `nave.py`
  - `destino.py`
  - `plataforma.py`
  - `lanzamiento.py`
  - `tests.py`
  - `validacion.py`

Esta regla no está tallada en piedra. Depende del proyecto y el Framework que uses.

## Static Typing

### ¿Qué son los tipados?

- Estático -> Levantan los errores de tipo en tiempo de compilación - El programa no se ejecuta hasta que el error se resuelva
- Dinámico -> Levantan el error el tiempo de ejecución - Cuando llegue al error, lo va a indicar
- Débil
- Fuerte

Un lenguaje va a tener un tipado diferente dependiendo de cómo trate a los tipos.

- Strong & Dinamic 💪💫 : Python, Ruby, Erlang
- Strong & Static 💪🗻: Java, C#, Scala
- Weak & Dynamic 😫💫 : JavaScript, PHP, Perl
- Weak & Static 😫🗻 : C, C++

Estático:

```java
// java
String str = "hello";
str = 5; // Error
```

Dinámico:

```python
# python
str = "Hello"
str = 5 # No hay problema :)
```

```python
# python
x = 1
y = "2"
z = x + y # Error
```

```javascript
// javascript
const x = 1
const y = "2"
const z = x + y // "12" - JS es raro 😅
```

```php
<?php
$str = 5 + "5"; //10 - PHP es raro 😅 (hace lo contrario a JS)
?>
```

Nota: El tipado dinámico es **peligroso**.

### Tipado estático en Python

[Documentación oficial del tipado estático en Python](https://docs.python.org/3/library/typing.html)

El tipado estático nos hará evitar errores de tipado antes de que el programa se ejecute.

```python
a: int = 5
print(a) # 5

b: str = 'Hola'
print(b) # Hola

c: bool = True
print(c) # True
```

Esta sintaxís está disponible desde la versión 3.6 de Python.

```python
def suma(a: int, b: int) -> int:
  return a + b

print(suma(1,2)) # 3
```

```python
def suma(a: int, b: int) -> int:
  return a + b

print(suma('1','2')) # 12 😅
```

Usando tipado en estructuras de datos. Desde la versión 3.6 debemos importar librerias.

```python
from typing import Dict, List

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
  'argentina': 1,
  'mexico': 34,
  'colombia': 45,
}

countries: List[Dict[str,str]] = [
  {
    'name': 'Argentina',
    'people': '450000', # Cuatrocientos cincuenta mil
  },
  {
    'name': 'México',
    'people': '90000000', # Noventa millones
  },
  {
    'name': 'Colombia',
    'people': '99999999999', #novecientos noventa y nueve mil millones novecientos mil novecientos noventa y nueve
  }
]
```

```python
from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)
```

```python
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

#Una variable que es de tipo CoordinatesType 🤯
coordinates: CoordinatesType = [
  {
    'coord1': (1,2),
    'coord2': (3,5),
  },
  {
    'coord1': (0,1),
    'coord2': (2,5),
  },
]
```

Ventajas de esto: *claridad del código*.

### Practicando el tipado estático

- Crear entorno virtual en Windows: `py -m venv venv`
- Crear entonro virutal en Unix: `python3 -m venv venv`

Activar entorno virtual en Unix: `source venv/bin/activate`

Descargamos (con el entorno virtual encendido) `pip install mypy`

❗ Comando importante: `mypy palindrome.py --check-untyped-defs` Nos dará en consola los errores que podemos entender sobre los tipados.

## Conceptos avanzados de funciones

### Scope: alcance de las variables

Una variable solo está disponible dentro de la región donde fue creada.

```python
# Local Scope

def my_func():
  y = 5 #La variable solo está disponible en esta función
  print(y)

my_func() # 5
```

---

```python
# Global Scope
y = 5

def my_func():
  print(y)

def my_other_func():
  print(y)

my_func() # 5
my_other_func() # 5
```

---

```python
z = 5 # global

def my_func():
  z = 3 # z local
  print(z)

my_func() # 3 - local

print(z) # 5 - global
```

---

```python
z = 5

def my_func():
  z = 3

  def my_other_func():
    z = 2
    print(z)

  my_other_func() # 2

  print(z) # 3

my_func()

print(z) # 5
```

### Closures

#### Nested Functions - Funciones anidadas

```python
def main():
  a = 1

  def nested():
    print(a)

  nested() # 1

main()
```

---

closure:

```python
def main():
  a = 1

  def nested():
    print(a)

  return nested

my_func = main()
my_func() # 1
```

Quiere decir que una variable que está en un scope superior, es recordada por una función de scope inferior.

---

```python
def main():
  a = 1

  def nested():
    print(a)

  return nested

my_func = main()
my_func() # 1

del(main) # borramos la función

my_func() # 1 🤯 debido a la nested function
```

Reglas para encontrar un closure:

- Debemos tener una nested function.
- La nested function debe referenciar un valor de un scope superior.
- La función que envuelve a la nested function debe retornarla también.

```python
def make_multiplier(x):

  def multiplier(n):
    return x * n

  return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3)) # => 10 * 3 = 30
print(times4(5)) # => 4 * 5 = 20
print(times10(times4(2))) # => 4 * 2 * 10 = 80
```

¿Dónde aparecen los closures?

1. Clase con solo 1 método
2. Cuando trabajamos con decoradores

### Programando closures

Código de clase 'clores.py':

```python
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
```

Reto 'make_division.py':

```python
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
```

### Decoradores

El concepto más avanzados de funciones.

Un decorador es un closure que tiene una funcionalidad adicional.

**Concepto de dcorador:** Función que recibe como parámetro otra función, le añade cosas, y retorna una función diferente.

Una función que le añade super poderes a la función.

Ejemplo de decorador:

```python
def decorador(func):
  def envoltura(): #wrapper
    print("Esto se añade a mi función original")
    func()
  return envoltura


def saludo():
  print("Hola")


saludo()
# Output: Hola

nuevoSaludo = decorador(saludo)
saludo()
# Output: Esto se añade a mi función original - Hola
```

Azúcar sintáctica: Cuando un código está embellezido para poder leerlo de una forma más estética.

Sugar syntax:

```python
def decorador(func):
  def envoltura(): #wrapper
    print("Esto se añade a mi función original")
    func()
  return envoltura


@decorador
def saludo():
  print("Hola")


saludo()
```

Otro ejemplo:

```python
def mayusculas(func):
  def envoltura(texto):
    return func(texto).upper()
  return envoltura


@mayusculas
def mensaje(nombre):
  return f'{nombre}, recibiste un mensaje'


print(mensaje('Cesar'))
```

### Programando decoradores

Usamos `*args y **kwargs` para que los decoradores puedan decorar a las funciones sin importar los parametros que reciban.

- *args: Argumentos posicionales
- *kwargs: Argumentos nombrados

`*` -> Operador de desestructuración de Python.

Ejemplo de decorador:

```python
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
```

Reto libre:

```python
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
```

## Estructuras de datos avanzadas

### Iteradores

Antes de entender qué son los iteradores, primero debemos entender a los iterables.

Son todos aquellos objetos que podemos recorrer en un ciclo. Son aquellas estructuras de datos divisibles en elementos únicos que yo puedo recorrer en un ciclo.

Pero en Python las cosas no son así. Los iterables se convierten en iteradores.

Ejemplo:

```python
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

print(next(my_iter))

# Cuando no quedan datos, la excepción StopIteration es elevada
```

---

```python
# Creando un iterador

my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador

while True: #ciclo infinito
  try:
    element = next(my_iter)
    print(element)
  except StopIteration:
    break
```

**Momento impactante:** El ciclo "for" dentro de Python, no existe. Es un while con StopIteration. 🤯🤯🤯

```python
my_list = [1,2,3,4,5]

for element in my_list:
  print(element)
```

---

`evenNumbers.py`:

```python
class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  #* Constructor de la clase
  def __init__(self, max = None): #self hace referencia al objeto futuro que voy a crear con esta clase
    self.max = max


  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0 #Primer número par
    #* Convertir un iterable en un iterador
    return self

  # Método para tener la función "next" de Python
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration
```

Ventajas de usar iteradores:

1. Nos ahorra recursos.
2. Ocupan poca memoria.

### La sucesión de Fibonacci

[Sucesión de Fibonacci](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci)

Reto:

```python
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
```

### Generadores

Sugar syntax de los iteradores. Los generadores son funciones que guardan un estado. Es un iterador escrito de forma más simple.

```python
def my_gen():

  """un ejemplo de generadores"""

  print('Hello world!')
  n = 0
  yield n # es exactamente lo mismo que return pero detiene la función, cuando se vuelva a llamar a la función, seguirá desde donde se quedó

  print('Hello heaven!')
  n = 1
  yield n

  print('Hello hell!')
  n = 2
  yield n


a = my_gen()
print(next(a)) # Hello world!
print(next(a)) # Hello heaven!
print(next(a)) # Hello hell!
print(next(a)) StopIteration
```

Ahora veremos un **generator expression** (es como list comprehension pero mucho mejor, porque podemos manejar mucha cantidad
de información sin tener problemas de rendimiento):

```python
#Generator expression

my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #List comprehension
my_second_gen = ()x*2 for x in my_list]) #Generator expression
```

### Mejorando nuestra sucesión de Fibonacci

Reto, usar generadores en Fibonacci:

```python
import time

def fibo_gen():
  n1 = 0
  n2 = 1
  counter = 0
  sumatory = 0
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
```

### Sets

Los sets (conjuntos) son una colección desordenada de elementos únicos e inmutables.

```python
my_set = {3, 4, 5}
print(f"my_set = {my_set}")

my_set2 = {"Hola",23.3, False, True}
print(f"my_set = {my_set2}")

my_set3 = {3, 3, 2} # Python automáticamente elimina los duplicados
print(f"my_set = {my_set3}")

my_set4 = {[1,2,3] , 4} #Error
print(f"my_set = {my_set4}")
```

---

```python
empty_set = {} # Dictionary
empty_set = set() # Set
```

---

```python
my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set) # {1, 2, 3, 4, 5}

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2) # {'Hola', 1}
```

---

Añadiendo y quitando elementos a los sets:

```python
my_set = {1, 2, 3}

# Añadir un elemento
my_set.add(4)

# Añadir varios elementos
my_set.update([1, 2, 5])
my_set.update((1, 7, 2), {6, 8})

# Borrar un elemento existente
my_set.discard(1)
my_set.remove(2)

# Borrar un elemento inexistente
my_set.discard(10) # No hay problema
my_set.remove(10) # Error, ese elemento no existe

# borrar elemento aleatorio
my_set.pop()

# Borrar todos los elementos
my_set.clear()
```

### Operaciones con sets

- Unión: Combinar todos los elementos de los sets (pero no se toman en cuenta los repetidos).
- Intersección: Combinar todos los elementos que tengan en común.
- Diferencia: Tomar 2 sets y de 1 quitar todos los elementos que tiene el otro.
- Diferencia simétrica: Tomar los elementos de los sets sin los que están en común.

### Eliminando los repetidos de una lista

Reto:

```python
import random

def remove_duplicates(some_list: list) -> list:
  return list(set(some_list))


def run():
  random_list = [random.randint(0, 10) for i in range(10)]
  print(f'Lista original: {random_list}')
  print(f'Elementos duplicados eliminados: {remove_duplicates(random_list)}')


if __name__ == '__main__':
  run()
```

## Bonus

### Manejo de fechas

`datetime` es un módulo de manejo de fechas.

```python
import datetime

my_time = datetime.datetime.now() # hora local de mi PC u hora universal
my_date = datetime.date.today() # fecha actual

my_day = datetime.date.today()

print(my_time)
print(my_date)

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')
```

Tabla de códigos de formato para fechas y horas(los más importantes):

| Formato  | Código |
| -------- | ------ |
| Año      | %Y     |
| Mes      | %m     |
| Día      | %d     |
| Hora     | %H     |
| Minutos  | %M     |
| Segundos | %S     |

```python
from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')
```

### Time zones

`pytz` es un módulo para manejar las timezones. Se debe descargar con pip. `pip install pytz` **Recuerda hacerlo en el entorno virtual**.

[Base de datos de timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
