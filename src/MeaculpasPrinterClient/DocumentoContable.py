#!/usr/bin/python
# -*- coding: cp850 -*-
import sys
from printer.document import Document

class DocumentoContable(Document):
    
    def __init__(self, *args, **kwargs):
        super(DocumentoContable, self).__init__(*args, **kwargs)
        self.itemQuantity = 0

    def setHeader(self, numeroDocumento):
        self.setData("\n"*7)
        self.setData("%60s" %numeroDocumento)
        
    def setCliente(self, nombre, rut, direccion, giro, comuna, fechaDocumento):
        self.setData("\n"*8)
        nombre = self.getDecodedString(nombre)
        direccion = self.getDecodedString(direccion)
        giro = self.getDecodedString(giro)
        comuna = self.getDecodedString(comuna)
        rut = self.getDecodedString(rut)
        
        nombre = "     %-55s" % nombre
        nombre = nombre[:55]

        direccion = "     %-55s" % direccion
        direccion = direccion[:55]
        self.setData(nombre.upper() + " " + rut)
        self.setData(direccion.upper() + " " + giro.upper())
        self.setData("     " + comuna.upper() + "\n")
        self.setData(fechaDocumento)
        
    def itemSectionInit(self):
        self.setData("\n"*2)
        
    def setItem(self, codigo, descripcion, cantidad, precio_unitario, precio_total):
        self.itemQuantity += 1
        descripcion = self.getDecodedString(descripcion)
        codigo = "%13s" % str(codigo)
        codigo = codigo[:13]
        descripcion = " %-32s" %(descripcion)
        descripcion = descripcion[:32]
        cantidad = " %9s"%str(cantidad)
        precio_unitario = " %9s"%str(precio_unitario)
        precio_total = " %10s"%str(precio_total)
        self.setData(codigo + descripcion + cantidad + precio_unitario + precio_total)

    def setCantidadPalabras(self, cantidadPalabras):
        cantidadPalabras = self.getDecodedString(cantidadPalabras)
        self.setData("\n"* (22 - self.itemQuantity))
        self.setData(cantidadPalabras.upper() + " pesos.\n")
        
    def setTotales(self, totalNeto, iva, ila13, ila15, ila27, total):
        leftMargin = " "*48
        self.setData(leftMargin + "%28s" % totalNeto)
        self.setData(leftMargin + "    19%" + "%21s" % iva)
        self.setData(leftMargin + "13%" + "%25s" % ila13)
        self.setData(leftMargin + "15%" + "%25s" % ila15)
        self.setData(leftMargin + "27%" + "%25s" % ila27)
        self.setData(leftMargin + " "*3 + "%25s" % total)
    
    def getDecodedString(self, text):
        return text.encode('cp850') #'cp1252'

