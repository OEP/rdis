"""
__graph_domainAdapter2Interface_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_domainAdapter2Interface_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 90, 66
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
        h = drawing.create_polygon(self.translate([198.0, 200.0, 240.0, 171.0, 282.0, 200.0, 240.0, 231.0, 220.0, 220.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white', smooth = '0', splinesteps =  '12')
        self.gf83 = GraphicalForm(drawing, h, "gf83")
        self.graphForms.append(self.gf83)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([240.0, 200.0, 240.0, -105.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'mappings', width = '0', justify= 'left', stipple='' )
        self.gf84 = GraphicalForm(drawing, h, 'gf84', fontObject=font)
        self.graphForms.append(self.gf84)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_domainAdapter2Interface_Center
