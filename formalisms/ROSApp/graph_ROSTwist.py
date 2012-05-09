"""
__graph_ROSTwist.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ROSTwist(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 107, 101
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
        h = drawing.create_rectangle(self.translate([200.0, 103.0, 303.0, 200.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf27 = GraphicalForm(drawing, h, "gf27")
        self.graphForms.append(self.gf27)

        h = drawing.create_line(self.translate([251.0, 191.0, 270.0, 154.0, 234.0, 140.0, 246.0, 166.0, 267.0, 154.0, 262.0, 122.0, 241.0, 119.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'last', arrowshape = (15,15,3))
        self.gf29 = GraphicalForm(drawing, h, "gf29")
        self.graphForms.append(self.gf29)

        h = drawing.create_oval(self.translate([202.0, 153.0, 202.0, 153.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([250.0, 106.0, 250.0, 106.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([305.0, 148.0, 305.0, 148.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([253.0, 200.0, 253.0, 200.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([201.0, 199.0, 201.0, 199.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([201.0, 105.0, 201.0, 105.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([304.0, 106.0, 304.0, 106.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([303.0, 201.0, 303.0, 201.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_ROSTwist
