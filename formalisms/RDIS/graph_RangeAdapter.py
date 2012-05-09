"""
__graph_RangeAdapter.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
__________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_RangeAdapter(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 106.0, 103
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
        h = drawing.create_rectangle(self.translate([201.0, 102.0, 301.0, 201.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf16 = GraphicalForm(drawing, h, "gf16")
        self.graphForms.append(self.gf16)

        h = drawing.create_oval(self.translate([240.0, 160.0, 256.0, 175.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf17 = GraphicalForm(drawing, h, "gf17")
        self.graphForms.append(self.gf17)

        h = drawing.create_line(self.translate([235.0, 155.0, 235.0, 155.0, 249.0, 144.0, 258.0, 154.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf20 = GraphicalForm(drawing, h, "gf20")
        self.graphForms.append(self.gf20)

        h = drawing.create_line(self.translate([220.0, 154.0, 220.0, 154.0, 248.0, 132.0, 269.0, 150.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf22 = GraphicalForm(drawing, h, "gf22")
        self.graphForms.append(self.gf22)

        h = drawing.create_line(self.translate([211.0, 150.0, 211.0, 150.0, 243.0, 123.0, 280.0, 144.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf23 = GraphicalForm(drawing, h, "gf23")
        self.graphForms.append(self.gf23)

        h = drawing.create_rectangle(self.translate([218.0, 114.0, 276.0, 125.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'sienna4')
        self.gf24 = GraphicalForm(drawing, h, "gf24")
        self.graphForms.append(self.gf24)

        h = drawing.create_oval(self.translate([220.0, 102.0, 220.0, 102.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([239.0, 101.0, 239.0, 101.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([262.0, 104.0, 262.0, 104.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([281.0, 104.0, 281.0, 104.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([305.0, 120.0, 305.0, 120.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([301.0, 146.0, 301.0, 146.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([303.0, 173.0, 303.0, 173.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([278.0, 202.0, 278.0, 202.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([251.0, 202.0, 251.0, 202.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([216.0, 201.0, 216.0, 201.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([199.0, 181.0, 199.0, 181.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([199.0, 158.0, 199.0, 158.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([202.0, 132.0, 202.0, 132.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_RangeAdapter
