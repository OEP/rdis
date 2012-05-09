# _ publishTwist2outputDiffSpeedee_GG_rule.py ____________________________________________________________________________
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
class publishTwist2outputDiffSpeedee_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_RDIS(parent)
      self.LHS.merge(ASG_ROSApp(parent))

      self.obj194=DifferentialSpeedAdapter(parent)
      self.obj194.preAction( self.LHS.CREATE )
      self.obj194.isGraphObjectVisual = True

      if(hasattr(self.obj194, '_setHierarchicalLink')):
        self.obj194._setHierarchicalLink(False)

      # angular
      self.obj194.angular.setValue('')
      self.obj194.angular.setNone()

      # linear
      self.obj194.linear.setValue('')
      self.obj194.linear.setNone()

      self.obj194.GGLabel.setValue(7)
      self.obj194.graphClass_= graph_DifferentialSpeedAdapter
      if parent.genGraphics:
         new_obj = graph_DifferentialSpeedAdapter(360.0,20.0,self.obj194)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj194.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj194)
      self.obj194.postAction( self.LHS.CREATE )

      self.obj195=DomainOutput(parent)
      self.obj195.preAction( self.LHS.CREATE )
      self.obj195.isGraphObjectVisual = True

      if(hasattr(self.obj195, '_setHierarchicalLink')):
        self.obj195._setHierarchicalLink(False)

      # name
      self.obj195.name.setValue('')
      self.obj195.name.setNone()

      self.obj195.GGLabel.setValue(6)
      self.obj195.graphClass_= graph_DomainOutput
      if parent.genGraphics:
         new_obj = graph_DomainOutput(340.0,140.0,self.obj195)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj195.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj195)
      self.obj195.postAction( self.LHS.CREATE )

      self.obj196=domainAdapter2domainOutput(parent)
      self.obj196.preAction( self.LHS.CREATE )
      self.obj196.isGraphObjectVisual = True

      if(hasattr(self.obj196, '_setHierarchicalLink')):
        self.obj196._setHierarchicalLink(False)

      self.obj196.GGLabel.setValue(8)
      self.obj196.graphClass_= graph_domainAdapter2domainOutput
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainOutput(446.0,158.0,self.obj196)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj196.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj196)
      self.obj196.postAction( self.LHS.CREATE )

      self.obj197=ROSTwist(parent)
      self.obj197.preAction( self.LHS.CREATE )
      self.obj197.isGraphObjectVisual = True

      if(hasattr(self.obj197, '_setHierarchicalLink')):
        self.obj197._setHierarchicalLink(False)

      # angular
      self.obj197.angular.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('x', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('y', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('z', 20)
      lcobj2.append(cobj2)
      self.obj197.angular.setValue(lcobj2)
      self.obj197.angular.setNone()

      # linear
      self.obj197.linear.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('x', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('y', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('z', 20)
      lcobj2.append(cobj2)
      self.obj197.linear.setValue(lcobj2)
      self.obj197.linear.setNone()

      self.obj197.GGLabel.setValue(4)
      self.obj197.graphClass_= graph_ROSTwist
      if parent.genGraphics:
         new_obj = graph_ROSTwist(100.0,260.0,self.obj197)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj197.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj197)
      self.obj197.postAction( self.LHS.CREATE )

      self.obj198=ROSType(parent)
      self.obj198.preAction( self.LHS.CREATE )
      self.obj198.isGraphObjectVisual = True

      if(hasattr(self.obj198, '_setHierarchicalLink')):
        self.obj198._setHierarchicalLink(False)

      self.obj198.GGLabel.setValue(5)
      self.obj198.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(154.5,256.0,self.obj198)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj198.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj198)
      self.obj198.postAction( self.LHS.CREATE )

      self.obj199=ROSTopic(parent)
      self.obj199.preAction( self.LHS.CREATE )
      self.obj199.isGraphObjectVisual = True

      if(hasattr(self.obj199, '_setHierarchicalLink')):
        self.obj199._setHierarchicalLink(False)

      # name
      self.obj199.name.setValue('')
      self.obj199.name.setNone()

      self.obj199.GGLabel.setValue(2)
      self.obj199.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(80.0,160.0,self.obj199)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj199.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj199)
      self.obj199.postAction( self.LHS.CREATE )

      self.obj200=ROSNode(parent)
      self.obj200.preAction( self.LHS.CREATE )
      self.obj200.isGraphObjectVisual = True

      if(hasattr(self.obj200, '_setHierarchicalLink')):
        self.obj200._setHierarchicalLink(False)

      # name
      self.obj200.name.setValue('')
      self.obj200.name.setNone()

      self.obj200.GGLabel.setValue(1)
      self.obj200.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(80.0,40.0,self.obj200)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj200.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj200)
      self.obj200.postAction( self.LHS.CREATE )

      self.obj201=ROSSubscribe(parent)
      self.obj201.preAction( self.LHS.CREATE )
      self.obj201.isGraphObjectVisual = True

      if(hasattr(self.obj201, '_setHierarchicalLink')):
        self.obj201._setHierarchicalLink(False)

      self.obj201.GGLabel.setValue(3)
      self.obj201.graphClass_= graph_ROSSubscribe
      if parent.genGraphics:
         new_obj = graph_ROSSubscribe(157.5,147.0,self.obj201)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj201.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj201)
      self.obj201.postAction( self.LHS.CREATE )

      self.obj194.out_connections_.append(self.obj196)
      self.obj196.in_connections_.append(self.obj194)
      self.obj194.graphObject_.pendingConnections.append((self.obj194.graphObject_.tag, self.obj196.graphObject_.tag, [433.0, 121.0, 446.0, 158.0], 0, True))
      self.obj196.out_connections_.append(self.obj195)
      self.obj195.in_connections_.append(self.obj196)
      self.obj196.graphObject_.pendingConnections.append((self.obj196.graphObject_.tag, self.obj195.graphObject_.tag, [459.0, 195.0, 446.0, 158.0], 0, True))
      self.obj198.out_connections_.append(self.obj197)
      self.obj197.in_connections_.append(self.obj198)
      self.obj198.graphObject_.pendingConnections.append((self.obj198.graphObject_.tag, self.obj197.graphObject_.tag, [152.0, 265.0, 154.5, 256.0], 0, True))
      self.obj199.out_connections_.append(self.obj201)
      self.obj201.in_connections_.append(self.obj199)
      self.obj199.graphObject_.pendingConnections.append((self.obj199.graphObject_.tag, self.obj201.graphObject_.tag, [163.0, 164.0, 157.5, 147.0], 0, True))
      self.obj199.out_connections_.append(self.obj198)
      self.obj198.in_connections_.append(self.obj199)
      self.obj199.graphObject_.pendingConnections.append((self.obj199.graphObject_.tag, self.obj198.graphObject_.tag, [157.0, 247.0, 154.5, 256.0], 0, True))
      self.obj201.out_connections_.append(self.obj200)
      self.obj200.in_connections_.append(self.obj201)
      self.obj201.graphObject_.pendingConnections.append((self.obj201.graphObject_.tag, self.obj200.graphObject_.tag, [152.0, 130.0, 157.5, 147.0], 0, True))

      self.RHS = ASG_RDIS(parent)
      self.RHS.merge(ASG_ROSApp(parent))
      self.RHS.merge(ASG_GenericGraph(parent))

      self.obj205=DifferentialSpeedAdapter(parent)
      self.obj205.preAction( self.RHS.CREATE )
      self.obj205.isGraphObjectVisual = True

      if(hasattr(self.obj205, '_setHierarchicalLink')):
        self.obj205._setHierarchicalLink(False)

      # angular
      self.obj205.angular.setValue('')
      self.obj205.angular.setNone()

      # linear
      self.obj205.linear.setValue('')
      self.obj205.linear.setNone()

      self.obj205.GGLabel.setValue(7)
      self.obj205.graphClass_= graph_DifferentialSpeedAdapter
      if parent.genGraphics:
         new_obj = graph_DifferentialSpeedAdapter(400.0,20.0,self.obj205)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj205.graphObject_ = new_obj
      self.obj2050= AttrCalc()
      self.obj2050.Copy=ATOM3Boolean()
      self.obj2050.Copy.setValue(('Copy from LHS', 1))
      self.obj2050.Copy.config = 0
      self.obj2050.Specify=ATOM3Constraint()
      self.obj2050.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj205.GGset2Any['angular']= self.obj2050
      self.obj2051= AttrCalc()
      self.obj2051.Copy=ATOM3Boolean()
      self.obj2051.Copy.setValue(('Copy from LHS', 1))
      self.obj2051.Copy.config = 0
      self.obj2051.Specify=ATOM3Constraint()
      self.obj2051.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj205.GGset2Any['linear']= self.obj2051

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj205)
      self.obj205.postAction( self.RHS.CREATE )

      self.obj206=DomainOutput(parent)
      self.obj206.preAction( self.RHS.CREATE )
      self.obj206.isGraphObjectVisual = True

      if(hasattr(self.obj206, '_setHierarchicalLink')):
        self.obj206._setHierarchicalLink(False)

      # name
      self.obj206.name.setValue('')
      self.obj206.name.setNone()

      self.obj206.GGLabel.setValue(6)
      self.obj206.graphClass_= graph_DomainOutput
      if parent.genGraphics:
         new_obj = graph_DomainOutput(200.0,140.0,self.obj206)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj206.graphObject_ = new_obj
      self.obj2060= AttrCalc()
      self.obj2060.Copy=ATOM3Boolean()
      self.obj2060.Copy.setValue(('Copy from LHS', 1))
      self.obj2060.Copy.config = 0
      self.obj2060.Specify=ATOM3Constraint()
      self.obj2060.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj206.GGset2Any['name']= self.obj2060

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj206)
      self.obj206.postAction( self.RHS.CREATE )

      self.obj207=domainAdapter2domainOutput(parent)
      self.obj207.preAction( self.RHS.CREATE )
      self.obj207.isGraphObjectVisual = True

      if(hasattr(self.obj207, '_setHierarchicalLink')):
        self.obj207._setHierarchicalLink(False)

      self.obj207.GGLabel.setValue(8)
      self.obj207.graphClass_= graph_domainAdapter2domainOutput
      if parent.genGraphics:
         new_obj = graph_domainAdapter2domainOutput(446.0,158.0,self.obj207)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj207.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj207)
      self.obj207.postAction( self.RHS.CREATE )

      self.obj208=ROSTwist(parent)
      self.obj208.preAction( self.RHS.CREATE )
      self.obj208.isGraphObjectVisual = True

      if(hasattr(self.obj208, '_setHierarchicalLink')):
        self.obj208._setHierarchicalLink(False)

      # angular
      self.obj208.angular.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('<angular>', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('<0.0>', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('<0.0>', 20)
      lcobj2.append(cobj2)
      self.obj208.angular.setValue(lcobj2)
      self.obj208.angular.setNone()

      # linear
      self.obj208.linear.setActionFlags([ 0, 0, 0, 0])
      lcobj2 =[]
      cobj2=ATOM3String('<linear>', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('<0.0>', 20)
      lcobj2.append(cobj2)
      cobj2=ATOM3String('<0.0>', 20)
      lcobj2.append(cobj2)
      self.obj208.linear.setValue(lcobj2)
      self.obj208.linear.setNone()

      self.obj208.GGLabel.setValue(4)
      self.obj208.graphClass_= graph_ROSTwist
      if parent.genGraphics:
         new_obj = graph_ROSTwist(-100.0,180.0,self.obj208)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj208.graphObject_ = new_obj
      self.obj2080= AttrCalc()
      self.obj2080.Copy=ATOM3Boolean()
      self.obj2080.Copy.setValue(('Copy from LHS', 0))
      self.obj2080.Copy.config = 0
      self.obj2080.Specify=ATOM3Constraint()
      self.obj2080.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj208.GGset2Any['angular']= self.obj2080
      self.obj2081= AttrCalc()
      self.obj2081.Copy=ATOM3Boolean()
      self.obj2081.Copy.setValue(('Copy from LHS', 0))
      self.obj2081.Copy.config = 0
      self.obj2081.Specify=ATOM3Constraint()
      self.obj2081.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj208.GGset2Any['linear']= self.obj2081

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj208)
      self.obj208.postAction( self.RHS.CREATE )

      self.obj209=ROSType(parent)
      self.obj209.preAction( self.RHS.CREATE )
      self.obj209.isGraphObjectVisual = True

      if(hasattr(self.obj209, '_setHierarchicalLink')):
        self.obj209._setHierarchicalLink(False)

      self.obj209.GGLabel.setValue(5)
      self.obj209.graphClass_= graph_ROSType
      if parent.genGraphics:
         new_obj = graph_ROSType(154.5,256.0,self.obj209)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj209.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj209)
      self.obj209.postAction( self.RHS.CREATE )

      self.obj210=ROSTopic(parent)
      self.obj210.preAction( self.RHS.CREATE )
      self.obj210.isGraphObjectVisual = True

      if(hasattr(self.obj210, '_setHierarchicalLink')):
        self.obj210._setHierarchicalLink(False)

      # name
      self.obj210.name.setValue('')
      self.obj210.name.setNone()

      self.obj210.GGLabel.setValue(2)
      self.obj210.graphClass_= graph_ROSTopic
      if parent.genGraphics:
         new_obj = graph_ROSTopic(-140.0,60.0,self.obj210)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj210.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj210)
      self.obj210.postAction( self.RHS.CREATE )

      self.obj211=ROSNode(parent)
      self.obj211.preAction( self.RHS.CREATE )
      self.obj211.isGraphObjectVisual = True

      if(hasattr(self.obj211, '_setHierarchicalLink')):
        self.obj211._setHierarchicalLink(False)

      # name
      self.obj211.name.setValue('')
      self.obj211.name.setNone()

      self.obj211.GGLabel.setValue(1)
      self.obj211.graphClass_= graph_ROSNode
      if parent.genGraphics:
         new_obj = graph_ROSNode(-120.0,-100.0,self.obj211)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj211.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj211)
      self.obj211.postAction( self.RHS.CREATE )

      self.obj212=ROSSubscribe(parent)
      self.obj212.preAction( self.RHS.CREATE )
      self.obj212.isGraphObjectVisual = True

      if(hasattr(self.obj212, '_setHierarchicalLink')):
        self.obj212._setHierarchicalLink(False)

      self.obj212.GGLabel.setValue(3)
      self.obj212.graphClass_= graph_ROSSubscribe
      if parent.genGraphics:
         new_obj = graph_ROSSubscribe(157.5,147.0,self.obj212)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj212.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj212)
      self.obj212.postAction( self.RHS.CREATE )

      self.obj213=GenericGraphEdge(parent)
      self.obj213.preAction( self.RHS.CREATE )
      self.obj213.isGraphObjectVisual = True

      if(hasattr(self.obj213, '_setHierarchicalLink')):
        self.obj213._setHierarchicalLink(False)

      self.obj213.GGLabel.setValue(10)
      self.obj213.graphClass_= graph_GenericGraphEdge
      if parent.genGraphics:
         new_obj = graph_GenericGraphEdge(368.0,264.0,self.obj213)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
      else: new_obj = None
      self.obj213.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj213)
      self.obj213.postAction( self.RHS.CREATE )

      self.obj205.out_connections_.append(self.obj207)
      self.obj207.in_connections_.append(self.obj205)
      self.obj205.graphObject_.pendingConnections.append((self.obj205.graphObject_.tag, self.obj207.graphObject_.tag, [603.0, 164.0, 446.0, 158.0], 2, 0))
      self.obj206.out_connections_.append(self.obj213)
      self.obj213.in_connections_.append(self.obj206)
      self.obj206.graphObject_.pendingConnections.append((self.obj206.graphObject_.tag, self.obj213.graphObject_.tag, [486.0, 293.0, 368.0, 264.0], 0, True))
      self.obj207.out_connections_.append(self.obj206)
      self.obj206.in_connections_.append(self.obj207)
      self.obj207.graphObject_.pendingConnections.append((self.obj207.graphObject_.tag, self.obj206.graphObject_.tag, [486.0, 293.0, 446.0, 158.0], 2, 0))
      self.obj209.out_connections_.append(self.obj208)
      self.obj208.in_connections_.append(self.obj209)
      self.obj209.graphObject_.pendingConnections.append((self.obj209.graphObject_.tag, self.obj208.graphObject_.tag, [101.0, 285.0, 154.5, 256.0], 2, 0))
      self.obj210.out_connections_.append(self.obj212)
      self.obj212.in_connections_.append(self.obj210)
      self.obj210.graphObject_.pendingConnections.append((self.obj210.graphObject_.tag, self.obj212.graphObject_.tag, [124.0, 211.0, 157.5, 147.0], 2, 0))
      self.obj210.out_connections_.append(self.obj209)
      self.obj209.in_connections_.append(self.obj210)
      self.obj210.graphObject_.pendingConnections.append((self.obj210.graphObject_.tag, self.obj209.graphObject_.tag, [124.0, 211.0, 154.5, 256.0], 2, 0))
      self.obj212.out_connections_.append(self.obj211)
      self.obj211.in_connections_.append(self.obj212)
      self.obj212.graphObject_.pendingConnections.append((self.obj212.graphObject_.tag, self.obj211.graphObject_.tag, [157.0, 104.0, 157.5, 147.0], 2, 0))
      self.obj213.out_connections_.append(self.obj210)
      self.obj210.in_connections_.append(self.obj213)
      self.obj213.graphObject_.pendingConnections.append((self.obj213.graphObject_.tag, self.obj210.graphObject_.tag, [250.0, 235.0, 368.0, 264.0], 0, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName27 is not guaranteed to be unique (so change it, be safe!)
      
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      return not hasattr(node2, "_uniqueName27") and not hasattr(node6, "_uniqueName27")
      
      
      

   def action(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the CONDITION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName27 is not guaranteed to be unique (so change it, be safe!)
      
      node2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))
      node6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))
      node2._uniqueName27 = True
      node6._uniqueName27 = True
      
      
      
      

