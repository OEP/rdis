"""
__Primitive.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: pkilgo
Modified: Sun Apr 15 13:18:31 2012
___________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3List import *
from graph_Primitive import *
class Primitive(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Primitive
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.name=ATOM3String('', 20)
      self.keyword_= self.name
      self.format=ATOM3String('', 20)
      self.formatArgs=ATOM3List([ 1, 1, 1, 0],ATOM3String)
      lcobj0=[]
      self.formatArgs.setValue(lcobj0)
      self.pack=ATOM3String('', 20)
      self.parameters=ATOM3List([ 1, 1, 1, 0],ATOM3String)
      lcobj0=[]
      self.parameters.setValue(lcobj0)
      self.postActions=ATOM3List([ 1, 1, 1, 0],ATOM3String)
      lcobj0=[]
      self.postActions.setValue(lcobj0)
      self.regex=ATOM3String('', 20)
      self.unpack=ATOM3String('', 20)
      self.generatedAttributes = {'format': ('ATOM3String', ),
                                  'formatArgs': ('ATOM3List', 'ATOM3String'),
                                  'name': ('ATOM3String', ),
                                  'pack': ('ATOM3String', ),
                                  'parameters': ('ATOM3List', 'ATOM3String'),
                                  'postActions': ('ATOM3List', 'ATOM3String'),
                                  'regex': ('ATOM3String', ),
                                  'unpack': ('ATOM3String', )      }
      self.realOrder = ['format','formatArgs','name','pack','parameters','postActions','regex','unpack']
      self.directEditing = [1,1,1,1,1,1,1,1]
   def clone(self):
      cloneObject = Primitive( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def QOCA(self, params):
      """
      QOCA Constraint Template
      NOTE: DO NOT select a POST/PRE action trigger
      Constraints will be added/removed in a logical manner by other mechanisms.
      """
      return # <---- Remove this to use QOCA
      
      """ Get the high level constraint helper and solver """
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)
      oc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)
      
      



