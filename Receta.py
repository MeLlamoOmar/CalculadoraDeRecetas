import os

class Receta:
  def __init__(self, nombre: str):
    self.__nombreReceta = nombre
    self.__costoReceta = 0
    self.__ingredientesReceta = []

  @property
  def nombre(self):
    return self.__nombreReceta
  
  @nombre.setter
  def nombre(self, nombreNuevo):
    self.__nombreReceta = nombreNuevo
    return self.__nombreReceta

  def mostrarReceta(self):
    os.system('cls')
    print(f'''
      Nombre de la Receta: {self.__nombreReceta}
      Numero de Ingredientes: {len(self.__ingredientesReceta)}

      Costo de la receta: {self.__costoReceta}
    ''')
    d = input('Desea ver los ingredientes(Y/N): ').upper()
    if (d == 'Y'):
      for i in range(len(self.__ingredientesReceta)):
        print(f'{i + 1}) {self.__ingredientesReceta[i].nombre} \n')
      input('Presione enter para continuar')
    elif (d == 'N'):
      return
    else:
      print('Por Favor ingrese una opcion valida')
      self.mostrarReceta()
  def agregarIngrediente(self, ingrediente):
    pesoReceta = int(input('Ingrese el peso utilizado en la receta (Si es por unidad ingrese la cantidad de unidades utilizadas): '))
    self.__costoReceta += self.calcularValor(ingrediente, pesoReceta)
  
  def calcularValor(self, ingrediente, pesoReceta):
    return ingrediente.precio / ingrediente.peso * pesoReceta
