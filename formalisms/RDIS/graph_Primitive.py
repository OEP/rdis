"""
__graph_Primitive.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Primitive(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 98, 105
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
        h = drawing.create_rectangle(self.translate([220.0, 141.0, 261.0, 180.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf73 = GraphicalForm(drawing, h, "gf73")
        self.graphForms.append(self.gf73)

        h = drawing.create_line(self.translate([220.0, 162.0, 201.0, 162.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf75 = GraphicalForm(drawing, h, "gf75")
        self.graphForms.append(self.gf75)

        h = drawing.create_oval(self.translate([179.0, 153.0, 199.0, 171.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = '')
        self.gf76 = GraphicalForm(drawing, h, "gf76")
        self.graphForms.append(self.gf76)

        h = drawing.create_line(self.translate([241.0, 142.0, 241.0, 122.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf78 = GraphicalForm(drawing, h, "gf78")
        self.graphForms.append(self.gf78)

        h = drawing.create_oval(self.translate([233.0, 106.0, 249.0, 120.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf79 = GraphicalForm(drawing, h, "gf79")
        self.graphForms.append(self.gf79)

        h = drawing.create_oval(self.translate([190.0, 162.0, 190.0, 162.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([242.0, 114.0, 242.0, 114.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='DejaVu Serif', size=18, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([240.0, 160.0, 240.0, -18.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'P', width = '0', justify= 'left', stipple='' )
        self.gf74 = GraphicalForm(drawing, h, 'gf74', fontObject=font)
        self.graphForms.append(self.gf74)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([241.0, 198.0, 241.0, 11.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf80 = GraphicalForm(drawing, h, 'gf80', fontObject=font)
        self.graphForms.append(self.gf80)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Primitive
