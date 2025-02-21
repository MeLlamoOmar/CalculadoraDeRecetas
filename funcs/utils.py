#Medidas de Articulos solidos: gramos(gr), Unidad(und), libras(lb)
#Medidas de articulos liquidos: onzas(oz), litros(lts), mililitros(ml)

from Receta import Receta
from Ingrediente import Ingrediente
from os import system
from sys import platform

def clearConsole():
  if platform == 'win32':
    system('cls')
  else:
    system('clear')

def ver(lista):
  for pos, el in enumerate(lista, start=1):
    print(f'{pos}) {el.nombre} \n')
    
def crear(opcion, lista):
  if opcion == 'receta':
    nombreReceta = input('Ingrese el nombre de la receta: ')
    lista.append(Receta(nombreReceta))
    print('''
    Para agregarle ingredientes a la receta vaya a la opcion de ver receta
    ''')
    input('Presione enter para continuar')
  elif opcion == 'ingrediente':
    medidas = ['gramos', 'unidad', 'libras', 'onzas', 'litros', 'mililitros']
    clearConsole()
    nombreIngrediente = input('Ingrese el nombre del ingrediente: ')
    clearConsole()
    print('''
    ----------Medidas------------------
    1) Gramos  2) Unidad  3) Libras
    4) Onzas   5) Litros  6) Mililitros
    ''')
    nombreMedida = int(input('Introduzca el numero de la opcion que desea: '))
    nombreMedida = medidas[nombreMedida - 1]
    clearConsole()
    pesoIngrediente = int(input('Introduzca el peso del articulo(Si la medida es unidad introduzca la cantidad de articulos): '))
    clearConsole()
    precioIngrediente = int(input('Introduzca el valor del articulo: '))
    lista.append(Ingrediente(nombreIngrediente, nombreMedida, pesoIngrediente, precioIngrediente))