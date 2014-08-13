#!/usr/bin/python
# -*- coding: cp850 -*-

class Document(object):

    def __init__(self,
                 characterWidth='\x05',
                 leftMargin='\x02',
                 rightMargin='\x85',
                 bottomMargin='\x06',
                 lineSpacing='\x02'):
        self.__data = []
        self.__characterWidth = characterWidth
        self.__leftMargin = leftMargin
        self.__rightMargin = rightMargin
        self.__bottomMargin = bottomMargin
        self.__lineSpacing= lineSpacing

    def setData(self, value):
        self.__data.append(value)


    def getData(self):
        return self.__data


    def getCharacterWidth(self):
        return self.__characterWidth


    def getLeftMargin(self):
        return self.__leftMargin


    def getRightMargin(self):
        return self.__rightMargin


    def getBottomMargin(self):
        return self.__bottomMargin


    def getLineSpacing(self):
        return self.__lineSpacing
    
    
    data = property(
        getData, 
        setData, 
        None,
        "returns a list which represent the whole document data"
    )

    characterWidth = property(
        getCharacterWidth,
        None,
        None,
        "gives the letter size which will be used in the document"
    )

    leftMargin = property(
        getLeftMargin,
        None,
        None,
        "gives the left margin"
    )
    
    rightMargin = property(
        getRightMargin,
        None,
        None,
        "gives the right margin"
    )

    bottomMargin = property(
        getBottomMargin,
        None,
        None,
        "gives bottom margin"
    )
    
    lineSpacing = property(
        getLineSpacing,
        None,
        None,
        "gives the line spacing"
    )
