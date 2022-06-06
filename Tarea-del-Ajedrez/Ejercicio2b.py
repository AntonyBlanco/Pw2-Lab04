from interpreter import draw
from chessPictures import *

row = knight.join(knight.negative())

ejercicio2 = (row.verticalMirror()).up(row)

draw(ejercicio2)
