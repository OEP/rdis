"""
__graph_Interface.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Interface(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 118, 72
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([300.0, 161.0, 340.0, 200.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf59 = GraphicalForm(drawing, h, "gf59")
        self.graphForms.append(self.gf59)

        h = drawing.create_line(self.translate([280.0, 181.0, 301.0, 181.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf64 = GraphicalForm(drawing, h, "gf64")
        self.graphForms.append(self.gf64)

        h = drawing.create_line(self.translate([341.0, 182.0, 360.0, 182.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf65 = GraphicalForm(drawing, h, "gf65")
        self.graphForms.append(self.gf65)

        h = drawing.create_oval(self.translate([261.0, 173.0, 278.0, 188.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf66 = GraphicalForm(drawing, h, "gf66")
        self.graphForms.append(self.gf66)

        h = drawing.create_oval(self.translate([360.0, 174.0, 375.0, 188.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf67 = GraphicalForm(drawing, h, "gf67")
        self.graphForms.append(self.gf67)

        h = drawing.create_oval(self.translate([272.0, 182.0, 272.0, 182.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([369.0, 180.0, 369.0, 180.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='FreeSerif', size=18, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([320.0, 180.0, 320.0, 26.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'I', width = '0', justify= 'left', stipple='' )
        self.gf62 = GraphicalForm(drawing, h, 'gf62', fontObject=font)
        self.graphForms.append(self.gf62)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([320.0, 220.0, 320.0, -27.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf70 = GraphicalForm(drawing, h, 'gf70', fontObject=font)
        self.graphForms.append(self.gf70)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Interface
