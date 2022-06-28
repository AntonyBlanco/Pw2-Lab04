from interpreter import draw
from chessPictures import *

linea = square.join(square.negative())

linea = linea.horizontalRepeat(3)

draw(linea)