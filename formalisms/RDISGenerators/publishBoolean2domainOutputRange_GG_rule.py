# _ publishBoolean2domainOutputRange_GG_rule.py ____________________________________________________________________________
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
class publishBoolean2domainOutputRange_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_RDIS(parent)
      self.LHS.merge(ASG_ROSApp(parent))

      self.obj219=RangeAdapter(parent)
      self.obj219.preAction( self.LHS.CREATE )
      self.obj219.isGraphObjectVisual = True

      if(hasattr(self.obj219, '_setHierarchicalLink')):
        self.obj219._setHierarchicalLink(False)

      # distance
      self.obj219.distance.setValue('')
      self.obj219.distance.setNone()

      self.obj219.GGLabel.setValue(7)
      self.obj219.graphClass_= graph_RangeAdapter
      if parent.genGraphics:
         new_obj = graph_RangeAdapter(300.0,0.0,self.obj219)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj219.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj219)
      self.obj219.postAction( self.LHS.CREATE )

      self.obj220=DomainOutput(parent)
      self.obj220.preAction( self.LHS.CREATE )
      self.obj220.isGraphObjectVisual = True

      if(hasattr(self.obj220, '_setHierarchicalLink')):
        self.obj220._setHierarchicalLink(False)

      # name
      self.obj220.name.setValue('')
      self.obj220.name.setNone()

      self.obj220.GGLabel.setValue(6)
      self.obj220.graphClass_= graph_DomainOutput
      if parent.genGraphics:
         new_obj = graph_DomainOutput(300.0,140.0,self.obj220)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj220.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj220)
      self.obj220.postAction( self.LHS.CREATE )

      self.obj221=domainAdapter2domainOutput(parent)
      self.obj221.preAction( self.LHS.CREATE )
      self.obj221.isGraphObjectVisual = True

      if(hasattr(self.obj221, '_setHierarchicalLink')):
        self.obj221._setHierarchicalLink(False)

      self.obj221.GGLabel.setValue(8)
      self.obj221.graphClass_= graph_domainAdapter2domainOutput
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainOutput(399.0,148.5,self.obj221)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj221.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj221)
      self.obj221.postAction( self.LHS.CREATE )

      self.obj222=ROSType(parent)
      self.obj222.preAction( self.LHS.CREATE )
      self.obj222.isGraphObjectVisual = True

      if(hasattr(self.obj222, '_setHierarchicalLink')):
        self.obj222._setHierarchicalLink(False)

      self.obj222.GGLabel.setValue(5)
      self.obj222.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(175.5,264.5,self.obj222)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj222.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj222)
      self.obj222.postAction( self.LHS.CREATE )

      self.obj223=ROSPublish(parent)
      self.obj223.preAction( self.LHS.CREATE )
      self.obj223.isGraphObjectVisual = True

      if(hasattr(self.obj223, '_setHierarchicalLink')):
        self.obj223._setHierarchicalLink(False)

      self.obj223.GGLabel.setValue(3)
      self.obj223.graphClass_= graph_ROSPublish
      if parent.genGraphics:
         new_obj = graph_ROSPublish(177.5,147.0,self.obj223)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj223.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj223)
      self.obj223.postAction( self.LHS.CREATE )

      self.obj224=ROSTopic(parent)
      self.obj224.preAction( self.LHS.CREATE )
      self.obj224.isGraphObjectVisual = True

      if(hasattr(self.obj224, '_setHierarchicalLink')):
        self.obj224._setHierarchicalLink(False)

      # name
      self.obj224.name.setValue('')
      self.obj224.name.setNone()

      self.obj224.GGLabel.setValue(2)
      self.obj224.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(100.0,160.0,self.obj224)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj224.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj224)
      self.obj224.postAction( self.LHS.CREATE )

      self.obj225=ROSBoolean(parent)
      self.obj225.preAction( self.LHS.CREATE )
      self.obj225.isGraphObjectVisual = True

      if(hasattr(self.obj225, '_setHierarchicalLink')):
        self.obj225._setHierarchicalLink(False)

      # data
      self.obj225.data.setValue('')
      self.obj225.data.setNone()

      self.obj225.GGLabel.setValue(4)
      self.obj225.graphClass_= graph_ROSBoolean
      if parent.genGraphics:
         new_obj = graph_ROSBoolean(120.0,280.0,self.obj225)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj225.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj225)
      self.obj225.postAction( self.LHS.CREATE )

      self.obj226=ROSNode(parent)
      self.obj226.preAction( self.LHS.CREATE )
      self.obj226.isGraphObjectVisual = True

      if(hasattr(self.obj226, '_setHierarchicalLink')):
        self.obj226._setHierarchicalLink(False)

      # name
      self.obj226.name.setValue('')
      self.obj226.name.setNone()

      self.obj226.GGLabel.setValue(1)
      self.obj226.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(100.0,40.0,self.obj226)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj226.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj226)
      self.obj226.postAction( self.LHS.CREATE )

      self.obj219.out_connections_.append(self.obj221)
      self.obj221.in_connections_.append(self.obj219)
      self.obj219.graphObject_.pendingConnections.append((self.obj219.graphObject_.tag, self.obj221.graphObject_.tag, [379.0, 102.0, 399.0, 148.5], 0, True))
      self.obj221.out_connections_.append(self.obj220)
      self.obj220.in_connections_.append(self.obj221)
      self.obj221.graphObject_.pendingConnections.append((self.obj221.graphObject_.tag, self.obj220.graphObject_.tag, [419.0, 195.0, 399.0, 148.5], 0, True))
      self.obj222.out_connections_.append(self.obj225)
      self.obj225.in_connections_.append(self.obj222)
      self.obj222.graphObject_.pendingConnections.append((self.obj222.graphObject_.tag, self.obj225.graphObject_.tag, [174.0, 282.0, 175.5, 264.5], 0, True))
      self.obj223.out_connections_.append(self.obj224)
      self.obj224.in_connections_.append(self.obj223)
      self.obj223.graphObject_.pendingConnections.append((self.obj223.graphObject_.tag, self.obj224.graphObject_.tag, [183.0, 164.0, 177.5, 147.0], 0, True))
      self.obj224.out_connections_.append(self.obj222)
      self.obj222.in_connections_.append(self.obj224)
      self.obj224.graphObject_.pendingConnections.append((self.obj224.graphObject_.tag, self.obj222.graphObject_.tag, [177.0, 247.0, 175.5, 264.5], 0, True))
      self.obj226.out_connections_.append(self.obj223)
      self.obj223.in_connections_.append(self.obj226)
      self.obj226.graphObject_.pendingConnections.append((self.obj226.graphObject_.tag, self.obj223.graphObject_.tag, [172.0, 130.0, 177.5, 147.0], 0, True))

      self.RHS = ASG_RDIS(parent)
      self.RHS.merge(ASG_ROSApp(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj230=RangeAdapter(parent)
      self.obj230.preAction( self.RHS.CREATE )
      self.obj230.isGraphObjectVisual = True

      if(hasattr(self.obj230, '_setHierarchicalLink')):
        self.obj230._setHierarchicalLink(False)

      # distance
      self.obj230.distance.setValue('')
      self.obj230.distance.setNone()

      self.obj230.GGLabel.setValue(7)
      self.obj230.graphClass_= graph_RangeAdapter
      if parent.genGraphics:
         new_obj = graph_RangeAdapter(300.0,0.0,self.obj230)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj230.graphObject_ = new_obj
      self.obj2300= AttrCalc()
      self.obj2300.Copy=ATOM3Boolean()
      self.obj2300.Copy.setValue(('Copy from LHS', 1))
      self.obj2300.Copy.config = 0
      self.obj2300.Specify=ATOM3Constraint()
      self.obj2300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj230.GGset2Any['distance']= self.obj2300

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj230)
      self.obj230.postAction( self.RHS.CREATE )

      self.obj231=DomainOutput(parent)
      self.obj231.preAction( self.RHS.CREATE )
      self.obj231.isGraphObjectVisual = True

      if(hasattr(self.obj231, '_setHierarchicalLink')):
        self.obj231._setHierarchicalLink(False)

      # name
      self.obj231.name.setValue('')
      self.obj231.name.setNone()

      self.obj231.GGLabel.setValue(6)
      self.obj231.graphClass_= graph_DomainOutput
      if parent.genGraphics:
         new_obj = graph_DomainOutput(200.0,140.0,self.obj231)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj231.graphObject_ = new_obj
      self.obj2310= AttrCalc()
      self.obj2310.Copy=ATOM3Boolean()
      self.obj2310.Copy.setValue(('Copy from LHS', 1))
      self.obj2310.Copy.config = 0
      self.obj2310.Specify=ATOM3Constraint()
      self.obj2310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj231.GGset2Any['name']= self.obj2310

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj231)
      self.obj231.postAction( self.RHS.CREATE )

      self.obj232=domainAdapter2domainOutput(parent)
      self.obj232.preAction( self.RHS.CREATE )
      self.obj232.isGraphObjectVisual = True

      if(hasattr(self.obj232, '_setHierarchicalLink')):
        self.obj232._setHierarchicalLink(False)

      self.obj232.GGLabel.setValue(8)
      self.obj232.graphClass_= graph_domainAdapter2domainOutput
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainOutput(399.0,148.5,self.obj232)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj232.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj232)
      self.obj232.postAction( self.RHS.CREATE )

      self.obj233=ROSType(parent)
      self.obj233.preAction( self.RHS.CREATE )
      self.obj233.isGraphObjectVisual = True

      if(hasattr(self.obj233, '_setHierarchicalLink')):
        self.obj233._setHierarchicalLink(False)

      self.obj233.GGLabel.setValue(5)
      self.obj233.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(175.5,264.5,self.obj233)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj233.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj233)
      self.obj233.postAction( self.RHS.CREATE )

      self.obj234=ROSPublish(parent)
      self.obj234.preAction( self.RHS.CREATE )
      self.obj234.isGraphObjectVisual = True

      if(hasattr(self.obj234, '_setHierarchicalLink')):
        self.obj234._setHierarchicalLink(False)

      self.obj234.GGLabel.setValue(3)
      self.obj234.graphClass_= graph_ROSPublish
      if parent.genGraphics:
         new_obj = graph_ROSPublish(177.5,147.0,self.obj234)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj234.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj234)
      self.obj234.postAction( self.RHS.CREATE )

      self.obj235=ROSTopic(parent)
      self.obj235.preAction( self.RHS.CREATE )
      self.obj235.isGraphObjectVisual = True

      if(hasattr(self.obj235, '_setHierarchicalLink')):
        self.obj235._setHierarchicalLink(False)

      # name
      self.obj235.name.setValue('')
      self.obj235.name.setNone()

      self.obj235.GGLabel.setValue(2)
      self.obj235.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(-160.0,20.0,self.obj235)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj235.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj235)
      self.obj235.postAction( self.RHS.CREATE )

      self.obj236=ROSBoolean(parent)
      self.obj236.preAction( self.RHS.CREATE )
      self.obj236.isGraphObjectVisual = True

      if(hasattr(self.obj236, '_setHierarchicalLink')):
        self.obj236._setHierarchicalLink(False)

      # data
      self.obj236.data.setValue('<distance == 0>')

      self.obj236.GGLabel.setValue(4)
      self.obj236.graphClass_= graph_ROSBoolean
      if parent.genGraphics:
         new_obj = graph_ROSBoolean(-120.0,200.0,self.obj236)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj236.graphObject_ = new_obj
      self.obj2360= AttrCalc()
      self.obj2360.Copy=ATOM3Boolean()
      self.obj2360.Copy.setValue(('Copy from LHS', 0))
      self.obj2360.Copy.config = 0
      self.obj2360.Specify=ATOM3Constraint()
      self.obj2360.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj236.GGset2Any['data']= self.obj2360

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj236)
      self.obj236.postAction( self.RHS.CREATE )

      self.obj237=ROSNode(parent)
      self.obj237.preAction( self.RHS.CREATE )
      self.obj237.isGraphObjectVisual = True

      if(hasattr(self.obj237, '_setHierarchicalLink')):
        self.obj237._setHierarchicalLink(False)

      # name
      self.obj237.name.setValue('')
      self.obj237.name.setNone()

      self.obj237.GGLabel.setValue(1)
      self.obj237.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(-200.0,-140.0,self.obj237)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj237.graphObject_ = new_obj
      self.obj2370= AttrCalc()
      self.obj2370.Copy=ATOM3Boolean()
      self.obj2370.Copy.setValue(('Copy from LHS', 1))
      self.obj2370.Copy.config = 0
      self.obj2370.Specify=ATOM3Constraint()
      self.obj2370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj237.GGset2Any['name']= self.obj2370

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj237)
      self.obj237.postAction( self.RHS.CREATE )

      self.obj238=GenericGraphEdge(parent)
      self.obj238.preAction( self.RHS.CREATE )
      self.obj238.isGraphObjectVisual = True

      if(hasattr(self.obj238, '_setHierarchicalLink')):
        self.obj238._setHierarchicalLink(False)

      self.obj238.GGLabel.setValue(10)
      self.obj238.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(358.0,244.0,self.obj238)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj238.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj238)
      self.obj238.postAction( self.RHS.CREATE )

      self.obj230.out_connections_.append(self.obj232)
      self.obj232.in_connections_.append(self.obj230)
      self.obj230.graphObject_.pendingConnections.append((self.obj230.graphObject_.tag, self.obj232.graphObject_.tag, [499.0, 158.0, 399.0, 148.5], 2, 0))
      self.obj231.out_connections_.append(self.obj238)
      self.obj238.in_connections_.append(self.obj231)
      self.obj231.graphObject_.pendingConnections.append((self.obj231.graphObject_.tag, self.obj238.graphObject_.tag, [486.0, 293.0, 358.0, 244.0], 0, True))
      self.obj232.out_connections_.append(self.obj231)
      self.obj231.in_connections_.append(self.obj232)
      self.obj232.graphObject_.pendingConnections.append((self.obj232.graphObject_.tag, self.obj231.graphObject_.tag, [486.0, 293.0, 399.0, 148.5], 2, 0))
      self.obj233.out_connections_.append(self.obj236)
      self.obj236.in_connections_.append(self.obj233)
      self.obj233.graphObject_.pendingConnections.append((self.obj233.graphObject_.tag, self.obj236.graphObject_.tag, [196.0, 300.0, 175.5, 264.5], 2, 0))
      self.obj234.out_connections_.append(self.obj235)
      self.obj235.in_connections_.append(self.obj234)
      self.obj234.graphObject_.pendingConnections.append((self.obj234.graphObject_.tag, self.obj235.graphObject_.tag, [104.0, 171.0, 177.5, 147.0], 2, 0))
      self.obj235.out_connections_.append(self.obj233)
      self.obj233.in_connections_.append(self.obj235)
      self.obj235.graphObject_.pendingConnections.append((self.obj235.graphObject_.tag, self.obj233.graphObject_.tag, [104.0, 171.0, 175.5, 264.5], 2, 0))
      self.obj237.out_connections_.append(self.obj234)
      self.obj234.in_connections_.append(self.obj237)
      self.obj237.graphObject_.pendingConnections.append((self.obj237.graphObject_.tag, self.obj234.graphObject_.tag, [77.0, 64.0, 177.5, 147.0], 2, 0))
      self.obj238.out_connections_.append(self.obj235)
      self.obj235.in_connections_.append(self.obj238)
      self.obj238.graphObject_.pendingConnections.append((self.obj238.graphObject_.tag, self.obj235.graphObject_.tag, [230.0, 195.0, 358.0, 244.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName35 is not guaranteed to be unique (so change it, be safe!)
      
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      return not hasattr(node2, "_uniqueName35") and not hasattr(node6, "_uniqueName35")
      
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName35 is not guaranteed to be unique (so change it, be safe!)
      
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      node2._uniqueName35 = True
      node6._uniqueName35 = True
      
      

