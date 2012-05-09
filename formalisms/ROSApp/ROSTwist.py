"""
__ROSTwist.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: pkilgo
Modified: Sun Apr 15 22:01:25 2012
__________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3List import *
from ATOM3String import *
from graph_ROSTwist import *
class ROSTwist(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_ROSTwist
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.angular=ATOM3List([ 0, 0, 0, 0],ATOM3String)
      lcobj0=[]
      cobj0=ATOM3String('x', 20)
      lcobj0.append(cobj0)
      cobj0=ATOM3String('y', 20)
      lcobj0.append(cobj0)
      cobj0=ATOM3String('z', 20)
      lcobj0.append(cobj0)
      self.angular.setValue(lcobj0)
      self.linear=ATOM3List([ 0, 0, 0, 0],ATOM3String)
      lcobj0=[]
      cobj0=ATOM3String('x', 20)
      lcobj0.append(cobj0)
      cobj0=ATOM3String('y', 20)
      lcobj0.append(cobj0)
      cobj0=ATOM3String('z', 20)
      lcobj0.append(cobj0)
      self.linear.setValue(lcobj0)
      self.generatedAttributes = {'angular': ('ATOM3List', 'ATOM3String'),
                                  'linear': ('ATOM3List', 'ATOM3String')      }
      self.realOrder = ['angular','linear']
      self.directEditing = [1,1]
   def clone(self):
      cloneObject = ROSTwist( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
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
      
      



