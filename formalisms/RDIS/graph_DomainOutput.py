"""
__graph_DomainOutput.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
__________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_DomainOutput(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 127.0, 88
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
        h = drawing.create_oval(self.translate([405.0, 151.0, 405.0, 151.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([286.0, 153.0, 286.0, 153.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([321.0, 122.0, 381.0, 182.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf96 = GraphicalForm(drawing, h, "gf96")
        self.graphForms.append(self.gf96)

        h = drawing.create_line(self.translate([382.0, 152.0, 397.0, 152.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf98 = GraphicalForm(drawing, h, "gf98")
        self.graphForms.append(self.gf98)

        h = drawing.create_oval(self.translate([396.0, 141.0, 411.0, 160.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = '')
        self.gf99 = GraphicalForm(drawing, h, "gf99")
        self.graphForms.append(self.gf99)

        h = drawing.create_line(self.translate([321.0, 152.0, 304.0, 152.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf100 = GraphicalForm(drawing, h, "gf100")
        self.graphForms.append(self.gf100)

        h = drawing.create_oval(self.translate([288.0, 144.0, 303.0, 162.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf101 = GraphicalForm(drawing, h, "gf101")
        self.graphForms.append(self.gf101)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([352.0, 152.0, 352.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Domain\nOutput', width = '0', justify= 'left', stipple='' )
        self.gf97 = GraphicalForm(drawing, h, 'gf97', fontObject=font)
        self.graphForms.append(self.gf97)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([351.0, 106.0, 351.0, 32.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf145 = GraphicalForm(drawing, h, 'gf145', fontObject=font)
        self.graphForms.append(self.gf145)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_DomainOutput
