"""
__graph_primitive2stateVariable_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_primitive2stateVariable_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 88, 46
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
        h = drawing.create_polygon(self.translate([241.0, 261.0, 200.0, 280.0, 241.0, 301.0, 282.0, 280.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white', smooth = 'False', splinesteps =  '12')
        self.gf7 = GraphicalForm(drawing, h, "gf7")
        self.graphForms.append(self.gf7)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([240.0, 280.0, 240.0, 119.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'postAction', width = '0', justify= 'left', stipple='' )
        self.gf14 = GraphicalForm(drawing, h, 'gf14', fontObject=font)
        self.graphForms.append(self.gf14)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_primitive2stateVariable_Center
