# _ subscribeBoolean2domainOutputRangeee_GG_rule.py ____________________________________________________________________________
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
class subscribeBoolean2domainOutputRangeee_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_RDIS(parent)
      self.LHS.merge(ASG_ROSApp(parent))

      self.obj1132=RangeAdapter(parent)
      self.obj1132.preAction( self.LHS.CREATE )
      self.obj1132.isGraphObjectVisual = True

      if(hasattr(self.obj1132, '_setHierarchicalLink')):
        self.obj1132._setHierarchicalLink(False)

      # distance
      self.obj1132.distance.setValue('')
      self.obj1132.distance.setNone()

      self.obj1132.GGLabel.setValue(7)
      self.obj1132.graphClass_= graph_RangeAdapter
      if parent.genGraphics:
         new_obj = graph_RangeAdapter(340.0,20.0,self.obj1132)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1132.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1132)
      self.obj1132.postAction( self.LHS.CREATE )

      self.obj1131=DomainOutput(parent)
      self.obj1131.preAction( self.LHS.CREATE )
      self.obj1131.isGraphObjectVisual = True

      if(hasattr(self.obj1131, '_setHierarchicalLink')):
        self.obj1131._setHierarchicalLink(False)

      # name
      self.obj1131.name.setValue('')
      self.obj1131.name.setNone()

      self.obj1131.GGLabel.setValue(6)
      self.obj1131.graphClass_= graph_DomainOutput
      if parent.genGraphics:
         new_obj = graph_DomainOutput(320.0,140.0,self.obj1131)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1131.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1131)
      self.obj1131.postAction( self.LHS.CREATE )

      self.obj1133=domainAdapter2domainOutput(parent)
      self.obj1133.preAction( self.LHS.CREATE )
      self.obj1133.isGraphObjectVisual = True

      if(hasattr(self.obj1133, '_setHierarchicalLink')):
        self.obj1133._setHierarchicalLink(False)

      self.obj1133.GGLabel.setValue(8)
      self.obj1133.graphClass_= graph_domainAdapter2domainOutput
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainOutput(415.5,158.5,self.obj1133)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1133.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1133)
      self.obj1133.postAction( self.LHS.CREATE )

      self.obj1124=ROSType(parent)
      self.obj1124.preAction( self.LHS.CREATE )
      self.obj1124.isGraphObjectVisual = True

      if(hasattr(self.obj1124, '_setHierarchicalLink')):
        self.obj1124._setHierarchicalLink(False)

      self.obj1124.GGLabel.setValue(5)
      self.obj1124.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(155.5,264.5,self.obj1124)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1124.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1124)
      self.obj1124.postAction( self.LHS.CREATE )

      self.obj1122=ROSTopic(parent)
      self.obj1122.preAction( self.LHS.CREATE )
      self.obj1122.isGraphObjectVisual = True

      if(hasattr(self.obj1122, '_setHierarchicalLink')):
        self.obj1122._setHierarchicalLink(False)

      # name
      self.obj1122.name.setValue('')
      self.obj1122.name.setNone()

      self.obj1122.GGLabel.setValue(3)
      self.obj1122.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(80.0,160.0,self.obj1122)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1122.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1122)
      self.obj1122.postAction( self.LHS.CREATE )

      self.obj1121=ROSBoolean(parent)
      self.obj1121.preAction( self.LHS.CREATE )
      self.obj1121.isGraphObjectVisual = True

      if(hasattr(self.obj1121, '_setHierarchicalLink')):
        self.obj1121._setHierarchicalLink(False)

      # data
      self.obj1121.data.setValue('')
      self.obj1121.data.setNone()

      self.obj1121.GGLabel.setValue(2)
      self.obj1121.graphClass_= graph_ROSBoolean
      if parent.genGraphics:
         new_obj = graph_ROSBoolean(100.0,280.0,self.obj1121)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1121.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1121)
      self.obj1121.postAction( self.LHS.CREATE )

      self.obj1120=ROSNode(parent)
      self.obj1120.preAction( self.LHS.CREATE )
      self.obj1120.isGraphObjectVisual = True

      if(hasattr(self.obj1120, '_setHierarchicalLink')):
        self.obj1120._setHierarchicalLink(False)

      # name
      self.obj1120.name.setValue('')
      self.obj1120.name.setNone()

      self.obj1120.GGLabel.setValue(1)
      self.obj1120.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(80.0,40.0,self.obj1120)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1120.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1120)
      self.obj1120.postAction( self.LHS.CREATE )

      self.obj1123=ROSSubscribe(parent)
      self.obj1123.preAction( self.LHS.CREATE )
      self.obj1123.isGraphObjectVisual = True

      if(hasattr(self.obj1123, '_setHierarchicalLink')):
        self.obj1123._setHierarchicalLink(False)

      self.obj1123.GGLabel.setValue(4)
      self.obj1123.graphClass_= graph_ROSSubscribe
      if parent.genGraphics:
         new_obj = graph_ROSSubscribe(157.5,147.0,self.obj1123)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1123.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj1123)
      self.obj1123.postAction( self.LHS.CREATE )

      self.obj1132.out_connections_.append(self.obj1133)
      self.obj1133.in_connections_.append(self.obj1132)
      self.obj1132.graphObject_.pendingConnections.append((self.obj1132.graphObject_.tag, self.obj1133.graphObject_.tag, [392.0, 122.0, 415.5, 158.5], 0, True))
      self.obj1133.out_connections_.append(self.obj1131)
      self.obj1131.in_connections_.append(self.obj1133)
      self.obj1133.graphObject_.pendingConnections.append((self.obj1133.graphObject_.tag, self.obj1131.graphObject_.tag, [439.0, 195.0, 415.5, 158.5], 0, True))
      self.obj1124.out_connections_.append(self.obj1121)
      self.obj1121.in_connections_.append(self.obj1124)
      self.obj1124.graphObject_.pendingConnections.append((self.obj1124.graphObject_.tag, self.obj1121.graphObject_.tag, [154.0, 282.0, 155.5, 264.5], 0, True))
      self.obj1122.out_connections_.append(self.obj1123)
      self.obj1123.in_connections_.append(self.obj1122)
      self.obj1122.graphObject_.pendingConnections.append((self.obj1122.graphObject_.tag, self.obj1123.graphObject_.tag, [163.0, 164.0, 157.5, 147.0], 0, True))
      self.obj1122.out_connections_.append(self.obj1124)
      self.obj1124.in_connections_.append(self.obj1122)
      self.obj1122.graphObject_.pendingConnections.append((self.obj1122.graphObject_.tag, self.obj1124.graphObject_.tag, [157.0, 247.0, 155.5, 264.5], 0, True))
      self.obj1123.out_connections_.append(self.obj1120)
      self.obj1120.in_connections_.append(self.obj1123)
      self.obj1123.graphObject_.pendingConnections.append((self.obj1123.graphObject_.tag, self.obj1120.graphObject_.tag, [152.0, 130.0, 157.5, 147.0], 0, True))

      self.RHS = ASG_RDIS(parent)
      self.RHS.merge(ASG_GenericGraph(parent))
      self.RHS.merge(ASG_ROSApp(parent))

      self.obj1132=RangeAdapter(parent)
      self.obj1132.preAction( self.RHS.CREATE )
      self.obj1132.isGraphObjectVisual = True

      if(hasattr(self.obj1132, '_setHierarchicalLink')):
        self.obj1132._setHierarchicalLink(False)

      # distance
      self.obj1132.distance.setValue('')
      self.obj1132.distance.setNone()

      self.obj1132.GGLabel.setValue(7)
      self.obj1132.graphClass_= graph_RangeAdapter
      if parent.genGraphics:
         new_obj = graph_RangeAdapter(140.0,-20.0,self.obj1132)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1132.graphObject_ = new_obj
      self.obj11320= AttrCalc()
      self.obj11320.Copy=ATOM3Boolean()
      self.obj11320.Copy.setValue(('Copy from LHS', 1))
      self.obj11320.Copy.config = 0
      self.obj11320.Specify=ATOM3Constraint()
      self.obj11320.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1132.GGset2Any['distance']= self.obj11320

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1132)
      self.obj1132.postAction( self.RHS.CREATE )

      self.obj1131=DomainOutput(parent)
      self.obj1131.preAction( self.RHS.CREATE )
      self.obj1131.isGraphObjectVisual = True

      if(hasattr(self.obj1131, '_setHierarchicalLink')):
        self.obj1131._setHierarchicalLink(False)

      # name
      self.obj1131.name.setValue('')
      self.obj1131.name.setNone()

      self.obj1131.GGLabel.setValue(6)
      self.obj1131.graphClass_= graph_DomainOutput
      if parent.genGraphics:
         new_obj = graph_DomainOutput(40.0,140.0,self.obj1131)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1131.graphObject_ = new_obj
      self.obj11310= AttrCalc()
      self.obj11310.Copy=ATOM3Boolean()
      self.obj11310.Copy.setValue(('Copy from LHS', 1))
      self.obj11310.Copy.config = 0
      self.obj11310.Specify=ATOM3Constraint()
      self.obj11310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1131.GGset2Any['name']= self.obj11310

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1131)
      self.obj1131.postAction( self.RHS.CREATE )

      self.obj1133=domainAdapter2domainOutput(parent)
      self.obj1133.preAction( self.RHS.CREATE )
      self.obj1133.isGraphObjectVisual = True

      if(hasattr(self.obj1133, '_setHierarchicalLink')):
        self.obj1133._setHierarchicalLink(False)

      self.obj1133.GGLabel.setValue(8)
      self.obj1133.graphClass_= graph_domainAdapter2domainOutput
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainOutput(415.5,158.5,self.obj1133)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1133.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1133)
      self.obj1133.postAction( self.RHS.CREATE )

      self.obj1148=GenericGraphEdge(parent)
      self.obj1148.preAction( self.RHS.CREATE )
      self.obj1148.isGraphObjectVisual = True

      if(hasattr(self.obj1148, '_setHierarchicalLink')):
        self.obj1148._setHierarchicalLink(False)

      self.obj1148.GGLabel.setValue(10)
      self.obj1148.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(404.25,115.0,self.obj1148)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1148.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1148)
      self.obj1148.postAction( self.RHS.CREATE )

      self.obj1149=GenericGraphEdge(parent)
      self.obj1149.preAction( self.RHS.CREATE )
      self.obj1149.isGraphObjectVisual = True

      if(hasattr(self.obj1149, '_setHierarchicalLink')):
        self.obj1149._setHierarchicalLink(False)

      self.obj1149.GGLabel.setValue(11)
      self.obj1149.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(399.5,171.25,self.obj1149)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1149.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1149)
      self.obj1149.postAction( self.RHS.CREATE )

      self.obj1159=GenericGraphEdge(parent)
      self.obj1159.preAction( self.RHS.CREATE )
      self.obj1159.isGraphObjectVisual = True

      if(hasattr(self.obj1159, '_setHierarchicalLink')):
        self.obj1159._setHierarchicalLink(False)

      self.obj1159.GGLabel.setValue(12)
      self.obj1159.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(278.0,254.0,self.obj1159)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1159.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1159)
      self.obj1159.postAction( self.RHS.CREATE )

      self.obj1124=ROSType(parent)
      self.obj1124.preAction( self.RHS.CREATE )
      self.obj1124.isGraphObjectVisual = True

      if(hasattr(self.obj1124, '_setHierarchicalLink')):
        self.obj1124._setHierarchicalLink(False)

      self.obj1124.GGLabel.setValue(5)
      self.obj1124.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(155.5,264.5,self.obj1124)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1124.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1124)
      self.obj1124.postAction( self.RHS.CREATE )

      self.obj1122=ROSTopic(parent)
      self.obj1122.preAction( self.RHS.CREATE )
      self.obj1122.isGraphObjectVisual = True

      if(hasattr(self.obj1122, '_setHierarchicalLink')):
        self.obj1122._setHierarchicalLink(False)

      # name
      self.obj1122.name.setValue('')
      self.obj1122.name.setNone()

      self.obj1122.GGLabel.setValue(3)
      self.obj1122.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(-160.0,40.0,self.obj1122)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1122.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1122)
      self.obj1122.postAction( self.RHS.CREATE )

      self.obj1121=ROSBoolean(parent)
      self.obj1121.preAction( self.RHS.CREATE )
      self.obj1121.isGraphObjectVisual = True

      if(hasattr(self.obj1121, '_setHierarchicalLink')):
        self.obj1121._setHierarchicalLink(False)

      # data
      self.obj1121.data.setValue('<distance == 0>')

      self.obj1121.GGLabel.setValue(2)
      self.obj1121.graphClass_= graph_ROSBoolean
      if parent.genGraphics:
         new_obj = graph_ROSBoolean(-180.0,200.0,self.obj1121)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1121.graphObject_ = new_obj
      self.obj11210= AttrCalc()
      self.obj11210.Copy=ATOM3Boolean()
      self.obj11210.Copy.setValue(('Copy from LHS', 0))
      self.obj11210.Copy.config = 0
      self.obj11210.Specify=ATOM3Constraint()
      self.obj11210.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj1121.GGset2Any['data']= self.obj11210

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1121)
      self.obj1121.postAction( self.RHS.CREATE )

      self.obj1120=ROSNode(parent)
      self.obj1120.preAction( self.RHS.CREATE )
      self.obj1120.isGraphObjectVisual = True

      if(hasattr(self.obj1120, '_setHierarchicalLink')):
        self.obj1120._setHierarchicalLink(False)

      # name
      self.obj1120.name.setValue('')
      self.obj1120.name.setNone()

      self.obj1120.GGLabel.setValue(1)
      self.obj1120.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(-160.0,-120.0,self.obj1120)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj1120.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1120)
      self.obj1120.postAction( self.RHS.CREATE )

      self.obj1123=ROSSubscribe(parent)
      self.obj1123.preAction( self.RHS.CREATE )
      self.obj1123.isGraphObjectVisual = True

      if(hasattr(self.obj1123, '_setHierarchicalLink')):
        self.obj1123._setHierarchicalLink(False)

      self.obj1123.GGLabel.setValue(4)
      self.obj1123.graphClass_= graph_ROSSubscribe
      if parent.genGraphics:
         new_obj = graph_ROSSubscribe(157.5,147.0,self.obj1123)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj1123.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj1123)
      self.obj1123.postAction( self.RHS.CREATE )

      self.obj1132.out_connections_.append(self.obj1133)
      self.obj1133.in_connections_.append(self.obj1132)
      self.obj1131.out_connections_.append(self.obj1159)
      self.obj1159.in_connections_.append(self.obj1131)
      self.obj1131.graphObject_.pendingConnections.append((self.obj1131.graphObject_.tag, self.obj1159.graphObject_.tag, [326.0, 293.0, 278.0, 254.0], 0, True))
      self.obj1133.out_connections_.append(self.obj1131)
      self.obj1131.in_connections_.append(self.obj1133)
      self.obj1159.out_connections_.append(self.obj1122)
      self.obj1122.in_connections_.append(self.obj1159)
      self.obj1159.graphObject_.pendingConnections.append((self.obj1159.graphObject_.tag, self.obj1122.graphObject_.tag, [230.0, 215.0, 278.0, 254.0], 0, True))
      self.obj1124.out_connections_.append(self.obj1121)
      self.obj1121.in_connections_.append(self.obj1124)
      self.obj1124.graphObject_.pendingConnections.append((self.obj1124.graphObject_.tag, self.obj1121.graphObject_.tag, [136.0, 300.0, 155.5, 264.5], 2, 0))
      self.obj1122.out_connections_.append(self.obj1123)
      self.obj1123.in_connections_.append(self.obj1122)
      self.obj1122.graphObject_.pendingConnections.append((self.obj1122.graphObject_.tag, self.obj1123.graphObject_.tag, [104.0, 191.0, 157.5, 147.0], 2, 0))
      self.obj1122.out_connections_.append(self.obj1124)
      self.obj1124.in_connections_.append(self.obj1122)
      self.obj1122.graphObject_.pendingConnections.append((self.obj1122.graphObject_.tag, self.obj1124.graphObject_.tag, [104.0, 191.0, 155.5, 264.5], 2, 0))
      self.obj1123.out_connections_.append(self.obj1120)
      self.obj1120.in_connections_.append(self.obj1123)
      self.obj1123.graphObject_.pendingConnections.append((self.obj1123.graphObject_.tag, self.obj1120.graphObject_.tag, [117.0, 84.0, 157.5, 147.0], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName45 is not guaranteed to be unique (so change it, be safe!)
      
      node3 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      return not hasattr(node3, "_uniqueName45") and not hasattr(node6, "_uniqueName45")
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName45 is not guaranteed to be unique (so change it, be safe!)
      
      node3 = self.getMatched(graphID, self.LHS.nodeWithLabel(3))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      node3._uniqueName45 = True
      node6._uniqueName45 = True
      
      

