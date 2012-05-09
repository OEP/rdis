"""
__iRobot_Create_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: pkilgo
Modified: Mon Apr 30 14:08:31 2012
___________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from DifferentialSpeedAdapter import *
from SerialConnection import *
from SingleThreading import *
from Primitive import *
from Interface import *
from StateVariable import *
from RangeAdapter import *
from DomainInterface import *
from DomainOutput import *
from interface2primitive import *
from primitive2connection import *
from connection2threading import *
from connectionStartup import *
from connectionKeepalive import *
from connectionTerminate import *
from domainInterface2Interface import *
from domainAdapter2domainOutput import *
from domainAdapter2domainInterface import *
from interface2domainOutput import *
from graph_interface2domainOutput import *
from graph_interface2primitive import *
from graph_connection2threading import *
from graph_DifferentialSpeedAdapter import *
from graph_connectionTerminate import *
from graph_DomainInterface import *
from graph_SingleThreading import *
from graph_Primitive import *
from graph_connectionKeepalive import *
from graph_StateVariable import *
from graph_SerialConnection import *
from graph_DomainOutput import *
from graph_domainInterface2Interface import *
from graph_domainAdapter2domainInterface import *
from graph_primitive2connection import *
from graph_Interface import *
from graph_RangeAdapter import *
from graph_domainAdapter2domainOutput import *
from graph_connectionStartup import *
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

def iRobot_Create_MDL(self, rootNode, RDISRootNode=None):

    # --- Generating attributes code for ASG RDIS ---
    if( RDISRootNode ): 
        # author
        RDISRootNode.author.setValue('Paul Kilgo')

        # description
        RDISRootNode.description.setValue('\n')
        RDISRootNode.description.setHeight(15)

        # name
        RDISRootNode.name.setValue('irobotCreate')
    # --- ASG attributes over ---


    self.obj29=DifferentialSpeedAdapter(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # angular
    self.obj29.angular.setValue('')
    self.obj29.angular.setNone()

    # linear
    self.obj29.linear.setValue('')
    self.obj29.linear.setNone()

    self.obj29.graphClass_= graph_DifferentialSpeedAdapter
    if self.genGraphics:
       new_obj = graph_DifferentialSpeedAdapter(380.0,340.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("DifferentialSpeedAdapter", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=SerialConnection(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # baud
    self.obj30.baud.setValue(57600)

    # name
    self.obj30.name.setValue('btserial')

    self.obj30.graphClass_= graph_SerialConnection
    if self.genGraphics:
       new_obj = graph_SerialConnection(0.0,100.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SerialConnection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=SingleThreading(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # freqHz
    self.obj31.freqHz.setValue(40)

    self.obj31.graphClass_= graph_SingleThreading
    if self.genGraphics:
       new_obj = graph_SingleThreading(20.0,20.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SingleThreading", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=Primitive(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # postActions
    self.obj32.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.postActions.setValue(lcobj2)

    # regex
    self.obj32.regex.setValue('')
    self.obj32.regex.setNone()

    # name
    self.obj32.name.setValue('start')

    # parameters
    self.obj32.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.parameters.setValue(lcobj2)

    # format
    self.obj32.format.setValue('')
    self.obj32.format.setNone()

    # formatArgs
    self.obj32.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<128>', 20)
    lcobj2.append(cobj2)
    self.obj32.formatArgs.setValue(lcobj2)

    # unpack
    self.obj32.unpack.setValue('')
    self.obj32.unpack.setNone()

    # pack
    self.obj32.pack.setValue('B')

    self.obj32.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(660.0,0.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=Primitive(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # postActions
    self.obj33.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.postActions.setValue(lcobj2)

    # regex
    self.obj33.regex.setValue('')
    self.obj33.regex.setNone()

    # name
    self.obj33.name.setValue('full')

    # parameters
    self.obj33.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.parameters.setValue(lcobj2)

    # format
    self.obj33.format.setValue('')
    self.obj33.format.setNone()

    # formatArgs
    self.obj33.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<132>', 20)
    lcobj2.append(cobj2)
    self.obj33.formatArgs.setValue(lcobj2)

    # unpack
    self.obj33.unpack.setValue('')
    self.obj33.unpack.setNone()

    # pack
    self.obj33.pack.setValue('B')

    self.obj33.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(700.0,80.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=Primitive(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # postActions
    self.obj34.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.postActions.setValue(lcobj2)

    # regex
    self.obj34.regex.setValue('')
    self.obj34.regex.setNone()

    # name
    self.obj34.name.setValue('drive')

    # parameters
    self.obj34.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('velocity', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('radius', 20)
    lcobj2.append(cobj2)
    self.obj34.parameters.setValue(lcobj2)

    # format
    self.obj34.format.setValue('')
    self.obj34.format.setNone()

    # formatArgs
    self.obj34.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<137>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<velocity>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<radius>', 20)
    lcobj2.append(cobj2)
    self.obj34.formatArgs.setValue(lcobj2)

    # unpack
    self.obj34.unpack.setValue('')
    self.obj34.unpack.setNone()

    # pack
    self.obj34.pack.setValue('>Bhh')

    self.obj34.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(740.0,160.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=Primitive(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # postActions
    self.obj35.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('bumperStates = __out__[0]', 20)
    lcobj2.append(cobj2)
    self.obj35.postActions.setValue(lcobj2)

    # regex
    self.obj35.regex.setValue('')
    self.obj35.regex.setNone()

    # name
    self.obj35.name.setValue('bumpers')

    # parameters
    self.obj35.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.parameters.setValue(lcobj2)

    # format
    self.obj35.format.setValue('')
    self.obj35.format.setNone()

    # formatArgs
    self.obj35.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<142>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<7>', 20)
    lcobj2.append(cobj2)
    self.obj35.formatArgs.setValue(lcobj2)

    # unpack
    self.obj35.unpack.setValue('B')

    # pack
    self.obj35.pack.setValue('BB')

    self.obj35.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(780.0,240.0,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=Interface(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # type
    self.obj36.type.setValue( (['adhoc', 'periodic'], 1) )
    self.obj36.type.config = 0

    # name
    self.obj36.name.setValue('get_bumpers')

    # parameters
    self.obj36.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.parameters.setValue(lcobj2)

    self.obj36.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(400.0,120.0,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=Interface(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # type
    self.obj37.type.setValue( (['adhoc', 'periodic'], 0) )
    self.obj37.type.config = 0

    # name
    self.obj37.name.setValue('drive')

    # parameters
    self.obj37.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('velocity', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('radius', 20)
    lcobj2.append(cobj2)
    self.obj37.parameters.setValue(lcobj2)

    self.obj37.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(400.0,200.0,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.94
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=Interface(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # type
    self.obj38.type.setValue( (['adhoc', 'periodic'], 0) )
    self.obj38.type.config = 0

    # name
    self.obj38.name.setValue('startup')

    # parameters
    self.obj38.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.parameters.setValue(lcobj2)

    self.obj38.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(400.0,40.0,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj64=Interface(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # type
    self.obj64.type.setValue( (['adhoc', 'periodic'], 0) )
    self.obj64.type.config = 0

    # name
    self.obj64.name.setValue('shutdown')

    # parameters
    self.obj64.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj64.parameters.setValue(lcobj2)

    self.obj64.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(520.0,340.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj39=StateVariable(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # type
    self.obj39.type.setValue( (['float', 'int', 'string'], 1) )
    self.obj39.type.config = 0

    # name
    self.obj39.name.setValue('bumperStates')

    # value
    self.obj39.value.setValue('')
    self.obj39.value.setNone()

    self.obj39.graphClass_= graph_StateVariable
    if self.genGraphics:
       new_obj = graph_StateVariable(1067.77569755,440,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateVariable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=RangeAdapter(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # distance
    self.obj40.distance.setValue('<int((bumperStates&3)==0)>')

    self.obj40.graphClass_= graph_RangeAdapter
    if self.genGraphics:
       new_obj = graph_RangeAdapter(180.0,220.0,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RangeAdapter", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=DomainInterface(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # name
    self.obj41.name.setValue('set_velocity')

    self.obj41.graphClass_= graph_DomainInterface
    if self.genGraphics:
       new_obj = graph_DomainInterface(16.0,336.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("DomainInterface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=DomainOutput(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # name
    self.obj42.name.setValue('detect_bump')

    self.obj42.graphClass_= graph_DomainOutput
    if self.genGraphics:
       new_obj = graph_DomainOutput(20.0,240.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("DomainOutput", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=interface2primitive(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # priority
    self.obj43.priority.setValue(0)

    # delay
    self.obj43.delay.setValue(100)

    # arguments
    self.obj43.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.arguments.setValue(lcobj2)

    self.obj43.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(591.310188404,144.502065954,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=interface2primitive(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # priority
    self.obj44.priority.setValue(0)

    # delay
    self.obj44.delay.setValue(100)

    # arguments
    self.obj44.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<velocity*1000>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<radius*1000>', 20)
    lcobj2.append(cobj2)
    self.obj44.arguments.setValue(lcobj2)

    self.obj44.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(571.485924838,253.201382825,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=interface2primitive(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # priority
    self.obj45.priority.setValue(0)

    # delay
    self.obj45.delay.setValue(1000)

    # arguments
    self.obj45.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.arguments.setValue(lcobj2)

    self.obj45.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(591.19016093,41.337030101,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=interface2primitive(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # priority
    self.obj46.priority.setValue(1)

    # delay
    self.obj46.delay.setValue(1000)

    # arguments
    self.obj46.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj46.arguments.setValue(lcobj2)

    self.obj46.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(589.328092916,88.576152609,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj69=interface2primitive(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # priority
    self.obj69.priority.setValue(0)

    # delay
    self.obj69.delay.setValue(100)

    # arguments
    self.obj69.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<0>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<0>', 20)
    lcobj2.append(cobj2)
    self.obj69.arguments.setValue(lcobj2)

    self.obj69.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(714.5,361.5,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj47=primitive2connection(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(237.096460468,18.075631185,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=primitive2connection(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(258.892708598,0.165134765,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=primitive2connection(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(366.703185768,-33.80787212,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=primitive2connection(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    self.obj50.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(400.001033647,272.616525021,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=connection2threading(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    self.obj51.graphClass_= graph_connection2threading
    if self.genGraphics:
       new_obj = graph_connection2threading(21.555021841,91.751694816,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connection2threading", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=connectionStartup(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # arguments
    self.obj52.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj52.arguments.setValue(lcobj2)

    self.obj52.graphClass_= graph_connectionStartup
    if self.genGraphics:
       new_obj = graph_connectionStartup(302.299420165,62.564405495,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connectionStartup", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=connectionKeepalive(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # interval
    self.obj53.interval.setValue(1000)

    # arguments
    self.obj53.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj53.arguments.setValue(lcobj2)

    self.obj53.graphClass_= graph_connectionKeepalive
    if self.genGraphics:
       new_obj = graph_connectionKeepalive(308.498736259,128.442955327,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connectionKeepalive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj67=connectionTerminate(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # arguments
    self.obj67.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj67.arguments.setValue(lcobj2)

    self.obj67.graphClass_= graph_connectionTerminate
    if self.genGraphics:
       new_obj = graph_connectionTerminate(225.5,356.5,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connectionTerminate", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj54=domainInterface2Interface(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # arguments
    self.obj54.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<linear>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<linear/angular if angular != 0 else 32.767>', 20)
    lcobj2.append(cobj2)
    self.obj54.arguments.setValue(lcobj2)

    self.obj54.graphClass_= graph_domainInterface2Interface
    if self.genGraphics:
       new_obj = graph_domainInterface2Interface(381.429768763,300.133878262,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("domainInterface2Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=domainAdapter2domainOutput(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    self.obj55.graphClass_= graph_domainAdapter2domainOutput
    if self.genGraphics:
       new_obj = graph_domainAdapter2domainOutput(170.983933209,266.530471179,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("domainAdapter2domainOutput", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=domainAdapter2domainInterface(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    self.obj56.graphClass_= graph_domainAdapter2domainInterface
    if self.genGraphics:
       new_obj = graph_domainAdapter2domainInterface(303.29726385,397.175273071,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("domainAdapter2domainInterface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=interface2domainOutput(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    self.obj57.graphClass_= graph_interface2domainOutput
    if self.genGraphics:
       new_obj = graph_interface2domainOutput(201.522301122,196.959093724,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2domainOutput", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    # Connections for obj29 (graphObject_: Obj0) of type DifferentialSpeedAdapter
    self.drawConnections(
(self.obj29,self.obj56,[383.0, 384.0, 303.64786384953624, 377.1752730712824, 303.29726385, 397.175273071],"true", 3) )
    # Connections for obj30 (graphObject_: Obj1) named btserial
    self.drawConnections(
(self.obj30,self.obj52,[172.0, 160.0, 264.18197793832815, 84.19520549523625, 302.29942016548546, 62.56440549523626],"true", 3),
(self.obj30,self.obj53,[172.0, 160.0, 270.3157969731085, 75.0737553266544, 308.4987362587035, 128.44295532665444],"true", 3),
(self.obj30,self.obj51,[59.0, 109.0, 52.55502184121565, 93.13249481627699, 21.555021840999984, 91.751694816],"true", 3),
(self.obj30,self.obj67,[172.0, 160.0, 225.5, 356.5],"true", 2) )
    # Connections for obj31 (graphObject_: Obj2) of type SingleThreading
    self.drawConnections(
 )
    # Connections for obj32 (graphObject_: Obj3) named start
    self.drawConnections(
(self.obj32,self.obj47,[672.9779626929999, 57.974795161600014, 336.34095114161903, -20.311470024833994, 237.09646046800003, 18.07563118499999],"true", 3) )
    # Connections for obj33 (graphObject_: Obj4) named full
    self.drawConnections(
(self.obj33,self.obj48,[713.1508607770002, 137.873975808, 358.4304237925728, -7.997171283267875, 258.892708598, 0.1651347650000048],"true", 3) )
    # Connections for obj34 (graphObject_: Obj5) named drive
    self.drawConnections(
(self.obj34,self.obj49,[753.004168192, 218.396722586, 459.70422781567993, -11.839491473855105, 366.703185768, -33.80787212000001],"true", 3) )
    # Connections for obj35 (graphObject_: Obj6) named bumpers
    self.drawConnections(
(self.obj35,self.obj50,[793.295140599, 298.0, 499.3248187966378, 324.7357250214549, 400.001033647, 272.616525021],"true", 3) )
    # Connections for obj36 (graphObject_: Obj7) named get_bumpers
    self.drawConnections(
(self.obj36,self.obj43,[509.7317571419999, 141.0, 554.4193425402001, 145.25206595426732, 591.310188404, 144.50206595400005],"true", 3),
(self.obj36,self.obj57,[412.731757142, 143.0, 278.6752404077589, 203.95909372350775, 201.52230112200004, 196.959093724],"true", 3) )
    # Connections for obj37 (graphObject_: Obj8) named drive
    self.drawConnections(
(self.obj37,self.obj44,[510.4592972800001, 221.0, 534.8497071097122, 254.102202179026, 571.485924838, 253.201382825],"true", 3) )
    # Connections for obj38 (graphObject_: Obj9) named startup
    self.drawConnections(
(self.obj38,self.obj45,[510.46976890899987, 61.0, 554.3131124839621, 57.593331310533586, 591.19016093, 41.33703010100001],"true", 3),
(self.obj38,self.obj46,[510.46976890899987, 61.0, 552.1578199486023, 74.60765865651865, 589.328092916, 88.57615260899999],"true", 3) )
    # Connections for obj64 (graphObject_: Obj36) named shutdown
    self.drawConnections(
(self.obj64,self.obj69,[630.0, 361.0, 714.5, 361.5],"true", 2) )
    # Connections for obj39 (graphObject_: Obj10) named bumperStates
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj11) of type RangeAdapter
    self.drawConnections(
(self.obj40,self.obj55,[183.0, 251.73343999999997, 181.2039332089999, 257.96383117852264, 170.98393320899999, 266.530471179],"true", 3) )
    # Connections for obj41 (graphObject_: Obj12) named set_velocity
    self.drawConnections(
(self.obj41,self.obj54,[158.59760000000006, 395.0, 316.96434444291424, 389.13387826170583, 381.42976876299997, 300.13387826200005],"true", 3) )
    # Connections for obj42 (graphObject_: Obj13) named detect_bump
    self.drawConnections(
 )
    # Connections for obj43 (graphObject_: Obj14) of type interface2primitive
    self.drawConnections(
(self.obj43,self.obj35,[591.310188404, 144.50206595400005, 628.2010342685345, 143.75206595426732, 793.295140599, 298.0],"true", 3) )
    # Connections for obj44 (graphObject_: Obj16) of type interface2primitive
    self.drawConnections(
(self.obj44,self.obj34,[571.485924838, 253.201382825, 608.1221425657122, 252.30056347182597, 753.004168192, 218.396722586],"true", 3) )
    # Connections for obj45 (graphObject_: Obj18) of type interface2primitive
    self.drawConnections(
(self.obj45,self.obj32,[591.19016093, 41.33703010100001, 628.0672093759025, 25.080728891333578, 672.9779626929999, 57.974795161600014],"true", 3) )
    # Connections for obj46 (graphObject_: Obj20) of type interface2primitive
    self.drawConnections(
(self.obj46,self.obj33,[589.328092916, 88.57615260899999, 626.4983658825512, 102.54464656051863, 713.1508607770002, 137.873975808],"true", 3) )
    # Connections for obj69 (graphObject_: Obj39) of type interface2primitive
    self.drawConnections(
(self.obj69,self.obj34,[714.5, 361.5, 753.0, 218.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj22) of type primitive2connection
    self.drawConnections(
(self.obj47,self.obj30,[237.09646046800003, 18.07563118499999, 137.85196979536397, 56.462732394365986, 102.0, 109.0],"true", 3) )
    # Connections for obj48 (graphObject_: Obj23) of type primitive2connection
    self.drawConnections(
(self.obj48,self.obj30,[258.892708598, 0.1651347650000048, 159.35499340430943, 8.32744081273205, 102.0, 109.0],"true", 3) )
    # Connections for obj49 (graphObject_: Obj24) of type primitive2connection
    self.drawConnections(
(self.obj49,self.obj30,[366.703185768, -33.80787212000001, 273.70214371967984, -55.77625276665509, 102.0, 109.0],"true", 3) )
    # Connections for obj50 (graphObject_: Obj25) of type primitive2connection
    self.drawConnections(
(self.obj50,self.obj30,[400.0010336468756, 272.6165250214549, 300.6772484971133, 220.49732502145486, 172.0, 160.0],"true", 3) )
    # Connections for obj51 (graphObject_: Obj26) of type connection2threading
    self.drawConnections(
(self.obj51,self.obj31,[21.555021840999984, 91.751694816, -9.444978158784352, 90.370894816277, 30.0, 73.0],"true", 3) )
    # Connections for obj52 (graphObject_: Obj27) of type connectionStartup
    self.drawConnections(
(self.obj52,self.obj38,[302.299420165, 62.56440549499999, 340.41686239264266, 40.933605495236264, 413.469768909, 63.0],"true", 3) )
    # Connections for obj53 (graphObject_: Obj29) of type connectionKeepalive
    self.drawConnections(
(self.obj53,self.obj36,[308.498736259, 128.442955327, 346.6816755442985, 181.81215532665448, 412.731757142, 143.0],"true", 3) )
    # Connections for obj67 (graphObject_: Obj37) of type connectionTerminate
    self.drawConnections(
(self.obj67,self.obj64,[225.5, 356.5, 533.0, 363.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj31) of type domainInterface2Interface
    self.drawConnections(
(self.obj54,self.obj37,[381.42976876299997, 300.13387826200005, 445.89519308291426, 211.1338782617059, 413.45929728, 223.0],"true", 3) )
    # Connections for obj55 (graphObject_: Obj33) of type domainAdapter2domainOutput
    self.drawConnections(
(self.obj55,self.obj42,[170.98393320899999, 266.530471179, 160.76393320899996, 275.09711117852265, 139.12, 295.0],"true", 3) )
    # Connections for obj56 (graphObject_: Obj34) of type domainAdapter2domainInterface
    self.drawConnections(
(self.obj56,self.obj41,[303.29726385, 397.175273071, 302.94666384953626, 417.1752730712824, 159.0, 395.0],"true", 3) )
    # Connections for obj57 (graphObject_: Obj35) of type interface2domainOutput
    self.drawConnections(
(self.obj57,self.obj42,[201.52230112200004, 196.959093724, 124.36936183656883, 189.95909372350775, 139.12, 295.0],"true", 3) )

newfunction = iRobot_Create_MDL

loadedMMName = 'RDIS_META'

atom3version = '0.3'
