"""
__ROS_wander_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: pkilgo
Modified: Sun Apr 15 23:18:08 2012
________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from ROSTwist import *
from ROSType import *
from ROSPublish import *
from ROSTopic import *
from ROSBoolean import *
from ROSNode import *
from ROSSubscribe import *
from graph_ROSTopic import *
from graph_ROSPublish import *
from graph_ROSBoolean import *
from graph_ROSTwist import *
from graph_ROSType import *
from graph_ROSNode import *
from graph_ROSSubscribe import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def ROS_wander_MDL(self, rootNode, ROSAppRootNode=None):

    # --- Generating attributes code for ASG ROSApp ---
    if( ROSAppRootNode ): 
        # author
        ROSAppRootNode.author.setValue('Annonymous')

        # description
        ROSAppRootNode.description.setValue('\n')
        ROSAppRootNode.description.setHeight(15)

        # name
        ROSAppRootNode.name.setValue('')
        ROSAppRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj29=ROSTwist(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # angular
    self.obj29.angular.setActionFlags([ 0, 0, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3String('x', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('y', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('z', 20)
    lcobj2.append(cobj2)
    self.obj29.angular.setValue(lcobj2)

    # linear
    self.obj29.linear.setActionFlags([ 0, 0, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3String('x', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('y', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('z', 20)
    lcobj2.append(cobj2)
    self.obj29.linear.setValue(lcobj2)

    self.obj29.graphClass_= graph_ROSTwist
    if self.genGraphics:
       new_obj = graph_ROSTwist(280.0,420.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSTwist", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj33=ROSType(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    self.obj33.graphClass_= graph_ROSType
    if self.genGraphics:
       new_obj = graph_ROSType(324.5,366.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=ROSType(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    self.obj34.graphClass_= graph_ROSType
    if self.genGraphics:
       new_obj = graph_ROSType(597.5,374.5,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=ROSPublish(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    self.obj35.graphClass_= graph_ROSPublish
    if self.genGraphics:
       new_obj = graph_ROSPublish(457.0,183.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSPublish", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj27=ROSTopic(self)
    self.obj27.isGraphObjectVisual = True

    if(hasattr(self.obj27, '_setHierarchicalLink')):
      self.obj27._setHierarchicalLink(False)

    # name
    self.obj27.name.setValue('setSpeed')

    self.obj27.graphClass_= graph_ROSTopic
    if self.genGraphics:
       new_obj = graph_ROSTopic(240.0,220.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSTopic", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)
    self.obj27.postAction( rootNode.CREATE )

    self.obj28=ROSTopic(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # name
    self.obj28.name.setValue('hitObject')

    self.obj28.graphClass_= graph_ROSTopic
    if self.genGraphics:
       new_obj = graph_ROSTopic(500.0,240.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSTopic", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj30=ROSBoolean(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # data
    self.obj30.data.setValue('')
    self.obj30.data.setNone()

    self.obj30.graphClass_= graph_ROSBoolean
    if self.genGraphics:
       new_obj = graph_ROSBoolean(600.0,420.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSBoolean", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj26=ROSNode(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # name
    self.obj26.name.setValue('rdisWanderer')

    self.obj26.graphClass_= graph_ROSNode
    if self.genGraphics:
       new_obj = graph_ROSNode(240.0,60.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSNode", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    self.obj36=ROSSubscribe(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    self.obj36.graphClass_= graph_ROSSubscribe
    if self.genGraphics:
       new_obj = graph_ROSSubscribe(317.5,187.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSSubscribe", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    # Connections for obj29 (graphObject_: Obj3) of type ROSTwist
    self.drawConnections(
 )
    # Connections for obj33 (graphObject_: Obj7) of type ROSType
    self.drawConnections(
(self.obj33,self.obj29,[324.5, 366.0, 332.0, 425.0],"true", 2) )
    # Connections for obj34 (graphObject_: Obj8) of type ROSType
    self.drawConnections(
(self.obj34,self.obj30,[597.5, 374.5, 618.0, 422.0],"true", 2) )
    # Connections for obj35 (graphObject_: Obj9) of type ROSPublish
    self.drawConnections(
(self.obj35,self.obj28,[457.0, 183.0, 530.0, 251.0],"true", 2) )
    # Connections for obj27 (graphObject_: Obj1) named setSpeed
    self.drawConnections(
(self.obj27,self.obj33,[317.0, 307.0, 324.5, 366.0],"true", 2),
(self.obj27,self.obj36,[323.0, 224.0, 317.5, 187.0],"true", 2) )
    # Connections for obj28 (graphObject_: Obj2) named hitObject
    self.drawConnections(
(self.obj28,self.obj34,[577.0, 327.0, 597.5, 374.5],"true", 2) )
    # Connections for obj30 (graphObject_: Obj4) of type ROSBoolean
    self.drawConnections(
 )
    # Connections for obj26 (graphObject_: Obj0) named rdisWanderer
    self.drawConnections(
(self.obj26,self.obj35,[384.0, 115.0, 457.0, 183.0],"true", 2) )
    # Connections for obj36 (graphObject_: Obj10) of type ROSSubscribe
    self.drawConnections(
(self.obj36,self.obj26,[317.5, 187.0, 312.0, 150.0],"true", 2) )

newfunction = ROS_wander_MDL

loadedMMName = 'ROSApp_META'

atom3version = '0.3'
