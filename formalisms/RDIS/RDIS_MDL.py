"""
__RDIS_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: pkilgo
Modified: Sun Apr 15 12:08:12 2012
__________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from CD_Class3 import *
from CD_Association3 import *
from CD_Inheritance3 import *
from graph_CD_Association3 import *
from graph_CD_Class3 import *
from graph_CD_Inheritance3 import *
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

def RDIS_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('RDIS')

        # author
        CD_ClassDiagramsV3RootNode.author.setValue('PaulKilgo')

        # showCardinalities
        CD_ClassDiagramsV3RootNode.showCardinalities.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showCardinalities.config = 0

        # showAssociationBox
        CD_ClassDiagramsV3RootNode.showAssociationBox.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAssociationBox.config = 0

        # description
        CD_ClassDiagramsV3RootNode.description.setValue('\n')
        CD_ClassDiagramsV3RootNode.description.setHeight(15)

        # showAttributes
        CD_ClassDiagramsV3RootNode.showAttributes.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAttributes.config = 0

        # showActions
        CD_ClassDiagramsV3RootNode.showActions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showActions.config = 0

        # showConditions
        CD_ClassDiagramsV3RootNode.showConditions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showConditions.config = 0

        # attributes
        CD_ClassDiagramsV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        CD_ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        CD_ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj119=CD_Class3(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # QOCA
    self.obj119.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj119.Graphical_Appearance.setValue( ('DifferentialSpeedAdapter', self.obj119))

    # name
    self.obj119.name.setValue('DifferentialSpeedAdapter')

    # attributes
    self.obj119.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('angular', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('linear', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj119.attributes.setValue(lcobj2)

    # Abstract
    self.obj119.Abstract.setValue((None, 0))
    self.obj119.Abstract.config = 0

    # cardinality
    self.obj119.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj119.cardinality.setValue(lcobj2)

    # display
    self.obj119.display.setValue('Attributes:\n  - angular :: String\n  - linear :: String\n')
    self.obj119.display.setHeight(15)

    # Actions
    self.obj119.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.Actions.setValue(lcobj2)

    # Constraints
    self.obj119.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.Constraints.setValue(lcobj2)

    self.obj119.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(240.0,500.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=CD_Class3(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # QOCA
    self.obj120.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj120.Graphical_Appearance.setValue( ('DomainAdapter', self.obj120))

    # name
    self.obj120.name.setValue('DomainAdapter')

    # attributes
    self.obj120.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.attributes.setValue(lcobj2)

    # Abstract
    self.obj120.Abstract.setValue((None, 1))
    self.obj120.Abstract.config = 0

    # cardinality
    self.obj120.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('domainAdapter2domainOutput', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('domainAdapter2domainInterface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    self.obj120.cardinality.setValue(lcobj2)

    # display
    self.obj120.display.setValue('Multiplicities:\n  - To domainAdapter2domainOutput: 0 to N\n  - To domainAdapter2domainInterface: 0 to 1\n')
    self.obj120.display.setHeight(15)

    # Actions
    self.obj120.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.Actions.setValue(lcobj2)

    # Constraints
    self.obj120.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.Constraints.setValue(lcobj2)

    self.obj120.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(60.0,240.0,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7445312499999999, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=CD_Class3(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # QOCA
    self.obj121.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj121.Graphical_Appearance.setValue( ('Connection', self.obj121))

    # name
    self.obj121.name.setValue('Connection')

    # attributes
    self.obj121.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj121.attributes.setValue(lcobj2)

    # Abstract
    self.obj121.Abstract.setValue((None, 1))
    self.obj121.Abstract.config = 0

    # cardinality
    self.obj121.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('primitive2connection', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connection2threading', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connectionStartup', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connectionKeepalive', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connectionTerminate', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    self.obj121.cardinality.setValue(lcobj2)

    # display
    self.obj121.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From primitive2connection: 0 to N\n  - To connection2threading: 0 to 1\n  - To connectionStartup: 0 to 1\n  - To connectionKeepalive: 0 to 1\n  - To connectionTerminate: 0 to 1\n')
    self.obj121.display.setHeight(15)

    # Actions
    self.obj121.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.Actions.setValue(lcobj2)

    # Constraints
    self.obj121.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.Constraints.setValue(lcobj2)

    self.obj121.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(580.0,300.0,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.39453125, 1.4459016393442623]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=CD_Class3(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(False)

    # QOCA
    self.obj122.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj122.Graphical_Appearance.setValue( ('SerialConnection', self.obj122))

    # name
    self.obj122.name.setValue('SerialConnection')

    # attributes
    self.obj122.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('baud', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj122.attributes.setValue(lcobj2)

    # Abstract
    self.obj122.Abstract.setValue((None, 0))
    self.obj122.Abstract.config = 0

    # cardinality
    self.obj122.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj122.cardinality.setValue(lcobj2)

    # display
    self.obj122.display.setValue('Attributes:\n  - baud :: Integer\n')
    self.obj122.display.setHeight(15)

    # Actions
    self.obj122.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.Actions.setValue(lcobj2)

    # Constraints
    self.obj122.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.Constraints.setValue(lcobj2)

    self.obj122.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,640.0,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=CD_Class3(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # QOCA
    self.obj123.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj123.Graphical_Appearance.setValue( ('Threading', self.obj123))

    # name
    self.obj123.name.setValue('Threading')

    # attributes
    self.obj123.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.attributes.setValue(lcobj2)

    # Abstract
    self.obj123.Abstract.setValue((None, 1))
    self.obj123.Abstract.config = 0

    # cardinality
    self.obj123.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('connection2threading', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj123.cardinality.setValue(lcobj2)

    # display
    self.obj123.display.setValue('Multiplicities:\n  - From connection2threading: 0 to 1\n')
    self.obj123.display.setHeight(15)

    # Actions
    self.obj123.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Actions.setValue(lcobj2)

    # Constraints
    self.obj123.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Constraints.setValue(lcobj2)

    self.obj123.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1140.0,620.0,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.4164062499999999, 1.0]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=CD_Class3(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # QOCA
    self.obj124.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj124.Graphical_Appearance.setValue( ('SingleThreading', self.obj124))

    # name
    self.obj124.name.setValue('SingleThreading')

    # attributes
    self.obj124.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('freqHz', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj124.attributes.setValue(lcobj2)

    # Abstract
    self.obj124.Abstract.setValue((None, 0))
    self.obj124.Abstract.config = 0

    # cardinality
    self.obj124.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj124.cardinality.setValue(lcobj2)

    # display
    self.obj124.display.setValue('Attributes:\n  - freqHz :: Integer\n')
    self.obj124.display.setHeight(15)

    # Actions
    self.obj124.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Actions.setValue(lcobj2)

    # Constraints
    self.obj124.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Constraints.setValue(lcobj2)

    self.obj124.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(900.0,720.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=CD_Class3(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # QOCA
    self.obj125.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj125.Graphical_Appearance.setValue( ('Primitive', self.obj125))

    # name
    self.obj125.name.setValue('Primitive')

    # attributes
    self.obj125.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('format', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('formatArgs', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('pack', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('parameters', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('postActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('regex', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('unpack', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj125.attributes.setValue(lcobj2)

    # Abstract
    self.obj125.Abstract.setValue((None, 0))
    self.obj125.Abstract.config = 0

    # cardinality
    self.obj125.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('interface2primitive', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('primitive2connection', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    self.obj125.cardinality.setValue(lcobj2)

    # display
    self.obj125.display.setValue('Attributes:\n  - format :: String\n  - formatArgs :: List\n  - name :: String\n  - pack :: String\n  - parameters :: List\n  - postActions :: List\n  - regex :: String\n  - unpack :: String\nMultiplicities:\n  - From interface2primitive: 0 to N\n  - To primitive2connection: 0 to 1\n')
    self.obj125.display.setHeight(15)

    # Actions
    self.obj125.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj125.Actions.setValue(lcobj2)

    # Constraints
    self.obj125.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj125.Constraints.setValue(lcobj2)

    self.obj125.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(860.0,140.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.3015625, 2.1688524590163936]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=CD_Class3(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # QOCA
    self.obj126.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj126.Graphical_Appearance.setValue( ('Interface', self.obj126))

    # name
    self.obj126.name.setValue('Interface')

    # attributes
    self.obj126.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('parameters', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['adhoc', 'periodic'],0,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('adhoc', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('periodic', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj126.attributes.setValue(lcobj2)

    # Abstract
    self.obj126.Abstract.setValue((None, 0))
    self.obj126.Abstract.config = 0

    # cardinality
    self.obj126.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('interface2primitive', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connectionStartup', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connectionKeepalive', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('connectionTerminate', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('domainInterface2Interface', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('interface2domainOutput', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj126.cardinality.setValue(lcobj2)

    # display
    self.obj126.display.setValue('Attributes:\n  - name :: String\n  - parameters :: List\n  - type :: Enum\nMultiplicities:\n  - To interface2primitive: 0 to N\n  - From connectionStartup: 0 to N\n  - From connectionKeepalive: 0 to N\n  - From connectionTerminate: 0 to N\n  - From domainInterface2Interface: 0 to N\n  - To interface2domainOutput: 0 to N\n')
    self.obj126.display.setHeight(15)

    # Actions
    self.obj126.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj126.Actions.setValue(lcobj2)

    # Constraints
    self.obj126.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj126.Constraints.setValue(lcobj2)

    self.obj126.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1120.0,0.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.596875, 1.9881147540983608]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=CD_Class3(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(False)

    # QOCA
    self.obj127.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj127.Graphical_Appearance.setValue( ('StateVariable', self.obj127))

    # name
    self.obj127.name.setValue('StateVariable')

    # attributes
    self.obj127.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Enum(['float', 'int', 'string'],0,1)
    cobj2.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj3 =[]
    cobj3=ATOM3String('float', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('int', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('string', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.configItems.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('value', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj127.attributes.setValue(lcobj2)

    # Abstract
    self.obj127.Abstract.setValue((None, 0))
    self.obj127.Abstract.config = 0

    # cardinality
    self.obj127.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj127.cardinality.setValue(lcobj2)

    # display
    self.obj127.display.setValue('Attributes:\n  - name :: String\n  - type :: Enum\n  - value :: String\n')
    self.obj127.display.setHeight(15)

    # Actions
    self.obj127.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj127.Actions.setValue(lcobj2)

    # Constraints
    self.obj127.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj127.Constraints.setValue(lcobj2)

    self.obj127.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,0.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=CD_Class3(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(False)

    # QOCA
    self.obj128.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj128.Graphical_Appearance.setValue( ('RangeAdapter', self.obj128))

    # name
    self.obj128.name.setValue('RangeAdapter')

    # attributes
    self.obj128.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('distance', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj128.attributes.setValue(lcobj2)

    # Abstract
    self.obj128.Abstract.setValue((None, 0))
    self.obj128.Abstract.config = 0

    # cardinality
    self.obj128.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj128.cardinality.setValue(lcobj2)

    # display
    self.obj128.display.setValue('Attributes:\n  - distance :: String\n')
    self.obj128.display.setHeight(15)

    # Actions
    self.obj128.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj128.Actions.setValue(lcobj2)

    # Constraints
    self.obj128.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj128.Constraints.setValue(lcobj2)

    self.obj128.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,500.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=CD_Class3(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    # QOCA
    self.obj129.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj129.Graphical_Appearance.setValue( ('DomainInterface', self.obj129))

    # name
    self.obj129.name.setValue('DomainInterface')

    # attributes
    self.obj129.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj129.attributes.setValue(lcobj2)

    # Abstract
    self.obj129.Abstract.setValue((None, 0))
    self.obj129.Abstract.config = 0

    # cardinality
    self.obj129.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('domainInterface2Interface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('domainAdapter2domainInterface', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj129.cardinality.setValue(lcobj2)

    # display
    self.obj129.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - To domainInterface2Interface: 0 to 1\n  - From domainAdapter2domainInterface: 0 to 1\n')
    self.obj129.display.setHeight(15)

    # Actions
    self.obj129.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj129.Actions.setValue(lcobj2)

    # Constraints
    self.obj129.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj129.Constraints.setValue(lcobj2)

    self.obj129.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(200.0,0.0,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.84296875, 1.0]
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=CD_Class3(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    # QOCA
    self.obj130.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj130.Graphical_Appearance.setValue( ('DomainOutput', self.obj130))

    # name
    self.obj130.name.setValue('DomainOutput')

    # attributes
    self.obj130.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj130.attributes.setValue(lcobj2)

    # Abstract
    self.obj130.Abstract.setValue((None, 0))
    self.obj130.Abstract.config = 0

    # cardinality
    self.obj130.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('domainAdapter2domainOutput', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('interface2domainOutput', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj130.cardinality.setValue(lcobj2)

    # display
    self.obj130.display.setValue('Attributes:\n  - name :: String\nMultiplicities:\n  - From domainAdapter2domainOutput: 0 to N\n  - From interface2domainOutput: 0 to N\n')
    self.obj130.display.setHeight(15)

    # Actions
    self.obj130.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj130.Actions.setValue(lcobj2)

    # Constraints
    self.obj130.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj130.Constraints.setValue(lcobj2)

    self.obj130.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(360.0,140.0,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7828125000000001, 1.0]
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=CD_Association3(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    # QOCA
    self.obj131.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj131.Graphical_Appearance.setValue( ('interface2primitive', self.obj131))
    self.obj131.Graphical_Appearance.linkInfo=linkEditor(self,self.obj131.Graphical_Appearance.semObject, "interface2primitive")
    self.obj131.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('interface2primitive_1stLink', self.obj131.Graphical_Appearance.linkInfo.FirstLink))
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('interface2primitive_1stSegment', self.obj131.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj131.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj131.Graphical_Appearance.linkInfo.Center.setValue( ('interface2primitive_Center', self.obj131.Graphical_Appearance.linkInfo))
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('interface2primitive_2ndSegment', self.obj131.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj131.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('interface2primitive_2ndLink', self.obj131.Graphical_Appearance.linkInfo.SecondLink))
    self.obj131.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj131.Graphical_Appearance.semObject
    self.obj131.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj131.Graphical_Appearance.semObject
    self.obj131.Graphical_Appearance.linkInfo.Center.semObject=self.obj131.Graphical_Appearance.semObject
    self.obj131.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj131.Graphical_Appearance.semObject
    self.obj131.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj131.Graphical_Appearance.semObject

    # name
    self.obj131.name.setValue('interface2primitive')

    # displaySelect
    self.obj131.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj131.displaySelect.config = 0

    # attributes
    self.obj131.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arguments', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('priority', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('delay', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj131.attributes.setValue(lcobj2)

    # cardinality
    self.obj131.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Primitive', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Interface', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj131.cardinality.setValue(lcobj2)

    # display
    self.obj131.display.setValue('Attributes:\n  - arguments :: List\n  - priority :: Integer\n  - delay :: Integer\nMultiplicities:\n  - To Primitive: 0 to 1\n  - From Interface: 0 to 1\n')
    self.obj131.display.setHeight(15)

    # Actions
    self.obj131.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj131.Actions.setValue(lcobj2)

    # Constraints
    self.obj131.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj131.Constraints.setValue(lcobj2)

    self.obj131.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1219.25,335.0,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1620000000000001, 1.6596774193548387]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=CD_Association3(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    # QOCA
    self.obj132.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj132.Graphical_Appearance.setValue( ('primitive2connection', self.obj132))
    self.obj132.Graphical_Appearance.linkInfo=linkEditor(self,self.obj132.Graphical_Appearance.semObject, "primitive2connection")
    self.obj132.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('primitive2connection_1stLink', self.obj132.Graphical_Appearance.linkInfo.FirstLink))
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('primitive2connection_1stSegment', self.obj132.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj132.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj132.Graphical_Appearance.linkInfo.Center.setValue( ('primitive2connection_Center', self.obj132.Graphical_Appearance.linkInfo))
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('primitive2connection_2ndSegment', self.obj132.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj132.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('primitive2connection_2ndLink', self.obj132.Graphical_Appearance.linkInfo.SecondLink))
    self.obj132.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj132.Graphical_Appearance.semObject
    self.obj132.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj132.Graphical_Appearance.semObject
    self.obj132.Graphical_Appearance.linkInfo.Center.semObject=self.obj132.Graphical_Appearance.semObject
    self.obj132.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj132.Graphical_Appearance.semObject
    self.obj132.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj132.Graphical_Appearance.semObject

    # name
    self.obj132.name.setValue('primitive2connection')

    # displaySelect
    self.obj132.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj132.displaySelect.config = 0

    # attributes
    self.obj132.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj132.attributes.setValue(lcobj2)

    # cardinality
    self.obj132.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Connection', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Primitive', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj132.cardinality.setValue(lcobj2)

    # display
    self.obj132.display.setValue('Multiplicities:\n  - To Connection: 0 to 1\n  - From Primitive: 0 to 1\n')
    self.obj132.display.setHeight(15)

    # Actions
    self.obj132.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj132.Actions.setValue(lcobj2)

    # Constraints
    self.obj132.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj132.Constraints.setValue(lcobj2)

    self.obj132.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(643.212890625,93.834016393,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.183, 1.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj133=CD_Association3(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # QOCA
    self.obj133.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj133.Graphical_Appearance.setValue( ('connection2threading', self.obj133))
    self.obj133.Graphical_Appearance.linkInfo=linkEditor(self,self.obj133.Graphical_Appearance.semObject, "connection2threading")
    self.obj133.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('connection2threading_1stLink', self.obj133.Graphical_Appearance.linkInfo.FirstLink))
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('connection2threading_1stSegment', self.obj133.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj133.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj133.Graphical_Appearance.linkInfo.Center.setValue( ('connection2threading_Center', self.obj133.Graphical_Appearance.linkInfo))
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('connection2threading_2ndSegment', self.obj133.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj133.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('connection2threading_2ndLink', self.obj133.Graphical_Appearance.linkInfo.SecondLink))
    self.obj133.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj133.Graphical_Appearance.semObject
    self.obj133.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj133.Graphical_Appearance.semObject
    self.obj133.Graphical_Appearance.linkInfo.Center.semObject=self.obj133.Graphical_Appearance.semObject
    self.obj133.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj133.Graphical_Appearance.semObject
    self.obj133.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj133.Graphical_Appearance.semObject

    # name
    self.obj133.name.setValue('connection2threading')

    # displaySelect
    self.obj133.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj133.displaySelect.config = 0

    # attributes
    self.obj133.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj133.attributes.setValue(lcobj2)

    # cardinality
    self.obj133.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Threading', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Connection', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj133.cardinality.setValue(lcobj2)

    # display
    self.obj133.display.setValue('Multiplicities:\n  - To Threading: 0 to 1\n  - From Connection: 0 to 1\n')
    self.obj133.display.setHeight(15)

    # Actions
    self.obj133.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj133.Actions.setValue(lcobj2)

    # Constraints
    self.obj133.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj133.Constraints.setValue(lcobj2)

    self.obj133.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(915.076171875,546.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.309, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=CD_Association3(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # QOCA
    self.obj134.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj134.Graphical_Appearance.setValue( ('connectionStartup', self.obj134))
    self.obj134.Graphical_Appearance.linkInfo=linkEditor(self,self.obj134.Graphical_Appearance.semObject, "connectionStartup")
    self.obj134.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('connectionStartup_1stLink', self.obj134.Graphical_Appearance.linkInfo.FirstLink))
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('connectionStartup_1stSegment', self.obj134.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj134.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj134.Graphical_Appearance.linkInfo.Center.setValue( ('connectionStartup_Center', self.obj134.Graphical_Appearance.linkInfo))
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('connectionStartup_2ndSegment', self.obj134.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj134.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('connectionStartup_2ndLink', self.obj134.Graphical_Appearance.linkInfo.SecondLink))
    self.obj134.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj134.Graphical_Appearance.semObject
    self.obj134.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj134.Graphical_Appearance.semObject
    self.obj134.Graphical_Appearance.linkInfo.Center.semObject=self.obj134.Graphical_Appearance.semObject
    self.obj134.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj134.Graphical_Appearance.semObject
    self.obj134.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj134.Graphical_Appearance.semObject

    # name
    self.obj134.name.setValue('connectionStartup')

    # displaySelect
    self.obj134.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj134.displaySelect.config = 0

    # attributes
    self.obj134.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arguments', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj134.attributes.setValue(lcobj2)

    # cardinality
    self.obj134.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Interface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Connection', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj134.cardinality.setValue(lcobj2)

    # display
    self.obj134.display.setValue('Attributes:\n  - arguments :: List\nMultiplicities:\n  - To Interface: 0 to 1\n  - From Connection: 0 to 1\n')
    self.obj134.display.setHeight(15)

    # Actions
    self.obj134.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj134.Actions.setValue(lcobj2)

    # Constraints
    self.obj134.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj134.Constraints.setValue(lcobj2)

    self.obj134.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1392.02148438,513.778688525,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.309, 1.185483870967742]
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj135=CD_Association3(self)
    self.obj135.isGraphObjectVisual = True

    if(hasattr(self.obj135, '_setHierarchicalLink')):
      self.obj135._setHierarchicalLink(False)

    # QOCA
    self.obj135.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj135.Graphical_Appearance.setValue( ('connectionKeepalive', self.obj135))
    self.obj135.Graphical_Appearance.linkInfo=linkEditor(self,self.obj135.Graphical_Appearance.semObject, "connectionKeepalive")
    self.obj135.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('connectionKeepalive_1stLink', self.obj135.Graphical_Appearance.linkInfo.FirstLink))
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('connectionKeepalive_1stSegment', self.obj135.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj135.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj135.Graphical_Appearance.linkInfo.Center.setValue( ('connectionKeepalive_Center', self.obj135.Graphical_Appearance.linkInfo))
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('connectionKeepalive_2ndSegment', self.obj135.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj135.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('connectionKeepalive_2ndLink', self.obj135.Graphical_Appearance.linkInfo.SecondLink))
    self.obj135.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj135.Graphical_Appearance.semObject
    self.obj135.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj135.Graphical_Appearance.semObject
    self.obj135.Graphical_Appearance.linkInfo.Center.semObject=self.obj135.Graphical_Appearance.semObject
    self.obj135.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj135.Graphical_Appearance.semObject
    self.obj135.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj135.Graphical_Appearance.semObject

    # name
    self.obj135.name.setValue('connectionKeepalive')

    # displaySelect
    self.obj135.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj135.displaySelect.config = 0

    # attributes
    self.obj135.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arguments', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('interval', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj135.attributes.setValue(lcobj2)

    # cardinality
    self.obj135.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Interface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Connection', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj135.cardinality.setValue(lcobj2)

    # display
    self.obj135.display.setValue('Attributes:\n  - arguments :: List\n  - interval :: Integer\nMultiplicities:\n  - To Interface: 0 to 1\n  - From Connection: 0 to 1\n')
    self.obj135.display.setHeight(15)

    # Actions
    self.obj135.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj135.Actions.setValue(lcobj2)

    # Constraints
    self.obj135.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj135.Constraints.setValue(lcobj2)

    self.obj135.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1146.39453125,503.897540984,self.obj135)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.309, 1.4225806451612903]
    else: new_obj = None
    self.obj135.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj135)
    self.globalAndLocalPostcondition(self.obj135, rootNode)
    self.obj135.postAction( rootNode.CREATE )

    self.obj136=CD_Association3(self)
    self.obj136.isGraphObjectVisual = True

    if(hasattr(self.obj136, '_setHierarchicalLink')):
      self.obj136._setHierarchicalLink(False)

    # QOCA
    self.obj136.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj136.Graphical_Appearance.setValue( ('connectionTerminate', self.obj136))
    self.obj136.Graphical_Appearance.linkInfo=linkEditor(self,self.obj136.Graphical_Appearance.semObject, "connectionTerminate")
    self.obj136.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('connectionTerminate_1stLink', self.obj136.Graphical_Appearance.linkInfo.FirstLink))
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('connectionTerminate_1stSegment', self.obj136.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj136.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj136.Graphical_Appearance.linkInfo.Center.setValue( ('connectionTerminate_Center', self.obj136.Graphical_Appearance.linkInfo))
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('connectionTerminate_2ndSegment', self.obj136.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj136.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('connectionTerminate_2ndLink', self.obj136.Graphical_Appearance.linkInfo.SecondLink))
    self.obj136.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj136.Graphical_Appearance.semObject
    self.obj136.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj136.Graphical_Appearance.semObject
    self.obj136.Graphical_Appearance.linkInfo.Center.semObject=self.obj136.Graphical_Appearance.semObject
    self.obj136.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj136.Graphical_Appearance.semObject
    self.obj136.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj136.Graphical_Appearance.semObject

    # name
    self.obj136.name.setValue('connectionTerminate')

    # displaySelect
    self.obj136.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj136.displaySelect.config = 0

    # attributes
    self.obj136.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arguments', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj136.attributes.setValue(lcobj2)

    # cardinality
    self.obj136.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Interface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Connection', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj136.cardinality.setValue(lcobj2)

    # display
    self.obj136.display.setValue('Attributes:\n  - arguments :: List\nMultiplicities:\n  - To Interface: 0 to 1\n  - From Connection: 0 to 1\n')
    self.obj136.display.setHeight(15)

    # Actions
    self.obj136.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj136.Actions.setValue(lcobj2)

    # Constraints
    self.obj136.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj136.Constraints.setValue(lcobj2)

    self.obj136.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1423.39453125,356.053278689,self.obj136)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.309, 1.185483870967742]
    else: new_obj = None
    self.obj136.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj136)
    self.globalAndLocalPostcondition(self.obj136, rootNode)
    self.obj136.postAction( rootNode.CREATE )

    self.obj137=CD_Association3(self)
    self.obj137.isGraphObjectVisual = True

    if(hasattr(self.obj137, '_setHierarchicalLink')):
      self.obj137._setHierarchicalLink(False)

    # QOCA
    self.obj137.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj137.Graphical_Appearance.setValue( ('domainInterface2Interface', self.obj137))
    self.obj137.Graphical_Appearance.linkInfo=linkEditor(self,self.obj137.Graphical_Appearance.semObject, "domainInterface2Interface")
    self.obj137.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('domainInterface2Interface_1stLink', self.obj137.Graphical_Appearance.linkInfo.FirstLink))
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('domainInterface2Interface_1stSegment', self.obj137.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj137.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj137.Graphical_Appearance.linkInfo.Center.setValue( ('domainInterface2Interface_Center', self.obj137.Graphical_Appearance.linkInfo))
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('domainInterface2Interface_2ndSegment', self.obj137.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj137.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('domainInterface2Interface_2ndLink', self.obj137.Graphical_Appearance.linkInfo.SecondLink))
    self.obj137.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj137.Graphical_Appearance.semObject
    self.obj137.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj137.Graphical_Appearance.semObject
    self.obj137.Graphical_Appearance.linkInfo.Center.semObject=self.obj137.Graphical_Appearance.semObject
    self.obj137.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj137.Graphical_Appearance.semObject
    self.obj137.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj137.Graphical_Appearance.semObject

    # name
    self.obj137.name.setValue('domainInterface2Interface')

    # displaySelect
    self.obj137.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj137.displaySelect.config = 0

    # attributes
    self.obj137.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arguments', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj137.attributes.setValue(lcobj2)

    # cardinality
    self.obj137.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Interface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('DomainInterface', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj137.cardinality.setValue(lcobj2)

    # display
    self.obj137.display.setValue('Attributes:\n  - arguments :: List\nMultiplicities:\n  - To Interface: 0 to 1\n  - From DomainInterface: 0 to 1\n')
    self.obj137.display.setHeight(15)

    # Actions
    self.obj137.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj137.Actions.setValue(lcobj2)

    # Constraints
    self.obj137.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj137.Constraints.setValue(lcobj2)

    self.obj137.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(874.20703125,92.6680327869,self.obj137)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.554, 1.185483870967742]
    else: new_obj = None
    self.obj137.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj137)
    self.globalAndLocalPostcondition(self.obj137, rootNode)
    self.obj137.postAction( rootNode.CREATE )

    self.obj138=CD_Association3(self)
    self.obj138.isGraphObjectVisual = True

    if(hasattr(self.obj138, '_setHierarchicalLink')):
      self.obj138._setHierarchicalLink(False)

    # QOCA
    self.obj138.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj138.Graphical_Appearance.setValue( ('domainAdapter2domainOutput', self.obj138))
    self.obj138.Graphical_Appearance.linkInfo=linkEditor(self,self.obj138.Graphical_Appearance.semObject, "domainAdapter2domainOutput")
    self.obj138.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('domainAdapter2domainOutput_1stLink', self.obj138.Graphical_Appearance.linkInfo.FirstLink))
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('domainAdapter2domainOutput_1stSegment', self.obj138.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj138.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj138.Graphical_Appearance.linkInfo.Center.setValue( ('domainAdapter2domainOutput_Center', self.obj138.Graphical_Appearance.linkInfo))
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('domainAdapter2domainOutput_2ndSegment', self.obj138.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj138.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('domainAdapter2domainOutput_2ndLink', self.obj138.Graphical_Appearance.linkInfo.SecondLink))
    self.obj138.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj138.Graphical_Appearance.semObject
    self.obj138.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj138.Graphical_Appearance.semObject
    self.obj138.Graphical_Appearance.linkInfo.Center.semObject=self.obj138.Graphical_Appearance.semObject
    self.obj138.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj138.Graphical_Appearance.semObject
    self.obj138.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj138.Graphical_Appearance.semObject

    # name
    self.obj138.name.setValue('domainAdapter2domainOutput')

    # displaySelect
    self.obj138.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj138.displaySelect.config = 0

    # attributes
    self.obj138.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj138.attributes.setValue(lcobj2)

    # cardinality
    self.obj138.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('DomainOutput', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('DomainAdapter', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj138.cardinality.setValue(lcobj2)

    # display
    self.obj138.display.setValue('Multiplicities:\n  - To DomainOutput: 0 to N\n  - From DomainAdapter: 0 to N\n')
    self.obj138.display.setHeight(15)

    # Actions
    self.obj138.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj138.Actions.setValue(lcobj2)

    # Constraints
    self.obj138.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj138.Constraints.setValue(lcobj2)

    self.obj138.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(443.8359375,408.5,self.obj138)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.672258064516129, 1.0]
    else: new_obj = None
    self.obj138.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj138)
    self.globalAndLocalPostcondition(self.obj138, rootNode)
    self.obj138.postAction( rootNode.CREATE )

    self.obj139=CD_Association3(self)
    self.obj139.isGraphObjectVisual = True

    if(hasattr(self.obj139, '_setHierarchicalLink')):
      self.obj139._setHierarchicalLink(False)

    # QOCA
    self.obj139.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj139.Graphical_Appearance.setValue( ('domainAdapter2domainInterface', self.obj139))
    self.obj139.Graphical_Appearance.linkInfo=linkEditor(self,self.obj139.Graphical_Appearance.semObject, "domainAdapter2domainInterface")
    self.obj139.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('domainAdapter2domainInterface_1stLink', self.obj139.Graphical_Appearance.linkInfo.FirstLink))
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('domainAdapter2domainInterface_1stSegment', self.obj139.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj139.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj139.Graphical_Appearance.linkInfo.Center.setValue( ('domainAdapter2domainInterface_Center', self.obj139.Graphical_Appearance.linkInfo))
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('domainAdapter2domainInterface_2ndSegment', self.obj139.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj139.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('domainAdapter2domainInterface_2ndLink', self.obj139.Graphical_Appearance.linkInfo.SecondLink))
    self.obj139.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj139.Graphical_Appearance.semObject
    self.obj139.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj139.Graphical_Appearance.semObject
    self.obj139.Graphical_Appearance.linkInfo.Center.semObject=self.obj139.Graphical_Appearance.semObject
    self.obj139.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj139.Graphical_Appearance.semObject
    self.obj139.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj139.Graphical_Appearance.semObject

    # name
    self.obj139.name.setValue('domainAdapter2domainInterface')

    # displaySelect
    self.obj139.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj139.displaySelect.config = 0

    # attributes
    self.obj139.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj139.attributes.setValue(lcobj2)

    # cardinality
    self.obj139.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('DomainInterface', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('DomainAdapter', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj139.cardinality.setValue(lcobj2)

    # display
    self.obj139.display.setValue('Multiplicities:\n  - To DomainInterface: 0 to 1\n  - From DomainAdapter: 0 to 1\n')
    self.obj139.display.setHeight(15)

    # Actions
    self.obj139.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj139.Actions.setValue(lcobj2)

    # Constraints
    self.obj139.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj139.Constraints.setValue(lcobj2)

    self.obj139.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(194.78125,186.0,self.obj139)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7651612903225804, 1.0]
    else: new_obj = None
    self.obj139.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj139)
    self.globalAndLocalPostcondition(self.obj139, rootNode)
    self.obj139.postAction( rootNode.CREATE )

    self.obj140=CD_Association3(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # QOCA
    self.obj140.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj140.Graphical_Appearance.setValue( ('interface2domainOutput', self.obj140))
    self.obj140.Graphical_Appearance.linkInfo=linkEditor(self,self.obj140.Graphical_Appearance.semObject, "interface2domainOutput")
    self.obj140.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('interface2domainOutput_1stLink', self.obj140.Graphical_Appearance.linkInfo.FirstLink))
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('interface2domainOutput_1stSegment', self.obj140.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj140.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj140.Graphical_Appearance.linkInfo.Center.setValue( ('interface2domainOutput_Center', self.obj140.Graphical_Appearance.linkInfo))
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('interface2domainOutput_2ndSegment', self.obj140.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj140.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('interface2domainOutput_2ndLink', self.obj140.Graphical_Appearance.linkInfo.SecondLink))
    self.obj140.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj140.Graphical_Appearance.semObject
    self.obj140.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj140.Graphical_Appearance.semObject
    self.obj140.Graphical_Appearance.linkInfo.Center.semObject=self.obj140.Graphical_Appearance.semObject
    self.obj140.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj140.Graphical_Appearance.semObject
    self.obj140.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj140.Graphical_Appearance.semObject

    # name
    self.obj140.name.setValue('interface2domainOutput')

    # displaySelect
    self.obj140.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj140.displaySelect.config = 0

    # attributes
    self.obj140.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj140.attributes.setValue(lcobj2)

    # cardinality
    self.obj140.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('DomainOutput', (('Source', 'Destination'), 0), '0', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Interface', (('Source', 'Destination'), 1), '0', '1'))
    lcobj2.append(cobj2)
    self.obj140.cardinality.setValue(lcobj2)

    # display
    self.obj140.display.setValue('Multiplicities:\n  - To DomainOutput: 0 to 1\n  - From Interface: 0 to 1\n')
    self.obj140.display.setHeight(15)

    # Actions
    self.obj140.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj140.Actions.setValue(lcobj2)

    # Constraints
    self.obj140.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj140.Constraints.setValue(lcobj2)

    self.obj140.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(845.22265625,229.334016393,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.33, 1.0]
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj141=CD_Inheritance3(self)
    self.obj141.isGraphObjectVisual = True

    if(hasattr(self.obj141, '_setHierarchicalLink')):
      self.obj141._setHierarchicalLink(False)

    self.obj141.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(215.0,405.0,self.obj141)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj141.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj141)
    self.globalAndLocalPostcondition(self.obj141, rootNode)
    self.obj141.postAction( rootNode.CREATE )

    self.obj142=CD_Inheritance3(self)
    self.obj142.isGraphObjectVisual = True

    if(hasattr(self.obj142, '_setHierarchicalLink')):
      self.obj142._setHierarchicalLink(False)

    self.obj142.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(780.40625,401.0,self.obj142)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj142.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj142)
    self.globalAndLocalPostcondition(self.obj142, rootNode)
    self.obj142.postAction( rootNode.CREATE )

    self.obj143=CD_Inheritance3(self)
    self.obj143.isGraphObjectVisual = True

    if(hasattr(self.obj143, '_setHierarchicalLink')):
      self.obj143._setHierarchicalLink(False)

    self.obj143.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(996.0,601.0,self.obj143)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj143.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj143)
    self.globalAndLocalPostcondition(self.obj143, rootNode)
    self.obj143.postAction( rootNode.CREATE )

    self.obj144=CD_Inheritance3(self)
    self.obj144.isGraphObjectVisual = True

    if(hasattr(self.obj144, '_setHierarchicalLink')):
      self.obj144._setHierarchicalLink(False)

    self.obj144.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(126.0,431.0,self.obj144)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj144.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj144)
    self.globalAndLocalPostcondition(self.obj144, rootNode)
    self.obj144.postAction( rootNode.CREATE )

    # Connections for obj119 (graphObject_: Obj62) named DifferentialSpeedAdapter
    self.drawConnections(
(self.obj119,self.obj141,[283.0, 501.0, 215.0, 405.0],"true", 2) )
    # Connections for obj120 (graphObject_: Obj63) named DomainAdapter
    self.drawConnections(
(self.obj120,self.obj138,[392.40234375, 361.0, 454.671875, 426.5, 443.8359375, 408.5],"true", 3),
(self.obj120,self.obj139,[191.78125, 241.0, 194.78125, 186.0],"true", 2) )
    # Connections for obj121 (graphObject_: Obj64) named Connection
    self.drawConnections(
(self.obj121,self.obj133,[846.15234375, 474.08196721311475, 915.076171875, 546.0],"true", 2),
(self.obj121,self.obj134,[846.15234375, 474.08196721311475, 1392.02148438, 513.778688525],"true", 2),
(self.obj121,self.obj135,[846.15234375, 474.08196721311475, 1146.39453125, 503.897540984],"true", 2),
(self.obj121,self.obj136,[846.15234375, 358.40983606557376, 1423.39453125, 356.053278689],"true", 2) )
    # Connections for obj122 (graphObject_: Obj65) named SerialConnection
    self.drawConnections(
(self.obj122,self.obj142,[776.0, 641.0, 780.40625, 401.0],"true", 2) )
    # Connections for obj123 (graphObject_: Obj66) named Threading
    self.drawConnections(
 )
    # Connections for obj124 (graphObject_: Obj67) named SingleThreading
    self.drawConnections(
(self.obj124,self.obj143,[1016.0, 721.0, 996.0, 601.0],"true", 2) )
    # Connections for obj125 (graphObject_: Obj68) named Primitive
    self.drawConnections(
(self.obj125,self.obj132,[907.0, 141.3606557377049, 675.72265625, 58.168032786885234, 643.212890625, 93.834016393],"true", 3) )
    # Connections for obj126 (graphObject_: Obj69) named Interface
    self.drawConnections(
(self.obj126,self.obj131,[1304.75, 279.0, 1280.5, 330.0, 1219.25, 335.0],"true", 3),
(self.obj126,self.obj140,[1121.109375, 239.2377049180328, 845.22265625, 229.33401639344265],"true", 2) )
    # Connections for obj127 (graphObject_: Obj70) named StateVariable
    self.drawConnections(
 )
    # Connections for obj128 (graphObject_: Obj71) named RangeAdapter
    self.drawConnections(
(self.obj128,self.obj144,[116.0, 501.0, 126.0, 431.0],"true", 2) )
    # Connections for obj129 (graphObject_: Obj72) named DomainInterface
    self.drawConnections(
(self.obj129,self.obj137,[551.66015625, 96.0, 874.20703125, 92.6680327869],"true", 2) )
    # Connections for obj130 (graphObject_: Obj73) named DomainOutput
    self.drawConnections(
 )
    # Connections for obj131 (graphObject_: Obj74) named interface2primitive
    self.drawConnections(
(self.obj131,self.obj125,[1219.25, 335.0, 1158.0, 340.0, 1108.7421875, 347.40163934426226],"true", 3) )
    # Connections for obj132 (graphObject_: Obj76) named primitive2connection
    self.drawConnections(
(self.obj132,self.obj121,[643.212890625, 93.834016393, 610.703125, 129.5, 630.0, 300.5737704918034],"true", 3) )
    # Connections for obj133 (graphObject_: Obj78) named connection2threading
    self.drawConnections(
(self.obj133,self.obj123,[915.076171875, 546.0, 1141.42578125, 661.0],"true", 2) )
    # Connections for obj134 (graphObject_: Obj80) named connectionStartup
    self.drawConnections(
(self.obj134,self.obj126,[1392.02148438, 513.778688525, 1368.625, 279.0],"true", 2) )
    # Connections for obj135 (graphObject_: Obj82) named connectionKeepalive
    self.drawConnections(
(self.obj135,self.obj126,[1146.39453125, 503.897540984, 1177.0, 279.0],"true", 2) )
    # Connections for obj136 (graphObject_: Obj84) named connectionTerminate
    self.drawConnections(
(self.obj136,self.obj126,[1423.39453125, 356.053278689, 1368.625, 279.0],"true", 2) )
    # Connections for obj137 (graphObject_: Obj86) named domainInterface2Interface
    self.drawConnections(
(self.obj137,self.obj126,[874.20703125, 92.6680327869, 1121.109375, 80.18852459016392],"true", 2) )
    # Connections for obj138 (graphObject_: Obj88) named domainAdapter2domainOutput
    self.drawConnections(
(self.obj138,self.obj130,[443.8359375, 408.5, 433.0, 390.5, 423.0, 281.0],"true", 3) )
    # Connections for obj139 (graphObject_: Obj90) named domainAdapter2domainInterface
    self.drawConnections(
(self.obj139,self.obj129,[194.78125, 186.0, 201.49609375, 121.0],"true", 2) )
    # Connections for obj140 (graphObject_: Obj92) named interface2domainOutput
    self.drawConnections(
(self.obj140,self.obj130,[845.22265625, 229.33401639344265, 699.3359375, 236.0],"true", 2) )
    # Connections for obj141 (graphObject_: Obj94) of type CD_Inheritance3
    self.drawConnections(
(self.obj141,self.obj120,[215.0, 405.0, 193.375, 381.0],"true", 2) )
    # Connections for obj142 (graphObject_: Obj96) of type CD_Inheritance3
    self.drawConnections(
(self.obj142,self.obj121,[780.40625, 401.0, 846.15234375, 398.8950819672131],"true", 2) )
    # Connections for obj143 (graphObject_: Obj98) of type CD_Inheritance3
    self.drawConnections(
(self.obj143,self.obj123,[996.0, 601.0, 1141.42578125, 661.0],"true", 2) )
    # Connections for obj144 (graphObject_: Obj100) of type CD_Inheritance3
    self.drawConnections(
(self.obj144,self.obj120,[126.0, 431.0, 126.0, 381.0],"true", 2) )

newfunction = RDIS_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
