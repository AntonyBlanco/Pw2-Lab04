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
    for x in self.img:
      content.append(x)
    colPieza = ""
    colCasilla = ""  
    for y in content:
      i = 0
      while i < len(y):
        letra = y[i]
        if(letra == '.'):
          colPieza = '.'
          break
        if(letra == '@'):
          colPieza = '@'
          break
        if(letra == '_'):
          colCasilla = '_'
          break
        if(letra == '='):
          colCasilla = '='
          break
        i += 1
    colNeg1 = self._invColor(colPieza)
    colNeg2 = self._invColor(colCasilla)
    i = 0
    for z in content:
      content[i] = content[i].replace(colPieza,colNeg1)
      content[i] = content[i].replace(colCasilla,colNeg2)
      i += 1   
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
    while(n-1>0):
      count = 0
      for y in self.img:
        content[count] += y
        count = count+1
      n -= 1
    return Picture(content)    
    

  def verticalRepeat(self, n):
    content = self.img
    while(n-1>0):
      content = content + self.img
      n -= 1
    return Picture(content)
    

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

