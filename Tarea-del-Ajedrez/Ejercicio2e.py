from interpreter import draw
from chessPictures import *

Cuadrados = square.negative().join(square)
Cuadrados = Cuadrados.horizontalRepeat(3)
draw(Cuadrados)