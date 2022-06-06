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

  def verticalMirror(self, ):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    length = len(self.img)
    for x in range(length):
      horizontal.append(self.img[length-x-1])
    return Picture(horizontal)

  def negative(self):
    c = []

    for x in range(len(self.img)):
      c.append("")
      for y in range(len(self.img[x])):
        c[x] = c[x] + self._invColor(self.img[x][y])

    return Picture(c)

  def join(self, p):
    c = []

    length = len(p.img)

    for x in range(length):
      c.append(self.img[x]+p.img[x])

    return Picture(c)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    self.img = p.img
    return Picture(self.img)
  
  def horizontalRepeat(self, n):
    figura = []
    for x in range(len(self.img)):
      figura.append(self.img[x])

    c = []

    i=0
    while i<n: 
      for x in range(len(self.img)):
        if i == n-1:
          c.append(self.img[x]+figura[x])
        else:
          self.img[x] = self.img[x]+figura[x]
      i=i+1

    return Picture(c)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

