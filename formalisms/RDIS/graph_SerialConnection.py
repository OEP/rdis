"""
__graph_SerialConnection.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_SerialConnection(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 174, 95
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
        h = drawing.create_rectangle(self.translate([184.0, 133.0, 333.0, 202.0]), tags = self.tag, stipple = '', width = 3, outline = 'white', fill = 'white')
        self.gf102 = GraphicalForm(drawing, h, "gf102")
        self.graphForms.append(self.gf102)

        h = drawing.create_line(self.translate([187.0, 141.0, 328.0, 141.0, 307.0, 200.0, 207.0, 200.0, 188.0, 141.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'round', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf91 = GraphicalForm(drawing, h, "gf91")
        self.graphForms.append(self.gf91)

        h = drawing.create_oval(self.translate([235.0, 158.0, 240.0, 163.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf92 = GraphicalForm(drawing, h, "gf92")
        self.graphForms.append(self.gf92)

        h = drawing.create_oval(self.translate([297.0, 158.0, 302.0, 163.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf94 = GraphicalForm(drawing, h, "gf94")
        self.graphForms.append(self.gf94)

        h = drawing.create_oval(self.translate([276.0, 158.0, 281.0, 163.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf95 = GraphicalForm(drawing, h, "gf95")
        self.graphForms.append(self.gf95)

        h = drawing.create_oval(self.translate([256.0, 158.0, 261.0, 163.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf96 = GraphicalForm(drawing, h, "gf96")
        self.graphForms.append(self.gf96)

        h = drawing.create_oval(self.translate([215.0, 158.0, 220.0, 163.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf97 = GraphicalForm(drawing, h, "gf97")
        self.graphForms.append(self.gf97)

        h = drawing.create_oval(self.translate([226.0, 176.0, 231.0, 181.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf98 = GraphicalForm(drawing, h, "gf98")
        self.graphForms.append(self.gf98)

        h = drawing.create_oval(self.translate([246.0, 176.0, 251.0, 181.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf99 = GraphicalForm(drawing, h, "gf99")
        self.graphForms.append(self.gf99)

        h = drawing.create_oval(self.translate([267.0, 176.0, 272.0, 181.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf100 = GraphicalForm(drawing, h, "gf100")
        self.graphForms.append(self.gf100)

        h = drawing.create_oval(self.translate([287.0, 176.0, 292.0, 181.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf101 = GraphicalForm(drawing, h, "gf101")
        self.graphForms.append(self.gf101)

        h = drawing.create_line(self.translate([319.0, 170.0, 342.0, 170.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf104 = GraphicalForm(drawing, h, "gf104")
        self.graphForms.append(self.gf104)

        h = drawing.create_oval(self.translate([340.0, 162.0, 354.0, 176.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'black')
        self.gf105 = GraphicalForm(drawing, h, "gf105")
        self.graphForms.append(self.gf105)

        h = drawing.create_line(self.translate([255.0, 123.0, 255.0, 141.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf106 = GraphicalForm(drawing, h, "gf106")
        self.graphForms.append(self.gf106)

        h = drawing.create_line(self.translate([220.0, 113.0, 220.0, 126.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf107 = GraphicalForm(drawing, h, "gf107")
        self.graphForms.append(self.gf107)

        h = drawing.create_line(self.translate([220.0, 124.0, 292.0, 124.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf108 = GraphicalForm(drawing, h, "gf108")
        self.graphForms.append(self.gf108)

        h = drawing.create_line(self.translate([290.0, 113.0, 290.0, 123.0]), tags = self.tag, stipple = '', width = 3, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf110 = GraphicalForm(drawing, h, "gf110")
        self.graphForms.append(self.gf110)

        h = drawing.create_oval(self.translate([227.0, 119.0, 227.0, 119.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([241.0, 118.0, 241.0, 118.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([255.0, 120.0, 255.0, 120.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([270.0, 118.0, 270.0, 118.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([284.0, 118.0, 284.0, 118.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([354.0, 169.0, 354.0, 169.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_SerialConnection
