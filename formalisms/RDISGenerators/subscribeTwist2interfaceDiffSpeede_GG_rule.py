# _ subscribeTwist2interfaceDiffSpeede_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from RangeAdapter import *
from ROSTwist import *
from SerialConnection import *
from connectionTerminate import *
from ASG_RDIS import *
from ROSPublish import *
from interface2domainOutput import *
from ROSSubscribe import *
from connection2threading import *
from StateVariable import *
from interface2primitive import *
from ASG_ROSApp import *
from Interface import *
from DomainInterface import *
from ROSNode import *
from DomainAdapter import *
from connectionKeepalive import *
from domainAdapter2domainInterface import *
from connectionStartup import *
from primitive2connection import *
from domainInterface2Interface import *
from Threading import *
from Connection import *
from domainAdapter2domainOutput import *
from ROSMessage import *
from Primitive import *
from SingleThreading import *
from ROSTopic import *
from ROSType import *
from DifferentialSpeedAdapter import *
from ROSBoolean import *
from DomainOutput import *
from GenericGraphNode import *
from GenericGraphEdge import *
from ASG_GenericGraph import *
class subscribeTwist2interfaceDiffSpeede_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_RDIS(parent)
      self.LHS.merge(ASG_ROSApp(parent))

      self.obj503=DifferentialSpeedAdapter(parent)
      self.obj503.preAction( self.LHS.CREATE )
      self.obj503.isGraphObjectVisual = True

      if(hasattr(self.obj503, '_setHierarchicalLink')):
        self.obj503._setHierarchicalLink(False)

      # angular
      self.obj503.angular.setValue('')
      self.obj503.angular.setNone()

      # linear
      self.obj503.linear.setValue('')
      self.obj503.linear.setNone()

      self.obj503.GGLabel.setValue(7)
      self.obj503.graphClass_= graph_DifferentialSpeedAdapter
      if parent.genGraphics:
         new_obj = graph_DifferentialSpeedAdapter(320.0,0.0,self.obj503)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj503.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj503)
      self.obj503.postAction( self.LHS.CREATE )

      self.obj500=DomainInterface(parent)
      self.obj500.preAction( self.LHS.CREATE )
      self.obj500.isGraphObjectVisual = True

      if(hasattr(self.obj500, '_setHierarchicalLink')):
        self.obj500._setHierarchicalLink(False)

      # name
      self.obj500.name.setValue('')
      self.obj500.name.setNone()

      self.obj500.GGLabel.setValue(6)
      self.obj500.graphClass_= graph_DomainInterface
      if parent.genGraphics:
         new_obj = graph_DomainInterface(300.0,180.0,self.obj500)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj500.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj500)
      self.obj500.postAction( self.LHS.CREATE )

      self.obj504=domainAdapter2domainInterface(parent)
      self.obj504.preAction( self.LHS.CREATE )
      self.obj504.isGraphObjectVisual = True

      if(hasattr(self.obj504, '_setHierarchicalLink')):
        self.obj504._setHierarchicalLink(False)

      self.obj504.GGLabel.setValue(8)
      self.obj504.graphClass_= graph_domainAdapter2domainInterface
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainInterface(452.5,155.0,self.obj504)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj504.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj504)
      self.obj504.postAction( self.LHS.CREATE )

      self.obj492=ROSTwist(parent)
      self.obj492.preAction( self.LHS.CREATE )
      self.obj492.isGraphObjectVisual = True

      if(hasattr(self.obj492, '_setHierarchicalLink')):
        self.obj492._setHierarchicalLink(False)

      # angular
      self.obj492.angular.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('x', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('y', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('z', 20)
      lcobj2.append(cobj2)
      self.obj492.angular.setValue(lcobj2)
      self.obj492.angular.setNone()

      # linear
      self.obj492.linear.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('x', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('y', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('z', 20)
      lcobj2.append(cobj2)
      self.obj492.linear.setValue(lcobj2)
      self.obj492.linear.setNone()

      self.obj492.GGLabel.setValue(4)
      self.obj492.graphClass_= graph_ROSTwist
      if parent.genGraphics:
         new_obj = graph_ROSTwist(80.0,320.0,self.obj492)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj492.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj492)
      self.obj492.postAction( self.LHS.CREATE )

      self.obj493=ROSType(parent)
      self.obj493.preAction( self.LHS.CREATE )
      self.obj493.isGraphObjectVisual = True

      if(hasattr(self.obj493, '_setHierarchicalLink')):
        self.obj493._setHierarchicalLink(False)

      self.obj493.GGLabel.setValue(5)
      self.obj493.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(87.0,301.0,self.obj493)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj493.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj493)
      self.obj493.postAction( self.LHS.CREATE )

      self.obj490=ROSTopic(parent)
      self.obj490.preAction( self.LHS.CREATE )
      self.obj490.isGraphObjectVisual = True

      if(hasattr(self.obj490, '_setHierarchicalLink')):
        self.obj490._setHierarchicalLink(False)

      # name
      self.obj490.name.setValue('')
      self.obj490.name.setNone()

      self.obj490.GGLabel.setValue(2)
      self.obj490.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(80.0,180.0,self.obj490)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj490.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj490)
      self.obj490.postAction( self.LHS.CREATE )

      self.obj489=ROSNode(parent)
      self.obj489.preAction( self.LHS.CREATE )
      self.obj489.isGraphObjectVisual = True

      if(hasattr(self.obj489, '_setHierarchicalLink')):
        self.obj489._setHierarchicalLink(False)

      # name
      self.obj489.name.setValue('')
      self.obj489.name.setNone()

      self.obj489.GGLabel.setValue(1)
      self.obj489.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(80.0,40.0,self.obj489)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj489.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj489)
      self.obj489.postAction( self.LHS.CREATE )

      self.obj491=ROSSubscribe(parent)
      self.obj491.preAction( self.LHS.CREATE )
      self.obj491.isGraphObjectVisual = True

      if(hasattr(self.obj491, '_setHierarchicalLink')):
        self.obj491._setHierarchicalLink(False)

      self.obj491.GGLabel.setValue(3)
      self.obj491.graphClass_= graph_ROSSubscribe
      if parent.genGraphics:
         new_obj = graph_ROSSubscribe(157.5,157.0,self.obj491)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj491.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj491)
      self.obj491.postAction( self.LHS.CREATE )

      self.obj503.out_connections_.append(self.obj504)
      self.obj504.in_connections_.append(self.obj503)
      self.obj503.graphObject_.pendingConnections.append((self.obj503.graphObject_.tag, self.obj504.graphObject_.tag, [422.0, 91.0, 452.5, 155.0], 0, True))
      self.obj504.out_connections_.append(self.obj500)
      self.obj500.in_connections_.append(self.obj504)
      self.obj504.graphObject_.pendingConnections.append((self.obj504.graphObject_.tag, self.obj500.graphObject_.tag, [443.0, 239.0, 452.5, 155.0], 0, True))
      self.obj493.out_connections_.append(self.obj492)
      self.obj492.in_connections_.append(self.obj493)
      self.obj493.graphObject_.pendingConnections.append((self.obj493.graphObject_.tag, self.obj492.graphObject_.tag, [83.0, 324.0, 87.0, 301.0], 0, True))
      self.obj490.out_connections_.append(self.obj491)
      self.obj491.in_connections_.append(self.obj490)
      self.obj490.graphObject_.pendingConnections.append((self.obj490.graphObject_.tag, self.obj491.graphObject_.tag, [163.0, 184.0, 157.5, 157.0], 0, True))
      self.obj490.out_connections_.append(self.obj493)
      self.obj493.in_connections_.append(self.obj490)
      self.obj490.graphObject_.pendingConnections.append((self.obj490.graphObject_.tag, self.obj493.graphObject_.tag, [91.0, 278.0, 87.0, 301.0], 0, True))
      self.obj491.out_connections_.append(self.obj489)
      self.obj489.in_connections_.append(self.obj491)
      self.obj491.graphObject_.pendingConnections.append((self.obj491.graphObject_.tag, self.obj489.graphObject_.tag, [152.0, 130.0, 157.5, 157.0], 0, True))

      self.RHS = ASG_RDIS(parent)
      self.RHS.merge(ASG_ROSApp(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj503=DifferentialSpeedAdapter(parent)
      self.obj503.preAction( self.RHS.CREATE )
      self.obj503.isGraphObjectVisual = True

      if(hasattr(self.obj503, '_setHierarchicalLink')):
        self.obj503._setHierarchicalLink(False)

      # angular
      self.obj503.angular.setValue('<angular[0]>')

      # linear
      self.obj503.linear.setValue('<linear[0]>')

      self.obj503.GGLabel.setValue(7)
      self.obj503.graphClass_= graph_DifferentialSpeedAdapter
      if parent.genGraphics:
         new_obj = graph_DifferentialSpeedAdapter(320.0,0.0,self.obj503)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj503.graphObject_ = new_obj
      self.obj5030= AttrCalc()
      self.obj5030.Copy=ATOM3Boolean()
      self.obj5030.Copy.setValue(('Copy from LHS', 0))
      self.obj5030.Copy.config = 0
      self.obj5030.Specify=ATOM3Constraint()
      self.obj5030.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj503.GGset2Any['angular']= self.obj5030
      self.obj5031= AttrCalc()
      self.obj5031.Copy=ATOM3Boolean()
      self.obj5031.Copy.setValue(('Copy from LHS', 0))
      self.obj5031.Copy.config = 0
      self.obj5031.Specify=ATOM3Constraint()
      self.obj5031.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj503.GGset2Any['linear']= self.obj5031

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj503)
      self.obj503.postAction( self.RHS.CREATE )

      self.obj500=DomainInterface(parent)
      self.obj500.preAction( self.RHS.CREATE )
      self.obj500.isGraphObjectVisual = True

      if(hasattr(self.obj500, '_setHierarchicalLink')):
        self.obj500._setHierarchicalLink(False)

      # name
      self.obj500.name.setValue('')
      self.obj500.name.setNone()

      self.obj500.GGLabel.setValue(6)
      self.obj500.graphClass_= graph_DomainInterface
      if parent.genGraphics:
         new_obj = graph_DomainInterface(300.0,80.0,self.obj500)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj500.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj500)
      self.obj500.postAction( self.RHS.CREATE )

      self.obj504=domainAdapter2domainInterface(parent)
      self.obj504.preAction( self.RHS.CREATE )
      self.obj504.isGraphObjectVisual = True

      if(hasattr(self.obj504, '_setHierarchicalLink')):
        self.obj504._setHierarchicalLink(False)

      self.obj504.GGLabel.setValue(8)
      self.obj504.graphClass_= graph_domainAdapter2domainInterface
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainInterface(452.5,155.0,self.obj504)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj504.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj504)
      self.obj504.postAction( self.RHS.CREATE )

      self.obj492=ROSTwist(parent)
      self.obj492.preAction( self.RHS.CREATE )
      self.obj492.isGraphObjectVisual = True

      if(hasattr(self.obj492, '_setHierarchicalLink')):
        self.obj492._setHierarchicalLink(False)

      # angular
      self.obj492.angular.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('x', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('y', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('z', 20)
      lcobj2.append(cobj2)
      self.obj492.angular.setValue(lcobj2)
      self.obj492.angular.setNone()

      # linear
      self.obj492.linear.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('x', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('y', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('z', 20)
      lcobj2.append(cobj2)
      self.obj492.linear.setValue(lcobj2)
      self.obj492.linear.setNone()

      self.obj492.GGLabel.setValue(4)
      self.obj492.graphClass_= graph_ROSTwist
      if parent.genGraphics:
         new_obj = graph_ROSTwist(80.0,260.0,self.obj492)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj492.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj492)
      self.obj492.postAction( self.RHS.CREATE )

      self.obj493=ROSType(parent)
      self.obj493.preAction( self.RHS.CREATE )
      self.obj493.isGraphObjectVisual = True

      if(hasattr(self.obj493, '_setHierarchicalLink')):
        self.obj493._setHierarchicalLink(False)

      self.obj493.GGLabel.setValue(5)
      self.obj493.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(87.0,301.0,self.obj493)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj493.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj493)
      self.obj493.postAction( self.RHS.CREATE )

      self.obj490=ROSTopic(parent)
      self.obj490.preAction( self.RHS.CREATE )
      self.obj490.isGraphObjectVisual = True

      if(hasattr(self.obj490, '_setHierarchicalLink')):
        self.obj490._setHierarchicalLink(False)

      # name
      self.obj490.name.setValue('')
      self.obj490.name.setNone()

      self.obj490.GGLabel.setValue(2)
      self.obj490.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(80.0,80.0,self.obj490)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj490.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj490)
      self.obj490.postAction( self.RHS.CREATE )

      self.obj489=ROSNode(parent)
      self.obj489.preAction( self.RHS.CREATE )
      self.obj489.isGraphObjectVisual = True

      if(hasattr(self.obj489, '_setHierarchicalLink')):
        self.obj489._setHierarchicalLink(False)

      # name
      self.obj489.name.setValue('')
      self.obj489.name.setNone()

      self.obj489.GGLabel.setValue(1)
      self.obj489.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(80.0,-140.0,self.obj489)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj489.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj489)
      self.obj489.postAction( self.RHS.CREATE )

      self.obj491=ROSSubscribe(parent)
      self.obj491.preAction( self.RHS.CREATE )
      self.obj491.isGraphObjectVisual = True

      if(hasattr(self.obj491, '_setHierarchicalLink')):
        self.obj491._setHierarchicalLink(False)

      self.obj491.GGLabel.setValue(3)
      self.obj491.graphClass_= graph_ROSSubscribe
      if parent.genGraphics:
         new_obj = graph_ROSSubscribe(157.5,157.0,self.obj491)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj491.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj491)
      self.obj491.postAction( self.RHS.CREATE )

      self.obj517=GenericGraphEdge(parent)
      self.obj517.preAction( self.RHS.CREATE )
      self.obj517.isGraphObjectVisual = True

      if(hasattr(self.obj517, '_setHierarchicalLink')):
        self.obj517._setHierarchicalLink(False)

      self.obj517.GGLabel.setValue(10)
      self.obj517.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(261.0,226.5,self.obj517)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj517.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj517)
      self.obj517.postAction( self.RHS.CREATE )

      self.obj503.out_connections_.append(self.obj504)
      self.obj504.in_connections_.append(self.obj503)
      self.obj503.graphObject_.pendingConnections.append((self.obj503.graphObject_.tag, self.obj504.graphObject_.tag, [523.0, 164.0, 452.5, 155.0], 2, 0))
      self.obj504.out_connections_.append(self.obj500)
      self.obj500.in_connections_.append(self.obj504)
      self.obj504.graphObject_.pendingConnections.append((self.obj504.graphObject_.tag, self.obj500.graphObject_.tag, [305.0, 234.0, 452.5, 155.0], 2, 0))
      self.obj493.out_connections_.append(self.obj492)
      self.obj492.in_connections_.append(self.obj493)
      self.obj493.graphObject_.pendingConnections.append((self.obj493.graphObject_.tag, self.obj492.graphObject_.tag, [101.0, 365.0, 87.0, 301.0], 2, 0))
      self.obj490.out_connections_.append(self.obj491)
      self.obj491.in_connections_.append(self.obj490)
      self.obj490.graphObject_.pendingConnections.append((self.obj490.graphObject_.tag, self.obj491.graphObject_.tag, [84.0, 231.0, 157.5, 157.0], 2, 0))
      self.obj490.out_connections_.append(self.obj493)
      self.obj493.in_connections_.append(self.obj490)
      self.obj490.graphObject_.pendingConnections.append((self.obj490.graphObject_.tag, self.obj493.graphObject_.tag, [84.0, 231.0, 87.0, 301.0], 2, 0))
      self.obj490.out_connections_.append(self.obj517)
      self.obj517.in_connections_.append(self.obj490)
      self.obj490.graphObject_.pendingConnections.append((self.obj490.graphObject_.tag, self.obj517.graphObject_.tag, [217.0, 219.0, 261.0, 226.5], 0, True))
      self.obj491.out_connections_.append(self.obj489)
      self.obj489.in_connections_.append(self.obj491)
      self.obj491.graphObject_.pendingConnections.append((self.obj491.graphObject_.tag, self.obj489.graphObject_.tag, [97.0, 64.0, 157.5, 157.0], 2, 0))
      self.obj517.out_connections_.append(self.obj500)
      self.obj500.in_connections_.append(self.obj517)
      self.obj517.graphObject_.pendingConnections.append((self.obj517.graphObject_.tag, self.obj500.graphObject_.tag, [305.0, 234.0, 261.0, 226.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName20 is not guaranteed to be unique (so change it, be safe!)
      
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      return not hasattr(node2, "_uniqueName20") and not hasattr(node6, "_uniqueName20")
      
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName20 is not guaranteed to be unique (so change it, be safe!)
      
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      node2._uniqueName20 = True
      node6._uniqueName20 = True
      
      

