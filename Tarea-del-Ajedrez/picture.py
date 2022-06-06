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
    return Picture(None)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

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

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    content = []
    for x in self.img:
      content.append(x)
    while(n > 0):
      count = 0
      for y in self.img:
        content[count] += y
        count += 1
      n -= 1
    return Picture(content)    
    

  def verticalRepeat(self, n):
    content = []
    for x in self.img:
      content.append(x)
    while(n > 0):
      content += self.img
      n -= 1
    return Picture(content)
    

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

