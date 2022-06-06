from interpreter import draw
from chessPictures import *

squareNeg = square.negative()
peonNeg = pawn.negative()

Negras = [rock,knight,bishop,queen,king,bishop,knight,rock]
i = 0
while i < len(Negras):
    Negras[i] = Negras[i].negative()
    i += 1
i = 0
j = 0
while i < len(Negras):
    if j == 0:
        Negras[i]= square.under(Negras[i])
        j += 1
    elif j == 1:
        Negras[i]= squareNeg.under(Negras[i])
        j -= 1
    i += 1
i = 0 
filaNeg1 = Negras[i]
while i < len(Negras)-1:
    filaNeg1 = filaNeg1.join(Negras[i+1])
    i += 1
i = 0
filaNeg2 = squareNeg.under(peonNeg)
filaNeg2 = filaNeg2.join(square.under(peonNeg))
filaNeg2 = filaNeg2.horizontalRepeat(3)

Blancas = [rock,knight,bishop,queen,king,bishop,knight,rock]
i = 0
j = 0
while i < len(Blancas):
    if j == 0:
        Blancas[i]= squareNeg.under(Blancas[i])
        j += 1
    elif j == 1:
        Blancas[i]= square.under(Blancas[i])
        j -= 1
    i += 1
i = 0
filaBla1 = Blancas[i]
while i < len(Blancas)-1:
    filaBla1 = filaBla1.join(Blancas[i+1])
    i += 1
filaBla2 = square.under(pawn)
filaBla2 = filaBla2.join(squareNeg.under(pawn))
filaBla2 = filaBla2.horizontalRepeat(3)

cuadrados = squareNeg.join(square)
cuadrados = cuadrados.up(square.join(squareNeg))
cuadrados = cuadrados.horizontalRepeat(3)
cuadrados = cuadrados.verticalRepeat(1)

filas = [filaBla1,filaBla2,cuadrados,filaNeg2,filaNeg1]
i = 0
tablero = filas[i]
while i < len(filas)-1:
    tablero = tablero.up(filas[i+1])
    i += 1
draw(tablero)