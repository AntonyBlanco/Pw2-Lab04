from interpreter import draw
from chessPictures import *
fil1 = knight.join(knight.negative())
fil2 = knight.negative().join(knight)
caballos = fil2.up(fil1)
draw(caballos)

