from importlib.resources import contents
from shelve import Shelf
from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    content = []
    for x in self.img:
      content.append(x[::-1])
    return Picture(content)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    content = []
    indice=len(self.img)-1
    for x in self.img:
      content.append(self.img[indice])
      indice=indice-1
    return Picture(content)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)
  #yo mero :v
  def join(self, p):
    count = 0
    content = []
    for x in self.img:
      content.append(x)
    for y in p.img:
      content[count] += y
      count = count+1
    return Picture(content)
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    

  def up(self, p):
    content = p.img + self.img
    return Picture(content)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

