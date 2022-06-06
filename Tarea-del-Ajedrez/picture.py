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
    c = []

    length = len(p.img)

    for x in range(length):
      c.append(self.img[x]+p.img[x])

    return Picture(c)

  def up(self, p):
    content = p.img + self.img
    return Picture(content)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    Content = []
    for x in p.img:
      Content.append(x)
    for x in range(len(p.img)):
      for y in range(len(p.img[x])):
        Content[x] = p.img[x].replace(" ",self.img[x][y])
    return Picture(Content)
  
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

