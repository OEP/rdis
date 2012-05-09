from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('ros2rdis', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('publishTwist2outputDiffSpeedee', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_RDIS(self)
   cobj0.LHS.merge(ASG_ROSApp(self))

   self.obj194=DifferentialSpeedAdapter(self)
   self.obj194.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_DifferentialSpeedAdapter(360.0,20.0,self.obj194)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj194.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj194)
   self.obj194.postAction( cobj0.LHS.CREATE )

   self.obj195=DomainOutput(self)
   self.obj195.preAction( cobj0.LHS.CREATE )
   self.obj195.isGraphObjectVisual = True

   if(hasattr(self.obj195, '_setHierarchicalLink')):
     self.obj195._setHierarchicalLink(False)

   # name
   self.obj195.name.setValue('')
   self.obj195.name.setNone()

   self.obj195.GGLabel.setValue(6)
   self.obj195.graphClass_= graph_DomainOutput
   if self.genGraphics:
      new_obj = graph_DomainOutput(340.0,140.0,self.obj195)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj195.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj195)
   self.obj195.postAction( cobj0.LHS.CREATE )

   self.obj196=domainAdapter2domainOutput(self)
   self.obj196.preAction( cobj0.LHS.CREATE )
   self.obj196.isGraphObjectVisual = True

   if(hasattr(self.obj196, '_setHierarchicalLink')):
     self.obj196._setHierarchicalLink(False)

   self.obj196.GGLabel.setValue(8)
   self.obj196.graphClass_= graph_domainAdapter2domainOutput
   if self.genGraphics:
      new_obj = graph_domainAdapter2domainOutput(446.0,158.0,self.obj196)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj196.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj196)
   self.obj196.postAction( cobj0.LHS.CREATE )

   self.obj197=ROSTwist(self)
   self.obj197.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_ROSTwist(100.0,260.0,self.obj197)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj197.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj197)
   self.obj197.postAction( cobj0.LHS.CREATE )

   self.obj198=ROSType(self)
   self.obj198.preAction( cobj0.LHS.CREATE )
   self.obj198.isGraphObjectVisual = True

   if(hasattr(self.obj198, '_setHierarchicalLink')):
     self.obj198._setHierarchicalLink(False)

   self.obj198.GGLabel.setValue(5)
   self.obj198.graphClass_= graph_ROSType
   if self.genGraphics:
      new_obj = graph_ROSType(154.5,256.0,self.obj198)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj198.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj198)
   self.obj198.postAction( cobj0.LHS.CREATE )

   self.obj199=ROSTopic(self)
   self.obj199.preAction( cobj0.LHS.CREATE )
   self.obj199.isGraphObjectVisual = True

   if(hasattr(self.obj199, '_setHierarchicalLink')):
     self.obj199._setHierarchicalLink(False)

   # name
   self.obj199.name.setValue('')
   self.obj199.name.setNone()

   self.obj199.GGLabel.setValue(2)
   self.obj199.graphClass_= graph_ROSTopic
   if self.genGraphics:
      new_obj = graph_ROSTopic(80.0,160.0,self.obj199)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj199.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj199)
   self.obj199.postAction( cobj0.LHS.CREATE )

   self.obj200=ROSNode(self)
   self.obj200.preAction( cobj0.LHS.CREATE )
   self.obj200.isGraphObjectVisual = True

   if(hasattr(self.obj200, '_setHierarchicalLink')):
     self.obj200._setHierarchicalLink(False)

   # name
   self.obj200.name.setValue('')
   self.obj200.name.setNone()

   self.obj200.GGLabel.setValue(1)
   self.obj200.graphClass_= graph_ROSNode
   if self.genGraphics:
      new_obj = graph_ROSNode(80.0,40.0,self.obj200)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj200.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj200)
   self.obj200.postAction( cobj0.LHS.CREATE )

   self.obj201=ROSSubscribe(self)
   self.obj201.preAction( cobj0.LHS.CREATE )
   self.obj201.isGraphObjectVisual = True

   if(hasattr(self.obj201, '_setHierarchicalLink')):
     self.obj201._setHierarchicalLink(False)

   self.obj201.GGLabel.setValue(3)
   self.obj201.graphClass_= graph_ROSSubscribe
   if self.genGraphics:
      new_obj = graph_ROSSubscribe(157.5,147.0,self.obj201)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj201.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj201)
   self.obj201.postAction( cobj0.LHS.CREATE )

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

   cobj0.RHS = ASG_RDIS(self)
   cobj0.RHS.merge(ASG_ROSApp(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj205=DifferentialSpeedAdapter(self)
   self.obj205.preAction( cobj0.RHS.CREATE )
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
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj205)
   self.obj205.postAction( cobj0.RHS.CREATE )

   self.obj206=DomainOutput(self)
   self.obj206.preAction( cobj0.RHS.CREATE )
   self.obj206.isGraphObjectVisual = True

   if(hasattr(self.obj206, '_setHierarchicalLink')):
     self.obj206._setHierarchicalLink(False)

   # name
   self.obj206.name.setValue('')
   self.obj206.name.setNone()

   self.obj206.GGLabel.setValue(6)
   self.obj206.graphClass_= graph_DomainOutput
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj206)
   self.obj206.postAction( cobj0.RHS.CREATE )

   self.obj207=domainAdapter2domainOutput(self)
   self.obj207.preAction( cobj0.RHS.CREATE )
   self.obj207.isGraphObjectVisual = True

   if(hasattr(self.obj207, '_setHierarchicalLink')):
     self.obj207._setHierarchicalLink(False)

   self.obj207.GGLabel.setValue(8)
   self.obj207.graphClass_= graph_domainAdapter2domainOutput
   if self.genGraphics:
      new_obj = graph_domainAdapter2domainOutput(446.0,158.0,self.obj207)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj207.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj207)
   self.obj207.postAction( cobj0.RHS.CREATE )

   self.obj208=ROSTwist(self)
   self.obj208.preAction( cobj0.RHS.CREATE )
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
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj208)
   self.obj208.postAction( cobj0.RHS.CREATE )

   self.obj209=ROSType(self)
   self.obj209.preAction( cobj0.RHS.CREATE )
   self.obj209.isGraphObjectVisual = True

   if(hasattr(self.obj209, '_setHierarchicalLink')):
     self.obj209._setHierarchicalLink(False)

   self.obj209.GGLabel.setValue(5)
   self.obj209.graphClass_= graph_ROSType
   if self.genGraphics:
      new_obj = graph_ROSType(154.5,256.0,self.obj209)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj209.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj209)
   self.obj209.postAction( cobj0.RHS.CREATE )

   self.obj210=ROSTopic(self)
   self.obj210.preAction( cobj0.RHS.CREATE )
   self.obj210.isGraphObjectVisual = True

   if(hasattr(self.obj210, '_setHierarchicalLink')):
     self.obj210._setHierarchicalLink(False)

   # name
   self.obj210.name.setValue('')
   self.obj210.name.setNone()

   self.obj210.GGLabel.setValue(2)
   self.obj210.graphClass_= graph_ROSTopic
   if self.genGraphics:
      new_obj = graph_ROSTopic(-140.0,60.0,self.obj210)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj210.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj210)
   self.obj210.postAction( cobj0.RHS.CREATE )

   self.obj211=ROSNode(self)
   self.obj211.preAction( cobj0.RHS.CREATE )
   self.obj211.isGraphObjectVisual = True

   if(hasattr(self.obj211, '_setHierarchicalLink')):
     self.obj211._setHierarchicalLink(False)

   # name
   self.obj211.name.setValue('')
   self.obj211.name.setNone()

   self.obj211.GGLabel.setValue(1)
   self.obj211.graphClass_= graph_ROSNode
   if self.genGraphics:
      new_obj = graph_ROSNode(-120.0,-100.0,self.obj211)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj211.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj211)
   self.obj211.postAction( cobj0.RHS.CREATE )

   self.obj212=ROSSubscribe(self)
   self.obj212.preAction( cobj0.RHS.CREATE )
   self.obj212.isGraphObjectVisual = True

   if(hasattr(self.obj212, '_setHierarchicalLink')):
     self.obj212._setHierarchicalLink(False)

   self.obj212.GGLabel.setValue(3)
   self.obj212.graphClass_= graph_ROSSubscribe
   if self.genGraphics:
      new_obj = graph_ROSSubscribe(157.5,147.0,self.obj212)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj212.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj212)
   self.obj212.postAction( cobj0.RHS.CREATE )

   self.obj213=GenericGraphEdge(self)
   self.obj213.preAction( cobj0.RHS.CREATE )
   self.obj213.isGraphObjectVisual = True

   if(hasattr(self.obj213, '_setHierarchicalLink')):
     self.obj213._setHierarchicalLink(False)

   self.obj213.GGLabel.setValue(10)
   self.obj213.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(368.0,264.0,self.obj213)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj213.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj213)
   self.obj213.postAction( cobj0.RHS.CREATE )

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

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName27 is not guaranteed to be unique (so change it, be safe!)\n\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nnode6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))\nreturn not hasattr(node2, "_uniqueName27") and not hasattr(node6, "_uniqueName27")\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName27 is not guaranteed to be unique (so change it, be safe!)\n\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nnode6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))\nnode2._uniqueName27 = True\nnode6._uniqueName27 = True\n\n\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('publishBoolean2domainOutputRange', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_RDIS(self)
   cobj0.LHS.merge(ASG_ROSApp(self))

   self.obj219=RangeAdapter(self)
   self.obj219.preAction( cobj0.LHS.CREATE )
   self.obj219.isGraphObjectVisual = True

   if(hasattr(self.obj219, '_setHierarchicalLink')):
     self.obj219._setHierarchicalLink(False)

   # distance
   self.obj219.distance.setValue('')
   self.obj219.distance.setNone()

   self.obj219.GGLabel.setValue(7)
   self.obj219.graphClass_= graph_RangeAdapter
   if self.genGraphics:
      new_obj = graph_RangeAdapter(300.0,0.0,self.obj219)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj219.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj219)
   self.obj219.postAction( cobj0.LHS.CREATE )

   self.obj220=DomainOutput(self)
   self.obj220.preAction( cobj0.LHS.CREATE )
   self.obj220.isGraphObjectVisual = True

   if(hasattr(self.obj220, '_setHierarchicalLink')):
     self.obj220._setHierarchicalLink(False)

   # name
   self.obj220.name.setValue('')
   self.obj220.name.setNone()

   self.obj220.GGLabel.setValue(6)
   self.obj220.graphClass_= graph_DomainOutput
   if self.genGraphics:
      new_obj = graph_DomainOutput(300.0,140.0,self.obj220)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj220.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj220)
   self.obj220.postAction( cobj0.LHS.CREATE )

   self.obj221=domainAdapter2domainOutput(self)
   self.obj221.preAction( cobj0.LHS.CREATE )
   self.obj221.isGraphObjectVisual = True

   if(hasattr(self.obj221, '_setHierarchicalLink')):
     self.obj221._setHierarchicalLink(False)

   self.obj221.GGLabel.setValue(8)
   self.obj221.graphClass_= graph_domainAdapter2domainOutput
   if self.genGraphics:
      new_obj = graph_domainAdapter2domainOutput(399.0,148.5,self.obj221)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj221.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj221)
   self.obj221.postAction( cobj0.LHS.CREATE )

   self.obj222=ROSType(self)
   self.obj222.preAction( cobj0.LHS.CREATE )
   self.obj222.isGraphObjectVisual = True

   if(hasattr(self.obj222, '_setHierarchicalLink')):
     self.obj222._setHierarchicalLink(False)

   self.obj222.GGLabel.setValue(5)
   self.obj222.graphClass_= graph_ROSType
   if self.genGraphics:
      new_obj = graph_ROSType(175.5,264.5,self.obj222)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj222.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj222)
   self.obj222.postAction( cobj0.LHS.CREATE )

   self.obj223=ROSPublish(self)
   self.obj223.preAction( cobj0.LHS.CREATE )
   self.obj223.isGraphObjectVisual = True

   if(hasattr(self.obj223, '_setHierarchicalLink')):
     self.obj223._setHierarchicalLink(False)

   self.obj223.GGLabel.setValue(3)
   self.obj223.graphClass_= graph_ROSPublish
   if self.genGraphics:
      new_obj = graph_ROSPublish(177.5,147.0,self.obj223)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj223.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj223)
   self.obj223.postAction( cobj0.LHS.CREATE )

   self.obj224=ROSTopic(self)
   self.obj224.preAction( cobj0.LHS.CREATE )
   self.obj224.isGraphObjectVisual = True

   if(hasattr(self.obj224, '_setHierarchicalLink')):
     self.obj224._setHierarchicalLink(False)

   # name
   self.obj224.name.setValue('')
   self.obj224.name.setNone()

   self.obj224.GGLabel.setValue(2)
   self.obj224.graphClass_= graph_ROSTopic
   if self.genGraphics:
      new_obj = graph_ROSTopic(100.0,160.0,self.obj224)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj224.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj224)
   self.obj224.postAction( cobj0.LHS.CREATE )

   self.obj225=ROSBoolean(self)
   self.obj225.preAction( cobj0.LHS.CREATE )
   self.obj225.isGraphObjectVisual = True

   if(hasattr(self.obj225, '_setHierarchicalLink')):
     self.obj225._setHierarchicalLink(False)

   # data
   self.obj225.data.setValue('')
   self.obj225.data.setNone()

   self.obj225.GGLabel.setValue(4)
   self.obj225.graphClass_= graph_ROSBoolean
   if self.genGraphics:
      new_obj = graph_ROSBoolean(120.0,280.0,self.obj225)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj225.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj225)
   self.obj225.postAction( cobj0.LHS.CREATE )

   self.obj226=ROSNode(self)
   self.obj226.preAction( cobj0.LHS.CREATE )
   self.obj226.isGraphObjectVisual = True

   if(hasattr(self.obj226, '_setHierarchicalLink')):
     self.obj226._setHierarchicalLink(False)

   # name
   self.obj226.name.setValue('')
   self.obj226.name.setNone()

   self.obj226.GGLabel.setValue(1)
   self.obj226.graphClass_= graph_ROSNode
   if self.genGraphics:
      new_obj = graph_ROSNode(100.0,40.0,self.obj226)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj226.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj226)
   self.obj226.postAction( cobj0.LHS.CREATE )

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

   cobj0.RHS = ASG_RDIS(self)
   cobj0.RHS.merge(ASG_ROSApp(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj230=RangeAdapter(self)
   self.obj230.preAction( cobj0.RHS.CREATE )
   self.obj230.isGraphObjectVisual = True

   if(hasattr(self.obj230, '_setHierarchicalLink')):
     self.obj230._setHierarchicalLink(False)

   # distance
   self.obj230.distance.setValue('')
   self.obj230.distance.setNone()

   self.obj230.GGLabel.setValue(7)
   self.obj230.graphClass_= graph_RangeAdapter
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj230)
   self.obj230.postAction( cobj0.RHS.CREATE )

   self.obj231=DomainOutput(self)
   self.obj231.preAction( cobj0.RHS.CREATE )
   self.obj231.isGraphObjectVisual = True

   if(hasattr(self.obj231, '_setHierarchicalLink')):
     self.obj231._setHierarchicalLink(False)

   # name
   self.obj231.name.setValue('')
   self.obj231.name.setNone()

   self.obj231.GGLabel.setValue(6)
   self.obj231.graphClass_= graph_DomainOutput
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj231)
   self.obj231.postAction( cobj0.RHS.CREATE )

   self.obj232=domainAdapter2domainOutput(self)
   self.obj232.preAction( cobj0.RHS.CREATE )
   self.obj232.isGraphObjectVisual = True

   if(hasattr(self.obj232, '_setHierarchicalLink')):
     self.obj232._setHierarchicalLink(False)

   self.obj232.GGLabel.setValue(8)
   self.obj232.graphClass_= graph_domainAdapter2domainOutput
   if self.genGraphics:
      new_obj = graph_domainAdapter2domainOutput(399.0,148.5,self.obj232)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj232.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj232)
   self.obj232.postAction( cobj0.RHS.CREATE )

   self.obj233=ROSType(self)
   self.obj233.preAction( cobj0.RHS.CREATE )
   self.obj233.isGraphObjectVisual = True

   if(hasattr(self.obj233, '_setHierarchicalLink')):
     self.obj233._setHierarchicalLink(False)

   self.obj233.GGLabel.setValue(5)
   self.obj233.graphClass_= graph_ROSType
   if self.genGraphics:
      new_obj = graph_ROSType(175.5,264.5,self.obj233)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj233.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj233)
   self.obj233.postAction( cobj0.RHS.CREATE )

   self.obj234=ROSPublish(self)
   self.obj234.preAction( cobj0.RHS.CREATE )
   self.obj234.isGraphObjectVisual = True

   if(hasattr(self.obj234, '_setHierarchicalLink')):
     self.obj234._setHierarchicalLink(False)

   self.obj234.GGLabel.setValue(3)
   self.obj234.graphClass_= graph_ROSPublish
   if self.genGraphics:
      new_obj = graph_ROSPublish(177.5,147.0,self.obj234)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj234.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj234)
   self.obj234.postAction( cobj0.RHS.CREATE )

   self.obj235=ROSTopic(self)
   self.obj235.preAction( cobj0.RHS.CREATE )
   self.obj235.isGraphObjectVisual = True

   if(hasattr(self.obj235, '_setHierarchicalLink')):
     self.obj235._setHierarchicalLink(False)

   # name
   self.obj235.name.setValue('')
   self.obj235.name.setNone()

   self.obj235.GGLabel.setValue(2)
   self.obj235.graphClass_= graph_ROSTopic
   if self.genGraphics:
      new_obj = graph_ROSTopic(-160.0,20.0,self.obj235)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj235.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj235)
   self.obj235.postAction( cobj0.RHS.CREATE )

   self.obj236=ROSBoolean(self)
   self.obj236.preAction( cobj0.RHS.CREATE )
   self.obj236.isGraphObjectVisual = True

   if(hasattr(self.obj236, '_setHierarchicalLink')):
     self.obj236._setHierarchicalLink(False)

   # data
   self.obj236.data.setValue('<distance == 0>')

   self.obj236.GGLabel.setValue(4)
   self.obj236.graphClass_= graph_ROSBoolean
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj236)
   self.obj236.postAction( cobj0.RHS.CREATE )

   self.obj237=ROSNode(self)
   self.obj237.preAction( cobj0.RHS.CREATE )
   self.obj237.isGraphObjectVisual = True

   if(hasattr(self.obj237, '_setHierarchicalLink')):
     self.obj237._setHierarchicalLink(False)

   # name
   self.obj237.name.setValue('')
   self.obj237.name.setNone()

   self.obj237.GGLabel.setValue(1)
   self.obj237.graphClass_= graph_ROSNode
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj237)
   self.obj237.postAction( cobj0.RHS.CREATE )

   self.obj238=GenericGraphEdge(self)
   self.obj238.preAction( cobj0.RHS.CREATE )
   self.obj238.isGraphObjectVisual = True

   if(hasattr(self.obj238, '_setHierarchicalLink')):
     self.obj238._setHierarchicalLink(False)

   self.obj238.GGLabel.setValue(10)
   self.obj238.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(358.0,244.0,self.obj238)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj238.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj238)
   self.obj238.postAction( cobj0.RHS.CREATE )

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

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName35 is not guaranteed to be unique (so change it, be safe!)\n\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nnode6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))\nreturn not hasattr(node2, "_uniqueName35") and not hasattr(node6, "_uniqueName35")\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName35 is not guaranteed to be unique (so change it, be safe!)\n\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nnode6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))\nnode2._uniqueName35 = True\nnode6._uniqueName35 = True\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('subscribeTwist2interfaceDiffSpeede', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_RDIS(self)
   cobj0.LHS.merge(ASG_ROSApp(self))

   self.obj503=DifferentialSpeedAdapter(self)
   self.obj503.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_DifferentialSpeedAdapter(320.0,0.0,self.obj503)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj503.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj503)
   self.obj503.postAction( cobj0.LHS.CREATE )

   self.obj500=DomainInterface(self)
   self.obj500.preAction( cobj0.LHS.CREATE )
   self.obj500.isGraphObjectVisual = True

   if(hasattr(self.obj500, '_setHierarchicalLink')):
     self.obj500._setHierarchicalLink(False)

   # name
   self.obj500.name.setValue('')
   self.obj500.name.setNone()

   self.obj500.GGLabel.setValue(6)
   self.obj500.graphClass_= graph_DomainInterface
   if self.genGraphics:
      new_obj = graph_DomainInterface(300.0,180.0,self.obj500)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj500.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj500)
   self.obj500.postAction( cobj0.LHS.CREATE )

   self.obj504=domainAdapter2domainInterface(self)
   self.obj504.preAction( cobj0.LHS.CREATE )
   self.obj504.isGraphObjectVisual = True

   if(hasattr(self.obj504, '_setHierarchicalLink')):
     self.obj504._setHierarchicalLink(False)

   self.obj504.GGLabel.setValue(8)
   self.obj504.graphClass_= graph_domainAdapter2domainInterface
   if self.genGraphics:
      new_obj = graph_domainAdapter2domainInterface(452.5,155.0,self.obj504)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj504.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj504)
   self.obj504.postAction( cobj0.LHS.CREATE )

   self.obj492=ROSTwist(self)
   self.obj492.preAction( cobj0.LHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_ROSTwist(80.0,320.0,self.obj492)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj492.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj492)
   self.obj492.postAction( cobj0.LHS.CREATE )

   self.obj493=ROSType(self)
   self.obj493.preAction( cobj0.LHS.CREATE )
   self.obj493.isGraphObjectVisual = True

   if(hasattr(self.obj493, '_setHierarchicalLink')):
     self.obj493._setHierarchicalLink(False)

   self.obj493.GGLabel.setValue(5)
   self.obj493.graphClass_= graph_ROSType
   if self.genGraphics:
      new_obj = graph_ROSType(87.0,301.0,self.obj493)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj493.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj493)
   self.obj493.postAction( cobj0.LHS.CREATE )

   self.obj490=ROSTopic(self)
   self.obj490.preAction( cobj0.LHS.CREATE )
   self.obj490.isGraphObjectVisual = True

   if(hasattr(self.obj490, '_setHierarchicalLink')):
     self.obj490._setHierarchicalLink(False)

   # name
   self.obj490.name.setValue('')
   self.obj490.name.setNone()

   self.obj490.GGLabel.setValue(2)
   self.obj490.graphClass_= graph_ROSTopic
   if self.genGraphics:
      new_obj = graph_ROSTopic(80.0,180.0,self.obj490)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj490.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj490)
   self.obj490.postAction( cobj0.LHS.CREATE )

   self.obj489=ROSNode(self)
   self.obj489.preAction( cobj0.LHS.CREATE )
   self.obj489.isGraphObjectVisual = True

   if(hasattr(self.obj489, '_setHierarchicalLink')):
     self.obj489._setHierarchicalLink(False)

   # name
   self.obj489.name.setValue('')
   self.obj489.name.setNone()

   self.obj489.GGLabel.setValue(1)
   self.obj489.graphClass_= graph_ROSNode
   if self.genGraphics:
      new_obj = graph_ROSNode(80.0,40.0,self.obj489)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj489.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj489)
   self.obj489.postAction( cobj0.LHS.CREATE )

   self.obj491=ROSSubscribe(self)
   self.obj491.preAction( cobj0.LHS.CREATE )
   self.obj491.isGraphObjectVisual = True

   if(hasattr(self.obj491, '_setHierarchicalLink')):
     self.obj491._setHierarchicalLink(False)

   self.obj491.GGLabel.setValue(3)
   self.obj491.graphClass_= graph_ROSSubscribe
   if self.genGraphics:
      new_obj = graph_ROSSubscribe(157.5,157.0,self.obj491)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj491.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj491)
   self.obj491.postAction( cobj0.LHS.CREATE )

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

   cobj0.RHS = ASG_RDIS(self)
   cobj0.RHS.merge(ASG_ROSApp(self))
   cobj0.RHS.merge(ASG_GenericGraph(self))

   self.obj503=DifferentialSpeedAdapter(self)
   self.obj503.preAction( cobj0.RHS.CREATE )
   self.obj503.isGraphObjectVisual = True

   if(hasattr(self.obj503, '_setHierarchicalLink')):
     self.obj503._setHierarchicalLink(False)

   # angular
   self.obj503.angular.setValue('<angular[0]>')

   # linear
   self.obj503.linear.setValue('<linear[0]>')

   self.obj503.GGLabel.setValue(7)
   self.obj503.graphClass_= graph_DifferentialSpeedAdapter
   if self.genGraphics:
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

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj503)
   self.obj503.postAction( cobj0.RHS.CREATE )

   self.obj500=DomainInterface(self)
   self.obj500.preAction( cobj0.RHS.CREATE )
   self.obj500.isGraphObjectVisual = True

   if(hasattr(self.obj500, '_setHierarchicalLink')):
     self.obj500._setHierarchicalLink(False)

   # name
   self.obj500.name.setValue('')
   self.obj500.name.setNone()

   self.obj500.GGLabel.setValue(6)
   self.obj500.graphClass_= graph_DomainInterface
   if self.genGraphics:
      new_obj = graph_DomainInterface(300.0,80.0,self.obj500)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj500.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj500)
   self.obj500.postAction( cobj0.RHS.CREATE )

   self.obj504=domainAdapter2domainInterface(self)
   self.obj504.preAction( cobj0.RHS.CREATE )
   self.obj504.isGraphObjectVisual = True

   if(hasattr(self.obj504, '_setHierarchicalLink')):
     self.obj504._setHierarchicalLink(False)

   self.obj504.GGLabel.setValue(8)
   self.obj504.graphClass_= graph_domainAdapter2domainInterface
   if self.genGraphics:
      new_obj = graph_domainAdapter2domainInterface(452.5,155.0,self.obj504)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj504.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj504)
   self.obj504.postAction( cobj0.RHS.CREATE )

   self.obj492=ROSTwist(self)
   self.obj492.preAction( cobj0.RHS.CREATE )
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
   if self.genGraphics:
      new_obj = graph_ROSTwist(80.0,260.0,self.obj492)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj492.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj492)
   self.obj492.postAction( cobj0.RHS.CREATE )

   self.obj493=ROSType(self)
   self.obj493.preAction( cobj0.RHS.CREATE )
   self.obj493.isGraphObjectVisual = True

   if(hasattr(self.obj493, '_setHierarchicalLink')):
     self.obj493._setHierarchicalLink(False)

   self.obj493.GGLabel.setValue(5)
   self.obj493.graphClass_= graph_ROSType
   if self.genGraphics:
      new_obj = graph_ROSType(87.0,301.0,self.obj493)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj493.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj493)
   self.obj493.postAction( cobj0.RHS.CREATE )

   self.obj490=ROSTopic(self)
   self.obj490.preAction( cobj0.RHS.CREATE )
   self.obj490.isGraphObjectVisual = True

   if(hasattr(self.obj490, '_setHierarchicalLink')):
     self.obj490._setHierarchicalLink(False)

   # name
   self.obj490.name.setValue('')
   self.obj490.name.setNone()

   self.obj490.GGLabel.setValue(2)
   self.obj490.graphClass_= graph_ROSTopic
   if self.genGraphics:
      new_obj = graph_ROSTopic(80.0,80.0,self.obj490)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj490.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj490)
   self.obj490.postAction( cobj0.RHS.CREATE )

   self.obj489=ROSNode(self)
   self.obj489.preAction( cobj0.RHS.CREATE )
   self.obj489.isGraphObjectVisual = True

   if(hasattr(self.obj489, '_setHierarchicalLink')):
     self.obj489._setHierarchicalLink(False)

   # name
   self.obj489.name.setValue('')
   self.obj489.name.setNone()

   self.obj489.GGLabel.setValue(1)
   self.obj489.graphClass_= graph_ROSNode
   if self.genGraphics:
      new_obj = graph_ROSNode(80.0,-140.0,self.obj489)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj489.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj489)
   self.obj489.postAction( cobj0.RHS.CREATE )

   self.obj491=ROSSubscribe(self)
   self.obj491.preAction( cobj0.RHS.CREATE )
   self.obj491.isGraphObjectVisual = True

   if(hasattr(self.obj491, '_setHierarchicalLink')):
     self.obj491._setHierarchicalLink(False)

   self.obj491.GGLabel.setValue(3)
   self.obj491.graphClass_= graph_ROSSubscribe
   if self.genGraphics:
      new_obj = graph_ROSSubscribe(157.5,157.0,self.obj491)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj491.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj491)
   self.obj491.postAction( cobj0.RHS.CREATE )

   self.obj517=GenericGraphEdge(self)
   self.obj517.preAction( cobj0.RHS.CREATE )
   self.obj517.isGraphObjectVisual = True

   if(hasattr(self.obj517, '_setHierarchicalLink')):
     self.obj517._setHierarchicalLink(False)

   self.obj517.GGLabel.setValue(10)
   self.obj517.graphClass_= graph_GenericGraphEdge
   if self.genGraphics:
      new_obj = graph_GenericGraphEdge(261.0,226.5,self.obj517)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
   else: new_obj = None
   self.obj517.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj517)
   self.obj517.postAction( cobj0.RHS.CREATE )

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

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName20 is not guaranteed to be unique (so change it, be safe!)\n\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nnode6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))\nreturn not hasattr(node2, "_uniqueName20") and not hasattr(node6, "_uniqueName20")\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the CONDITION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName20 is not guaranteed to be unique (so change it, be safe!)\n\nnode2 = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\nnode6 = self.getMatched(graphID, self.LHS.nodeWithLabel(6))\nnode2._uniqueName20 = True\nnode6._uniqueName20 = True\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


