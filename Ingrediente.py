class Ingrediente:
  def __init__(self, nombre, medida, peso, precio):
    self.__nombreIngrediente = nombre
    self.__nombreMedida = medida
    self.__pesoIngrediente = peso
    self.__precioIngrediente = precio

  @property
  def nombre(self):
    return self.__nombreIngrediente

  @nombre.setter
  def nombre(self, nombreNuevo):
    self.__nombreIngrediente = nombreNuevo
    return self.__nombreIngrediente

  @property
  def medida(self):
    return self.__nombreMedida

  @medida.setter
  def medida(self, nombreMedidaNuevo):
    self.__nombreMedida = nombreMedidaNuevo
    return self.__nombreMedida

  @property
  def peso(self):
    return self.__pesoIngrediente

  @peso.setter
  def peso(self, pesoNuevo):
    self.__pesoIngrediente = pesoNuevo
    return self.__pesoIngrediente

  @property
  def precio(self):
    return self.__precioIngrediente

  @precio.setter
  def precio(self, precioNuevo):
    self.__precioIngrediente = precioNuevo
    return self.__precioIngrediente

  def mostrarIngrediente(self):
    print(f'''
      Nombre Ingrediente: {self.__nombreIngrediente}
      Medida del ingrediente: {self.__nombreMedida}
      Peso del Ingrediente: {self.__pesoIngrediente}
      Precio del Ingrediente: {self.__precioIngrediente}
    ''')