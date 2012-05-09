"""
__graph_DifferentialSpeedAdapter.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_DifferentialSpeedAdapter(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 103, 104
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
        h = drawing.create_rectangle(self.translate([202.0, 102.0, 301.0, 202.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf38 = GraphicalForm(drawing, h, "gf38")
        self.graphForms.append(self.gf38)

        h = drawing.create_oval(self.translate([239.0, 150.0, 257.0, 168.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf39 = GraphicalForm(drawing, h, "gf39")
        self.graphForms.append(self.gf39)

        h = drawing.create_line(self.translate([248.0, 169.0, 248.0, 110.0, 230.0, 127.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf40 = GraphicalForm(drawing, h, "gf40")
        self.graphForms.append(self.gf40)

        h = drawing.create_line(self.translate([248.0, 112.0, 268.0, 127.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf41 = GraphicalForm(drawing, h, "gf41")
        self.graphForms.append(self.gf41)

        h = drawing.create_line(self.translate([250.0, 133.0, 288.0, 133.0, 287.0, 167.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf42 = GraphicalForm(drawing, h, "gf42")
        self.graphForms.append(self.gf42)

        h = drawing.create_line(self.translate([288.0, 165.0, 274.0, 158.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf43 = GraphicalForm(drawing, h, "gf43")
        self.graphForms.append(self.gf43)

        h = drawing.create_line(self.translate([288.0, 166.0, 298.0, 150.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf44 = GraphicalForm(drawing, h, "gf44")
        self.graphForms.append(self.gf44)

        h = drawing.create_oval(self.translate([218.0, 101.0, 218.0, 101.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([241.0, 104.0, 241.0, 104.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([269.0, 102.0, 269.0, 102.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([300.0, 113.0, 300.0, 113.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([302.0, 134.0, 302.0, 134.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([302.0, 161.0, 302.0, 161.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([302.0, 191.0, 302.0, 191.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([273.0, 201.0, 273.0, 201.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([254.0, 201.0, 254.0, 201.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([224.0, 204.0, 224.0, 204.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([202.0, 185.0, 202.0, 185.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([203.0, 164.0, 203.0, 164.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([203.0, 144.0, 203.0, 144.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([203.0, 120.0, 203.0, 120.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_DifferentialSpeedAdapter
