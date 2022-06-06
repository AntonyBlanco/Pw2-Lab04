from interpreter import draw
from chessPictures import *
Cuadrados = square.join(square.negative())
Fila1 = Cuadrados.horizontalRepeat(3)
Cuadrados = square.negative().join(square)
Fila2 = Cuadrados.horizontalRepeat(3)
Filas = Fila2.up(Fila1)
Filas = Filas.verticalRepeat(1)
draw(Filas)
