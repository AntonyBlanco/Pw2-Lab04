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
    content = []
    x = 0
    while x < len(self.img):
      content.append("")
      y = 0
      while y < len(self.img[x]):
        content[x] += self._invColor(self.img[x][y])
        y += 1
      x += 1
    return Picture(content)   
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
    content = self.img + p.img
    return Picture(content)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    content=[]
    for x in self.img:
      content.append("")
    count=0
    while(n>0): 
      content[count]+=self.img[count]
      count += 1
      if count==len(self.img):
        print("len: ",len(self.img))
        n=n-1
        count=0
    return Picture(content)  

  def verticalRepeat(self, n):
    content=[]
    for x in self.img:
      content.append(x)
    while(n-1>0): 
      content+=self.img
      n=n-1
    return Picture(content)   

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

