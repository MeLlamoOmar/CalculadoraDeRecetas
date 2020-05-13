from Receta import Receta
from Ingrediente import Ingrediente
from funcs.menus import *
from funcs.utils import ver, crear
import os

def main():
  recetas = []
  ingredientes = [Ingrediente('Uva', 'Unidad', 0, 50)]

  loop = True
  while(loop):
    os.system('cls')
    desicionMenu = None
    desicionSubMenu = None
    desicionVer = None

    menuPrincipal()
    desicionMenu = int(input('Seleccione la opcion deseada: '))
    while(desicionMenu != None):
      os.system('cls')
      if (desicionMenu == 1):
        menuReceta()
        desicionSubMenu = int(input('Seleccione la opcion deseada: '))
        if desicionSubMenu == 1:
          if (len(recetas) == 0):
            print('No tiene ninguna receta creada \b')
            d = input('Desea crear una receta ahora?(Y/N): ').upper()
            if (d == 'Y'):
              desicionSubMenu = 2
            elif (d == 'N'):
              desicionSubMenu = None
            else:
              print('OK')
          else:
            ver(recetas)
            desicionVer = int(input('Seleccione la receta deseada: '))
            recetas[desicionVer - 1].mostrarReceta()
            input('Presione enter para continuar')
        elif desicionSubMenu == 2:
          os.system('cls')
          crear('receta', recetas)
          desicionSubMenu = None
        elif desicionSubMenu == 3:
          ver(recetas)
          d = int(input('Seleccione la receta deseada: '))
          recetas.pop(d - 1)
          print('Receta eliminada\n')
          input('Presione enter para continuar')
          desicionSubMenu = None
        elif desicionSubMenu == 4:
          if (len(recetas) == 0):
            print('No tiene ninguna receta creada \b')
            d = input('Desea crear una receta ahora?(Y/N): ').upper()
            if (d == 'Y'):
              desicionSubMenu = 2
            elif (d == 'N'):
              desicionSubMenu = None
            else:
              print('OK')
          else:
            masIngredientes = True
            ver(recetas)
            desicionVer = int(input('Seleccione la receta deseada: '))
            recetaSeleccionada = recetas[desicionVer - 1]
            while masIngredientes:
              ver(ingredientes)
              desicionVer = int(input('Seleccione el ingrediente deseado: '))
              recetaSeleccionada.agregarIngrediente(ingredientes[desicionVer - 1])
              d = input('Desea seguir agregando ingredientes?(Y/N): ').upper()
            if (d == 'Y'):
              pass
            elif (d == 'N'):
              masIngredientes = False
            else:
              print('OK')
            input('Presione enter para continuar')
        elif desicionSubMenu == 5:
          desicionSubMenu = None
          desicionMenu = None
        else:
          desicionSubMenu = None
          input('''
          Por Favor seleccione una opcion valida

          Presione enter para continuar
          ''')
      elif (desicionMenu == 2):
        menuIngrediente()
        desicionSubMenu = int(input('Seleccione la opcion deseada: '))
        if desicionSubMenu == 1:
          if (len(ingredientes) == 0):
            print('No tiene ningun ingrediente creado \b')
            d = input('Desea crear un ingrediente ahora?(Y/N): ').upper()
            if (d == 'Y'):
              desicionSubMenu = 2
            elif (d == 'N'):
              desicionSubMenu = None
            else:
              print('OK')
          else:
            ver(ingredientes)
            desicionVer = int(input('Seleccione la receta deseada: '))
            ingredientes[desicionVer - 1].mostrarIngrediente()
            input('Presione enter para continuar')
            desicionSubMenu = None
        elif desicionSubMenu == 2:
          os.system('cls')
          crear('ingrediente', ingredientes)
          desicionSubMenu = None
        elif desicionSubMenu == 3:
          ver(recetas)
          d = int(input('Seleccione el ingrediente deseado: '))
          ingredientes.pop(d - 1)
          print('Ingrediente eliminado\n')
          input('Presione enter para continuar')
          desicionSubMenu = None
        elif desicionSubMenu == 4:
          desicionSubMenu = None
          desicionMenu = None
      elif (desicionMenu == 3):
        desicionMenu = None
        loop = False
      else:
        print('Por favor elija una opcion valida')

main()