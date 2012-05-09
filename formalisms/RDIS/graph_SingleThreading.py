"""
__graph_SingleThreading.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_SingleThreading(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 63.0, 61
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
        h = drawing.create_oval(self.translate([221.0, 121.0, 279.0, 178.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf119 = GraphicalForm(drawing, h, "gf119")
        self.graphForms.append(self.gf119)

        h = drawing.create_line(self.translate([258.0, 127.0, 258.0, 127.0, 239.0, 127.0, 240.0, 146.0, 258.0, 147.0, 259.0, 161.0, 249.0, 165.0, 250.0, 175.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'last', arrowshape = (15,15,3))
        self.gf122 = GraphicalForm(drawing, h, "gf122")
        self.graphForms.append(self.gf122)

        h = drawing.create_oval(self.translate([218.0, 148.0, 218.0, 148.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([233.0, 127.0, 233.0, 127.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([259.0, 122.0, 259.0, 122.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([276.0, 134.0, 276.0, 134.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([280.0, 153.0, 280.0, 153.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([269.0, 171.0, 269.0, 171.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([249.0, 179.0, 249.0, 179.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([229.0, 172.0, 229.0, 172.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_SingleThreading
