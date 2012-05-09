"""
__graph_DomainInterface.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_DomainInterface(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 144, 91
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
        h = drawing.create_oval(self.translate([185.0, 154.0, 185.0, 154.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([316.0, 152.0, 316.0, 152.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([220.0, 121.0, 282.0, 182.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf132 = GraphicalForm(drawing, h, "gf132")
        self.graphForms.append(self.gf132)

        h = drawing.create_line(self.translate([221.0, 152.0, 194.0, 152.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf134 = GraphicalForm(drawing, h, "gf134")
        self.graphForms.append(self.gf134)

        h = drawing.create_oval(self.translate([175.0, 144.0, 193.0, 162.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = '')
        self.gf136 = GraphicalForm(drawing, h, "gf136")
        self.graphForms.append(self.gf136)

        h = drawing.create_line(self.translate([284.0, 153.0, 302.0, 153.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf140 = GraphicalForm(drawing, h, "gf140")
        self.graphForms.append(self.gf140)

        h = drawing.create_oval(self.translate([301.0, 146.0, 315.0, 159.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf141 = GraphicalForm(drawing, h, "gf141")
        self.graphForms.append(self.gf141)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([252.0, 153.0, 252.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Domain\nInterface', width = '0', justify= 'left', stipple='' )
        self.gf133 = GraphicalForm(drawing, h, 'gf133', fontObject=font)
        self.graphForms.append(self.gf133)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([253.0, 103.0, 253.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf142 = GraphicalForm(drawing, h, 'gf142', fontObject=font)
        self.graphForms.append(self.gf142)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_DomainInterface
