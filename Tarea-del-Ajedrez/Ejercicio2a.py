from interpreter import draw
from chessPictures import *
superior=knight.join(knight.negative())
inferior=knight.negative().join(knight)
draw(superior.under(inferior))
