"""
__graph_domainInterface2Interface_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_domainInterface2Interface_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 89, 47
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
        h = drawing.create_polygon(self.translate([-41.0, 0.0, -1.0, -21.0, 42.0, 0.0, -2.0, 21.0]), tags = self.tag, stipple = '', width = 3, outline = 'black', fill = 'white', smooth = 'False', splinesteps =  '12')
        self.gf85 = GraphicalForm(drawing, h, "gf85")
        self.graphForms.append(self.gf85)

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-1.0, 0.0, -1.0, -188.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'mappings', width = '0', justify= 'left', stipple='' )
        self.gf86 = GraphicalForm(drawing, h, 'gf86', fontObject=font)
        self.graphForms.append(self.gf86)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_domainInterface2Interface_Center
