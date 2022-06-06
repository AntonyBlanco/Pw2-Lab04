from interpreter import draw
from chessPictures import *
filaA=square.join(square.negative()).horizontalRepeat(4)
filaB=square.negative().join(square).horizontalRepeat(4)
union=filaA.under(filaB)
draw(union.verticalRepeat(2))