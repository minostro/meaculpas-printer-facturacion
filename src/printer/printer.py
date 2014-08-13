#!/usr/bin/python
# -*- coding: cp850 -*-

import usb.core

class Printer(object):
    
    def __init__(self, vendorId, productId):
        self.vendorId = vendorId
        self.productId = productId
        self.device = None
        self.endPoint = 0x01
        self.interface = 0
        self.initializeDevice()
        
    def initializeDevice(self):
        self.device = usb.core.find(
            idVendor=self.vendorId,
            idProduct=self.productId
        )
        
        if self.device is None:
            raise ValueError('Device not found')

        self.device.set_configuration()

    def initializePrinter(self):
        self.device.write(
            self.endPoint,
            '\x1b\x40',
            self.interface
        )  

    def setCharacterWidth(self, characterWidth):
        self.device.write(
            self.endPoint,
            '\x1b'+characterWidth,
            self.interface
        )

    def setMargins(self, left, right, bottom):
        self.setLeftMargin(left)
        self.setRightMargin(right)
        self.setBottomMargin(bottom)
    
    def setLeftMargin(self, leftMargin):
        self.device.write(
            self.endPoint,
            '\x1b\x6c'+leftMargin,
            self.interface
        )

    def setRightMargin(self, rightMargin):
        self.device.write(
            self.endPoint,
            '\x1b\x51'+rightMargin,
            self.interface
        )
    
    def setBottomMargin(self, bottomMargin):
        self.device.write(
            self.endPoint,
            '\x1b\x4e'+bottomMargin,
            self.interface
        )

    def setLineSpacing(self, lineSpacing):
        self.device.write(
            self.endPoint,
            '\x1b'+lineSpacing,
            self.interface
        )

    def writeDocument(self, aData):
        for data in aData:
            self.device.write(
                self.endPoint,
                data + "\n",
                self.interface
            )
        
    def finishDocument(self):
        self.device.write(
            self.endPoint,
            '\x0c',
            self.interface
        )        

    def printDocument(self, document):
        self.initializePrinter()
        self.setCharacterWidth(document.characterWidth)
        self.setMargins(
            document.leftMargin,
            document.rightMargin,
            document.bottomMargin
        )
        self.setLineSpacing(document.lineSpacing)
        self.writeDocument(document.data)
        self.finishDocument()
