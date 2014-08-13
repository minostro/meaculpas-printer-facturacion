#!/usr/bin/python
# -*- coding: cp850 -*-


from printer import Printer
from document import Document

guiaDespacho = Document()
guiaDespacho.data = "05-abril-2012"
guiaDespacho.data = "MILTON INOSTROZA AGUILERA"
guiaDespacho.data = "AV. BLANCO ENCALADA 1771, DEPTO.: 308"
guiaDespacho.data = "SANTIAGO     -      SANTIAGO"

for i in range(30):
    guiaDespacho.data = str(i+1) + "    PISCO MISTRAL 45¦ BOTELLA 750 cc.     $15.000.-"

guiaDespacho.data = "$12.590.-"
guiaDespacho.data = "$234.2342.-"

epson = Printer(0x04B8, 0x0005)
epson.printDocument(guiaDespacho)
