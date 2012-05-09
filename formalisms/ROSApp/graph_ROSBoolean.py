"""
__graph_ROSBoolean.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ROSBoolean(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 102, 102
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
        h = drawing.create_rectangle(self.translate([300.0, 100.0, 398.0, 198.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white')
        self.gf39 = GraphicalForm(drawing, h, "gf39")
        self.graphForms.append(self.gf39)

        h = drawing.create_oval(self.translate([302.0, 131.0, 302.0, 131.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([316.0, 100.0, 316.0, 100.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([352.0, 100.0, 352.0, 100.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([386.0, 101.0, 386.0, 101.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([400.0, 120.0, 400.0, 120.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([399.0, 150.0, 399.0, 150.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([399.0, 181.0, 399.0, 181.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([375.0, 200.0, 375.0, 200.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([329.0, 198.0, 329.0, 198.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([303.0, 186.0, 303.0, 186.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([301.0, 156.0, 301.0, 156.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([348.0, 124.0, 348.0, -9.0])[:2], tags = self.tag, font=font, fill = 'green', anchor = 'center', text = 'ON', width = '0', justify= 'left', stipple='' )
        self.gf45 = GraphicalForm(drawing, h, 'gf45', fontObject=font)
        self.graphForms.append(self.gf45)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([348.0, 168.0, 348.0, -24.0])[:2], tags = self.tag, font=font, fill = 'red3', anchor = 'center', text = 'OFF', width = '0', justify= 'left', stipple='' )
        self.gf46 = GraphicalForm(drawing, h, 'gf46', fontObject=font)
        self.graphForms.append(self.gf46)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_ROSBoolean
