from interpreter import draw
from chessPictures import *

cabBlanVol = knight.verticalMirror()
cabNegrVol = knight.negative().verticalMirror()
fil1 = knight.join(knight.negative())
fil2 = cabNegrVol.join(cabBlanVol)
caballos = fil2.up(fil1)
draw(caballos)
