#!/usr/bin/python
# -*- coding: cp850 -*-

from document import Document


class TestDocument(object):
    
    def __init__(self):
        self.document = Document()
        self.document.data = "05-abril-2012"
        self.document.data = "MILTON INOSTROZA AGUILERA"
        self.document.data = "AV. BLANCO ENCALADA 1771, DEPTO.: 308"
        self.document.data = "SANTIAGO     -      SANTIAGO"
        
        for i in range(30):
            self.document.data = str(i+1) + "    PISCO MISTRAL 45§ BOTELLA 750 cc.     $15.000.-"
        
        self.document.data = "$12.590.-"
        self.document.data = "$234.2342.-"
    
    def getDocument(self):
        return self.document