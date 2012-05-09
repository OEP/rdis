"""
__Create_Wander_pre_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: pkilgo
Modified: Wed May  9 10:37:36 2012
_______________________________________________________________________________
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
from ROSTwist import *
from ROSType import *
from ROSPublish import *
from ROSTopic import *
from ROSBoolean import *
from ROSNode import *
from ROSSubscribe import *
from graph_connection2threading import *
from graph_SingleThreading import *
from graph_ROSTwist import *
from graph_ROSType import *
from graph_domainInterface2Interface import *
from graph_primitive2connection import *
from graph_Interface import *
from graph_domainAdapter2domainOutput import *
from graph_interface2primitive import *
from graph_ROSBoolean import *
from graph_DomainInterface import *
from graph_Primitive import *
from graph_SerialConnection import *
from graph_connectionStartup import *
from graph_StateVariable import *
from graph_DifferentialSpeedAdapter import *
from graph_connectionTerminate import *
from graph_connectionKeepalive import *
from graph_domainAdapter2domainInterface import *
from graph_ROSNode import *
from graph_interface2domainOutput import *
from graph_ROSTopic import *
from graph_ROSPublish import *
from graph_RangeAdapter import *
from graph_DomainOutput import *
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

def Create_Wander_pre_MDL(self, rootNode, RDISRootNode=None, ROSAppRootNode=None):

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


    self.obj65=DifferentialSpeedAdapter(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # angular
    self.obj65.angular.setValue('')
    self.obj65.angular.setNone()

    # linear
    self.obj65.linear.setValue('')
    self.obj65.linear.setNone()

    self.obj65.graphClass_= graph_DifferentialSpeedAdapter
    if self.genGraphics:
       new_obj = graph_DifferentialSpeedAdapter(380.0,340.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("DifferentialSpeedAdapter", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=SerialConnection(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # baud
    self.obj66.baud.setValue(57600)

    # name
    self.obj66.name.setValue('btserial')

    self.obj66.graphClass_= graph_SerialConnection
    if self.genGraphics:
       new_obj = graph_SerialConnection(0.0,100.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SerialConnection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=SingleThreading(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # freqHz
    self.obj67.freqHz.setValue(40)

    self.obj67.graphClass_= graph_SingleThreading
    if self.genGraphics:
       new_obj = graph_SingleThreading(20.0,20.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("SingleThreading", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=Primitive(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # postActions
    self.obj68.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj68.postActions.setValue(lcobj2)

    # regex
    self.obj68.regex.setValue('')
    self.obj68.regex.setNone()

    # name
    self.obj68.name.setValue('start')

    # parameters
    self.obj68.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj68.parameters.setValue(lcobj2)

    # format
    self.obj68.format.setValue('')
    self.obj68.format.setNone()

    # formatArgs
    self.obj68.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<128>', 20)
    lcobj2.append(cobj2)
    self.obj68.formatArgs.setValue(lcobj2)

    # unpack
    self.obj68.unpack.setValue('')
    self.obj68.unpack.setNone()

    # pack
    self.obj68.pack.setValue('B')

    self.obj68.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(660.0,0.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=Primitive(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # postActions
    self.obj69.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.postActions.setValue(lcobj2)

    # regex
    self.obj69.regex.setValue('')
    self.obj69.regex.setNone()

    # name
    self.obj69.name.setValue('full')

    # parameters
    self.obj69.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.parameters.setValue(lcobj2)

    # format
    self.obj69.format.setValue('')
    self.obj69.format.setNone()

    # formatArgs
    self.obj69.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<132>', 20)
    lcobj2.append(cobj2)
    self.obj69.formatArgs.setValue(lcobj2)

    # unpack
    self.obj69.unpack.setValue('')
    self.obj69.unpack.setNone()

    # pack
    self.obj69.pack.setValue('B')

    self.obj69.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(700.0,80.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=Primitive(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # postActions
    self.obj70.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj70.postActions.setValue(lcobj2)

    # regex
    self.obj70.regex.setValue('')
    self.obj70.regex.setNone()

    # name
    self.obj70.name.setValue('drive')

    # parameters
    self.obj70.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('velocity', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('radius', 20)
    lcobj2.append(cobj2)
    self.obj70.parameters.setValue(lcobj2)

    # format
    self.obj70.format.setValue('')
    self.obj70.format.setNone()

    # formatArgs
    self.obj70.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<137>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<velocity>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<radius>', 20)
    lcobj2.append(cobj2)
    self.obj70.formatArgs.setValue(lcobj2)

    # unpack
    self.obj70.unpack.setValue('')
    self.obj70.unpack.setNone()

    # pack
    self.obj70.pack.setValue('>Bhh')

    self.obj70.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(740.0,160.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=Primitive(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # postActions
    self.obj71.postActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('bumperStates = __out__[0]', 20)
    lcobj2.append(cobj2)
    self.obj71.postActions.setValue(lcobj2)

    # regex
    self.obj71.regex.setValue('')
    self.obj71.regex.setNone()

    # name
    self.obj71.name.setValue('bumpers')

    # parameters
    self.obj71.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj71.parameters.setValue(lcobj2)

    # format
    self.obj71.format.setValue('')
    self.obj71.format.setNone()

    # formatArgs
    self.obj71.formatArgs.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<142>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<7>', 20)
    lcobj2.append(cobj2)
    self.obj71.formatArgs.setValue(lcobj2)

    # unpack
    self.obj71.unpack.setValue('B')

    # pack
    self.obj71.pack.setValue('BB')

    self.obj71.graphClass_= graph_Primitive
    if self.genGraphics:
       new_obj = graph_Primitive(780.0,240.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=Interface(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # type
    self.obj72.type.setValue( (['adhoc', 'periodic'], 1) )
    self.obj72.type.config = 0

    # name
    self.obj72.name.setValue('get_bumpers')

    # parameters
    self.obj72.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj72.parameters.setValue(lcobj2)

    self.obj72.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(400.0,120.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=Interface(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # type
    self.obj73.type.setValue( (['adhoc', 'periodic'], 0) )
    self.obj73.type.config = 0

    # name
    self.obj73.name.setValue('drive')

    # parameters
    self.obj73.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('velocity', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('radius', 20)
    lcobj2.append(cobj2)
    self.obj73.parameters.setValue(lcobj2)

    self.obj73.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(400.0,200.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.94
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=Interface(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # type
    self.obj74.type.setValue( (['adhoc', 'periodic'], 0) )
    self.obj74.type.config = 0

    # name
    self.obj74.name.setValue('startup')

    # parameters
    self.obj74.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj74.parameters.setValue(lcobj2)

    self.obj74.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(400.0,40.0,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=Interface(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # type
    self.obj75.type.setValue( (['adhoc', 'periodic'], 0) )
    self.obj75.type.config = 0

    # name
    self.obj75.name.setValue('shutdown')

    # parameters
    self.obj75.parameters.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj75.parameters.setValue(lcobj2)

    self.obj75.graphClass_= graph_Interface
    if self.genGraphics:
       new_obj = graph_Interface(520.0,340.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=StateVariable(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # type
    self.obj76.type.setValue( (['float', 'int', 'string'], 1) )
    self.obj76.type.config = 0

    # name
    self.obj76.name.setValue('bumperStates')

    # value
    self.obj76.value.setValue('')
    self.obj76.value.setNone()

    self.obj76.graphClass_= graph_StateVariable
    if self.genGraphics:
       new_obj = graph_StateVariable(620.0,440.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("StateVariable", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=RangeAdapter(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # distance
    self.obj77.distance.setValue('<int((bumperStates&3)==0)>')

    self.obj77.graphClass_= graph_RangeAdapter
    if self.genGraphics:
       new_obj = graph_RangeAdapter(180.0,220.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("RangeAdapter", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=DomainInterface(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # name
    self.obj78.name.setValue('set_velocity')

    self.obj78.graphClass_= graph_DomainInterface
    if self.genGraphics:
       new_obj = graph_DomainInterface(16.0,336.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("DomainInterface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=DomainOutput(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # name
    self.obj79.name.setValue('detect_bump')

    self.obj79.graphClass_= graph_DomainOutput
    if self.genGraphics:
       new_obj = graph_DomainOutput(20.0,240.0,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("DomainOutput", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=interface2primitive(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # priority
    self.obj80.priority.setValue(0)

    # delay
    self.obj80.delay.setValue(100)

    # arguments
    self.obj80.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj80.arguments.setValue(lcobj2)

    self.obj80.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(591.310188404,144.502065954,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=interface2primitive(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # priority
    self.obj81.priority.setValue(0)

    # delay
    self.obj81.delay.setValue(100)

    # arguments
    self.obj81.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<velocity*1000>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<radius*1000>', 20)
    lcobj2.append(cobj2)
    self.obj81.arguments.setValue(lcobj2)

    self.obj81.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(571.485924838,253.201382825,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=interface2primitive(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # priority
    self.obj82.priority.setValue(0)

    # delay
    self.obj82.delay.setValue(1000)

    # arguments
    self.obj82.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj82.arguments.setValue(lcobj2)

    self.obj82.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(591.19016093,41.337030101,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=interface2primitive(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # priority
    self.obj83.priority.setValue(1)

    # delay
    self.obj83.delay.setValue(1000)

    # arguments
    self.obj83.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj83.arguments.setValue(lcobj2)

    self.obj83.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(589.328092916,88.576152609,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=interface2primitive(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # priority
    self.obj84.priority.setValue(0)

    # delay
    self.obj84.delay.setValue(100)

    # arguments
    self.obj84.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<0>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<0>', 20)
    lcobj2.append(cobj2)
    self.obj84.arguments.setValue(lcobj2)

    self.obj84.graphClass_= graph_interface2primitive
    if self.genGraphics:
       new_obj = graph_interface2primitive(714.5,361.5,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=primitive2connection(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    self.obj85.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(237.096460468,18.075631185,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=primitive2connection(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    self.obj86.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(258.892708598,0.165134765,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=primitive2connection(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    self.obj87.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(366.703185768,-33.80787212,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=primitive2connection(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    self.obj88.graphClass_= graph_primitive2connection
    if self.genGraphics:
       new_obj = graph_primitive2connection(400.001033647,272.616525021,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=connection2threading(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    self.obj89.graphClass_= graph_connection2threading
    if self.genGraphics:
       new_obj = graph_connection2threading(21.555021841,91.751694816,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connection2threading", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=connectionStartup(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # arguments
    self.obj90.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj90.arguments.setValue(lcobj2)

    self.obj90.graphClass_= graph_connectionStartup
    if self.genGraphics:
       new_obj = graph_connectionStartup(302.299420165,62.564405495,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connectionStartup", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=connectionKeepalive(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # interval
    self.obj91.interval.setValue(1000)

    # arguments
    self.obj91.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj91.arguments.setValue(lcobj2)

    self.obj91.graphClass_= graph_connectionKeepalive
    if self.genGraphics:
       new_obj = graph_connectionKeepalive(308.498736259,128.442955327,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connectionKeepalive", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=connectionTerminate(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(False)

    # arguments
    self.obj92.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj92.arguments.setValue(lcobj2)

    self.obj92.graphClass_= graph_connectionTerminate
    if self.genGraphics:
       new_obj = graph_connectionTerminate(225.5,356.5,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("connectionTerminate", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=domainInterface2Interface(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(False)

    # arguments
    self.obj93.arguments.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('<linear>', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('<linear/angular if angular != 0 else 32.767>', 20)
    lcobj2.append(cobj2)
    self.obj93.arguments.setValue(lcobj2)

    self.obj93.graphClass_= graph_domainInterface2Interface
    if self.genGraphics:
       new_obj = graph_domainInterface2Interface(381.429768763,300.133878262,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("domainInterface2Interface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=domainAdapter2domainOutput(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    self.obj94.graphClass_= graph_domainAdapter2domainOutput
    if self.genGraphics:
       new_obj = graph_domainAdapter2domainOutput(170.983933209,266.530471179,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("domainAdapter2domainOutput", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=domainAdapter2domainInterface(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    self.obj95.graphClass_= graph_domainAdapter2domainInterface
    if self.genGraphics:
       new_obj = graph_domainAdapter2domainInterface(303.29726385,397.175273071,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("domainAdapter2domainInterface", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=interface2domainOutput(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    self.obj96.graphClass_= graph_interface2domainOutput
    if self.genGraphics:
       new_obj = graph_interface2domainOutput(201.522301122,196.959093724,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("interface2domainOutput", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj105=ROSTwist(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # angular
    self.obj105.angular.setActionFlags([ 0, 0, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3String('x', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('y', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('z', 20)
    lcobj2.append(cobj2)
    self.obj105.angular.setValue(lcobj2)

    # linear
    self.obj105.linear.setActionFlags([ 0, 0, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3String('x', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('y', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('z', 20)
    lcobj2.append(cobj2)
    self.obj105.linear.setValue(lcobj2)

    self.obj105.graphClass_= graph_ROSTwist
    if self.genGraphics:
       new_obj = graph_ROSTwist(200.0,660.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSTwist", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=ROSType(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    self.obj106.graphClass_= graph_ROSType
    if self.genGraphics:
       new_obj = graph_ROSType(229.5,620.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=ROSType(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    self.obj107.graphClass_= graph_ROSType
    if self.genGraphics:
       new_obj = graph_ROSType(615.5,695.5,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSType", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=ROSPublish(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    self.obj108.graphClass_= graph_ROSPublish
    if self.genGraphics:
       new_obj = graph_ROSPublish(492.0,552.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSPublish", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=ROSTopic(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # name
    self.obj109.name.setValue('setSpeed')

    self.obj109.graphClass_= graph_ROSTopic
    if self.genGraphics:
       new_obj = graph_ROSTopic(140.0,480.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSTopic", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=ROSTopic(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # name
    self.obj110.name.setValue('hitObject')

    self.obj110.graphClass_= graph_ROSTopic
    if self.genGraphics:
       new_obj = graph_ROSTopic(440.0,600.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSTopic", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=ROSBoolean(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # data
    self.obj111.data.setValue('')
    self.obj111.data.setNone()

    self.obj111.graphClass_= graph_ROSBoolean
    if self.genGraphics:
       new_obj = graph_ROSBoolean(680.0,720.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSBoolean", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=ROSNode(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # name
    self.obj112.name.setValue('rdisWanderer')

    self.obj112.graphClass_= graph_ROSNode
    if self.genGraphics:
       new_obj = graph_ROSNode(320.0,460.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSNode", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=ROSSubscribe(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    self.obj113.graphClass_= graph_ROSSubscribe
    if self.genGraphics:
       new_obj = graph_ROSSubscribe(290.5,469.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ROSSubscribe", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    # Connections for obj65 (graphObject_: Obj41) of type DifferentialSpeedAdapter
    self.drawConnections(
(self.obj65,self.obj95,[383.0, 384.0, 303.64786384953624, 377.1752730712824, 303.29726385, 397.175273071],"true", 3) )
    # Connections for obj66 (graphObject_: Obj42) named btserial
    self.drawConnections(
(self.obj66,self.obj90,[172.0, 160.0, 264.18197793832815, 84.19520549523625, 302.29942016548546, 62.56440549523626],"true", 3),
(self.obj66,self.obj91,[172.0, 160.0, 270.3157969731085, 75.0737553266544, 308.4987362587035, 128.44295532665444],"true", 3),
(self.obj66,self.obj89,[59.0, 109.0, 52.55502184121565, 93.13249481627699, 21.555021840999984, 91.751694816],"true", 3),
(self.obj66,self.obj92,[172.0, 160.0, 225.5, 356.5],"true", 2) )
    # Connections for obj67 (graphObject_: Obj43) of type SingleThreading
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj44) named start
    self.drawConnections(
(self.obj68,self.obj85,[672.9779626929999, 57.974795161600014, 336.34095114161903, -20.311470024833994, 237.09646046800003, 18.07563118499999],"true", 3) )
    # Connections for obj69 (graphObject_: Obj45) named full
    self.drawConnections(
(self.obj69,self.obj86,[713.1508607770002, 137.873975808, 358.4304237925728, -7.997171283267875, 258.892708598, 0.1651347650000048],"true", 3) )
    # Connections for obj70 (graphObject_: Obj46) named drive
    self.drawConnections(
(self.obj70,self.obj87,[753.004168192, 218.396722586, 459.70422781567993, -11.839491473855105, 366.703185768, -33.80787212000001],"true", 3) )
    # Connections for obj71 (graphObject_: Obj47) named bumpers
    self.drawConnections(
(self.obj71,self.obj88,[793.295140599, 298.0, 499.3248187966378, 324.7357250214549, 400.001033647, 272.616525021],"true", 3) )
    # Connections for obj72 (graphObject_: Obj48) named get_bumpers
    self.drawConnections(
(self.obj72,self.obj80,[510.0, 141.0, 554.4193425402001, 145.25206595426732, 591.310188404, 144.502065954],"true", 3),
(self.obj72,self.obj96,[413.0, 143.0, 278.6752404077589, 203.95909372350775, 201.522301122, 196.959093724],"true", 3) )
    # Connections for obj73 (graphObject_: Obj49) named drive
    self.drawConnections(
(self.obj73,self.obj81,[510.4592972800001, 221.0, 534.8497071097122, 254.102202179026, 571.485924838, 253.201382825],"true", 3) )
    # Connections for obj74 (graphObject_: Obj50) named startup
    self.drawConnections(
(self.obj74,self.obj82,[510.46976890899987, 61.0, 554.3131124839621, 57.593331310533586, 591.19016093, 41.33703010100001],"true", 3),
(self.obj74,self.obj83,[510.46976890899987, 61.0, 552.1578199486023, 74.60765865651865, 589.328092916, 88.57615260899999],"true", 3) )
    # Connections for obj75 (graphObject_: Obj51) named shutdown
    self.drawConnections(
(self.obj75,self.obj84,[630.0, 361.0, 714.5, 361.5],"true", 2) )
    # Connections for obj76 (graphObject_: Obj52) named bumperStates
    self.drawConnections(
 )
    # Connections for obj77 (graphObject_: Obj53) of type RangeAdapter
    self.drawConnections(
(self.obj77,self.obj94,[183.0, 251.73343999999997, 181.2039332089999, 257.96383117852264, 170.98393320899999, 266.530471179],"true", 3) )
    # Connections for obj78 (graphObject_: Obj54) named set_velocity
    self.drawConnections(
(self.obj78,self.obj93,[158.59760000000006, 395.0, 316.96434444291424, 389.13387826170583, 381.42976876299997, 300.13387826200005],"true", 3) )
    # Connections for obj79 (graphObject_: Obj55) named detect_bump
    self.drawConnections(
 )
    # Connections for obj80 (graphObject_: Obj56) of type interface2primitive
    self.drawConnections(
(self.obj80,self.obj71,[591.310188404, 144.502065954, 628.2010342685345, 143.75206595426732, 793.0, 298.0],"true", 3) )
    # Connections for obj81 (graphObject_: Obj58) of type interface2primitive
    self.drawConnections(
(self.obj81,self.obj70,[571.485924838, 253.201382825, 608.1221425657122, 252.30056347182597, 753.004168192, 218.396722586],"true", 3) )
    # Connections for obj82 (graphObject_: Obj60) of type interface2primitive
    self.drawConnections(
(self.obj82,self.obj68,[591.19016093, 41.33703010100001, 628.0672093759025, 25.080728891333578, 672.9779626929999, 57.974795161600014],"true", 3) )
    # Connections for obj83 (graphObject_: Obj62) of type interface2primitive
    self.drawConnections(
(self.obj83,self.obj69,[589.328092916, 88.57615260899999, 626.4983658825512, 102.54464656051863, 713.1508607770002, 137.873975808],"true", 3) )
    # Connections for obj84 (graphObject_: Obj64) of type interface2primitive
    self.drawConnections(
(self.obj84,self.obj70,[714.5, 361.5, 753.0, 218.0],"true", 2) )
    # Connections for obj85 (graphObject_: Obj66) of type primitive2connection
    self.drawConnections(
(self.obj85,self.obj66,[237.09646046800003, 18.07563118499999, 137.85196979536397, 56.462732394365986, 102.0, 109.0],"true", 3) )
    # Connections for obj86 (graphObject_: Obj67) of type primitive2connection
    self.drawConnections(
(self.obj86,self.obj66,[258.892708598, 0.1651347650000048, 159.35499340430943, 8.32744081273205, 102.0, 109.0],"true", 3) )
    # Connections for obj87 (graphObject_: Obj68) of type primitive2connection
    self.drawConnections(
(self.obj87,self.obj66,[366.703185768, -33.80787212000001, 273.70214371967984, -55.77625276665509, 102.0, 109.0],"true", 3) )
    # Connections for obj88 (graphObject_: Obj69) of type primitive2connection
    self.drawConnections(
(self.obj88,self.obj66,[400.0010336468756, 272.6165250214549, 300.6772484971133, 220.49732502145486, 172.0, 160.0],"true", 3) )
    # Connections for obj89 (graphObject_: Obj70) of type connection2threading
    self.drawConnections(
(self.obj89,self.obj67,[21.555021840999984, 91.751694816, -9.444978158784352, 90.370894816277, 30.0, 73.0],"true", 3) )
    # Connections for obj90 (graphObject_: Obj71) of type connectionStartup
    self.drawConnections(
(self.obj90,self.obj74,[302.299420165, 62.56440549499999, 340.41686239264266, 40.933605495236264, 413.469768909, 63.0],"true", 3) )
    # Connections for obj91 (graphObject_: Obj73) of type connectionKeepalive
    self.drawConnections(
(self.obj91,self.obj72,[308.498736259, 128.442955327, 346.6816755442985, 181.81215532665448, 413.0, 143.0],"true", 3) )
    # Connections for obj92 (graphObject_: Obj75) of type connectionTerminate
    self.drawConnections(
(self.obj92,self.obj75,[225.5, 356.5, 533.0, 363.0],"true", 2) )
    # Connections for obj93 (graphObject_: Obj77) of type domainInterface2Interface
    self.drawConnections(
(self.obj93,self.obj73,[381.42976876299997, 300.13387826200005, 445.89519308291426, 211.1338782617059, 413.45929728, 223.0],"true", 3) )
    # Connections for obj94 (graphObject_: Obj79) of type domainAdapter2domainOutput
    self.drawConnections(
(self.obj94,self.obj79,[170.98393320899999, 266.530471179, 160.76393320899996, 275.09711117852265, 139.12, 295.0],"true", 3) )
    # Connections for obj95 (graphObject_: Obj80) of type domainAdapter2domainInterface
    self.drawConnections(
(self.obj95,self.obj78,[303.29726385, 397.175273071, 302.94666384953626, 417.1752730712824, 159.0, 395.0],"true", 3) )
    # Connections for obj96 (graphObject_: Obj81) of type interface2domainOutput
    self.drawConnections(
(self.obj96,self.obj79,[201.522301122, 196.959093724, 124.36936183656883, 189.95909372350775, 139.0, 295.0],"true", 3) )
    # Connections for obj105 (graphObject_: Obj82) of type ROSTwist
    self.drawConnections(
 )
    # Connections for obj106 (graphObject_: Obj83) of type ROSType
    self.drawConnections(
(self.obj106,self.obj105,[229.5, 620.0, 252.0, 665.0],"true", 2) )
    # Connections for obj107 (graphObject_: Obj84) of type ROSType
    self.drawConnections(
(self.obj107,self.obj111,[615.5, 695.5, 698.0, 722.0],"true", 2) )
    # Connections for obj108 (graphObject_: Obj85) of type ROSPublish
    self.drawConnections(
(self.obj108,self.obj110,[492.0, 552.0, 523.0, 604.0],"true", 2) )
    # Connections for obj109 (graphObject_: Obj86) named setSpeed
    self.drawConnections(
(self.obj109,self.obj106,[217.0, 567.0, 229.5, 620.0],"true", 2),
(self.obj109,self.obj113,[275.0, 511.0, 290.5, 469.0],"true", 2) )
    # Connections for obj110 (graphObject_: Obj87) named hitObject
    self.drawConnections(
(self.obj110,self.obj107,[568.0, 667.0, 615.5, 695.5],"true", 2) )
    # Connections for obj111 (graphObject_: Obj88) of type ROSBoolean
    self.drawConnections(
 )
    # Connections for obj112 (graphObject_: Obj89) named rdisWanderer
    self.drawConnections(
(self.obj112,self.obj108,[464.0, 515.0, 492.0, 552.0],"true", 2) )
    # Connections for obj113 (graphObject_: Obj90) of type ROSSubscribe
    self.drawConnections(
(self.obj113,self.obj112,[290.5, 469.0, 322.0, 506.0],"true", 2) )

newfunction = Create_Wander_pre_MDL

loadedMMName = ['RDIS_META', 'ROSApp_META']

atom3version = '0.3'
