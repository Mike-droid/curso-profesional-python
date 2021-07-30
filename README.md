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
