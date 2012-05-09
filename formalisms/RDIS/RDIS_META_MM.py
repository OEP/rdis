"""
__RDIS_META_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: pkilgo
Modified: Wed Apr 11 18:06:57 2012
_______________________________________________________________________
"""
from ASG_RDIS_META import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from DifferentialSpeedAdapter       import *
from DomainAdapter       import *
from Connection       import *
from SerialConnection       import *
from Threading       import *
from SingleThreading       import *
from Primitive       import *
from Interface       import *
from StateVariable       import *
from RangeAdapter       import *
from DomainInterface       import *
from interface2primitive       import *
from primitive2connection       import *
from connection2threading       import *
from connectionStartup       import *
from connectionKeepalive       import *
from connectionTerminate       import *
from interface2domainAdapter       import *
from domainInterface2domainAdapter       import *
from domainInterface2Interface       import *
def createNewASGroot(self):
   return ASG_RDIS_META(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New DifferentialSpeedAdapter", command=lambda x=self: x.createNewDifferentialSpeedAdapter(x, 100, 100) )
    modelMenu.add_command(label="New DomainAdapter", command=lambda x=self: x.createNewDomainAdapter(x, 100, 100) )
    modelMenu.add_command(label="New Connection", command=lambda x=self: x.createNewConnection(x, 100, 100) )
    modelMenu.add_command(label="New SerialConnection", command=lambda x=self: x.createNewSerialConnection(x, 100, 100) )
    modelMenu.add_command(label="New Threading", command=lambda x=self: x.createNewThreading(x, 100, 100) )
    modelMenu.add_command(label="New SingleThreading", command=lambda x=self: x.createNewSingleThreading(x, 100, 100) )
    modelMenu.add_command(label="New Primitive", command=lambda x=self: x.createNewPrimitive(x, 100, 100) )
    modelMenu.add_command(label="New Interface", command=lambda x=self: x.createNewInterface(x, 100, 100) )
    modelMenu.add_command(label="New StateVariable", command=lambda x=self: x.createNewStateVariable(x, 100, 100) )
    modelMenu.add_command(label="New RangeAdapter", command=lambda x=self: x.createNewRangeAdapter(x, 100, 100) )
    modelMenu.add_command(label="New DomainInterface", command=lambda x=self: x.createNewDomainInterface(x, 100, 100) )
    modelMenu.add_command(label="New interface2primitive", command=lambda x=self: x.createNewinterface2primitive(x, 100, 100) )
    modelMenu.add_command(label="New primitive2connection", command=lambda x=self: x.createNewprimitive2connection(x, 100, 100) )
    modelMenu.add_command(label="New connection2threading", command=lambda x=self: x.createNewconnection2threading(x, 100, 100) )
    modelMenu.add_command(label="New connectionStartup", command=lambda x=self: x.createNewconnectionStartup(x, 100, 100) )
    modelMenu.add_command(label="New connectionKeepalive", command=lambda x=self: x.createNewconnectionKeepalive(x, 100, 100) )
    modelMenu.add_command(label="New connectionTerminate", command=lambda x=self: x.createNewconnectionTerminate(x, 100, 100) )
    modelMenu.add_command(label="New interface2domainAdapter", command=lambda x=self: x.createNewinterface2domainAdapter(x, 100, 100) )
    modelMenu.add_command(label="New domainInterface2domainAdapter", command=lambda x=self: x.createNewdomainInterface2domainAdapter(x, 100, 100) )
    modelMenu.add_command(label="New domainInterface2Interface", command=lambda x=self: x.createNewdomainInterface2Interface(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['RangeAdapter']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['domainInterface2Interface']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': [( 'Interface', self.createNewInterface)]
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': [( 'Interface', self.createNewInterface)]
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['Primitive']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': [( 'primitive2connection', self.createNewprimitive2connection)]
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': [( 'primitive2connection', self.createNewprimitive2connection)]
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['SingleThreading']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['connection2threading']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['StateVariable']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['domainInterface2domainAdapter']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['SerialConnection']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': [( 'connection2threading', self.createNewconnection2threading)]
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': [( 'connection2threading', self.createNewconnection2threading)]
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': [( 'connectionStartup', self.createNewconnectionStartup), ( 'connectionKeepalive', self.createNewconnectionKeepalive), ( 'connectionTerminate', self.createNewconnectionTerminate)]
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['connectionStartup']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': [( 'Interface', self.createNewInterface)]
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': [( 'Interface', self.createNewInterface)]
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['connectionTerminate']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': [( 'Interface', self.createNewInterface)]
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': [( 'Interface', self.createNewInterface)]
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['interface2domainAdapter']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['Threading']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['Connection']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': [( 'connection2threading', self.createNewconnection2threading)]
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': [( 'connection2threading', self.createNewconnection2threading)]
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': [( 'connectionStartup', self.createNewconnectionStartup), ( 'connectionKeepalive', self.createNewconnectionKeepalive), ( 'connectionTerminate', self.createNewconnectionTerminate)]
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['interface2primitive']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': [( 'Primitive', self.createNewPrimitive)]
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['DifferentialSpeedAdapter']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['primitive2connection']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': [( 'Connection', self.createNewConnection), ( 'SerialConnection', self.createNewSerialConnection)]
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': [( 'Connection', self.createNewConnection), ( 'SerialConnection', self.createNewSerialConnection)]
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': [( 'Connection', self.createNewConnection), ( 'SerialConnection', self.createNewSerialConnection)]
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': [( 'Connection', self.createNewConnection), ( 'SerialConnection', self.createNewSerialConnection)]
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['Interface']={
           'RangeAdapter': [( 'interface2domainAdapter', self.createNewinterface2domainAdapter)]
          ,'Primitive': [( 'interface2primitive', self.createNewinterface2primitive)]
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': [( 'interface2domainAdapter', self.createNewinterface2domainAdapter)]
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [( 'interface2domainAdapter', self.createNewinterface2domainAdapter)] }
    self.ConnectivityMap['DomainInterface']={
           'RangeAdapter': [( 'domainInterface2domainAdapter', self.createNewdomainInterface2domainAdapter)]
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': [( 'domainInterface2Interface', self.createNewdomainInterface2Interface)]
          ,'DomainInterface': []
          ,'DomainAdapter': [( 'domainInterface2domainAdapter', self.createNewdomainInterface2domainAdapter)]
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [( 'domainInterface2domainAdapter', self.createNewdomainInterface2domainAdapter)] }
    self.ConnectivityMap['DomainAdapter']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': []
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': []
          ,'DifferentialSpeedAdapter': [] }
    self.ConnectivityMap['connectionKeepalive']={
           'RangeAdapter': []
          ,'Primitive': []
          ,'SingleThreading': []
          ,'connection2threading': []
          ,'StateVariable': []
          ,'domainInterface2Interface': []
          ,'SerialConnection': []
          ,'connectionStartup': []
          ,'domainInterface2domainAdapter': []
          ,'connectionKeepalive': []
          ,'Threading': []
          ,'Connection': []
          ,'interface2primitive': [( 'Interface', self.createNewInterface)]
          ,'connectionTerminate': []
          ,'primitive2connection': []
          ,'Interface': []
          ,'DomainInterface': []
          ,'DomainAdapter': []
          ,'interface2domainAdapter': [( 'Interface', self.createNewInterface)]
          ,'DifferentialSpeedAdapter': [] }
    
    self.CardinalityTable['DifferentialSpeedAdapter']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': [('0', 'N', 'Destination')]
          ,'domainInterface2domainAdapter': [('0', 'N', 'Destination')]
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['DomainAdapter']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': [('0', 'N', 'Destination')]
          ,'domainInterface2domainAdapter': [('0', 'N', 'Destination')]
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['Connection']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': [('0', 'N', 'Destination')]
          ,'connection2threading': [('0', 'N', 'Source')]
          ,'connectionStartup': [('0', '1', 'Source')]
          ,'connectionKeepalive': [('0', 'N', 'Source')]
          ,'connectionTerminate': [('0', 'N', 'Source')]
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['SerialConnection']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': [('0', 'N', 'Destination')]
          ,'connection2threading': [('0', 'N', 'Source')]
          ,'connectionStartup': [('0', '1', 'Source')]
          ,'connectionKeepalive': [('0', 'N', 'Source')]
          ,'connectionTerminate': [('0', 'N', 'Source')]
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['Threading']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': [('0', 'N', 'Destination')]
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['SingleThreading']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': [('0', 'N', 'Destination')]
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['Primitive']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': [('0', 'N', 'Destination')]
          ,'primitive2connection': [('0', '1', 'Source')]
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['Interface']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': [('0', 'N', 'Source')]
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': [('0', 'N', 'Destination')]
          ,'connectionKeepalive': [('0', 'N', 'Destination')]
          ,'connectionTerminate': [('0', 'N', 'Destination')]
          ,'interface2domainAdapter': [('0', 'N', 'Source')]
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [('0', 'N', 'Destination')] }
    self.CardinalityTable['StateVariable']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['RangeAdapter']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': [('0', 'N', 'Destination')]
          ,'domainInterface2domainAdapter': [('0', 'N', 'Destination')]
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['DomainInterface']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': [('0', '1', 'Source')]
          ,'domainInterface2Interface': [('0', '1', 'Source')] }
    self.CardinalityTable['interface2primitive']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': [('0', '1', 'Source')]
          ,'Interface': [('0', '1', 'Destination')]
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['primitive2connection']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': [('0', '1', 'Source')]
          ,'SerialConnection': [('0', '1', 'Source')]
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': [('0', '1', 'Destination')]
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['connection2threading']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': [('0', 'N', 'Destination')]
          ,'SerialConnection': [('0', 'N', 'Destination')]
          ,'Threading': [('0', 'N', 'Source')]
          ,'SingleThreading': [('0', 'N', 'Source')]
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['connectionStartup']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': [('0', '1', 'Destination')]
          ,'SerialConnection': [('0', '1', 'Destination')]
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': [('0', '1', 'Source')]
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['connectionKeepalive']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': [('0', '1', 'Destination')]
          ,'SerialConnection': [('0', '1', 'Destination')]
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': [('0', '1', 'Source')]
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['connectionTerminate']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': [('0', '1', 'Destination')]
          ,'SerialConnection': [('0', '1', 'Destination')]
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': [('0', '1', 'Source')]
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['interface2domainAdapter']={
          'DifferentialSpeedAdapter': [('0', '1', 'Source')]
          ,'DomainAdapter': [('0', '1', 'Source')]
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': [('0', '1', 'Destination')]
          ,'StateVariable': []
          ,'RangeAdapter': [('0', '1', 'Source')]
          ,'DomainInterface': []
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['domainInterface2domainAdapter']={
          'DifferentialSpeedAdapter': [('0', '1', 'Source')]
          ,'DomainAdapter': [('0', '1', 'Source')]
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': []
          ,'StateVariable': []
          ,'RangeAdapter': [('0', '1', 'Source')]
          ,'DomainInterface': [('0', '1', 'Destination')]
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    self.CardinalityTable['domainInterface2Interface']={
          'DifferentialSpeedAdapter': []
          ,'DomainAdapter': []
          ,'Connection': []
          ,'SerialConnection': []
          ,'Threading': []
          ,'SingleThreading': []
          ,'Primitive': []
          ,'Interface': [('0', '1', 'Source')]
          ,'StateVariable': []
          ,'RangeAdapter': []
          ,'DomainInterface': [('0', '1', 'Destination')]
          ,'interface2primitive': []
          ,'primitive2connection': []
          ,'connection2threading': []
          ,'connectionStartup': []
          ,'connectionKeepalive': []
          ,'connectionTerminate': []
          ,'interface2domainAdapter': []
          ,'domainInterface2domainAdapter': []
          ,'domainInterface2Interface': [] }
    
    self.entitiesInMetaModel['RDIS_META']=["DifferentialSpeedAdapter", "DomainAdapter", "Connection", "SerialConnection", "Threading", "SingleThreading", "Primitive", "Interface", "StateVariable", "RangeAdapter", "DomainInterface", "interface2primitive", "primitive2connection", "connection2threading", "connectionStartup", "connectionKeepalive", "connectionTerminate", "interface2domainAdapter", "domainInterface2domainAdapter", "domainInterface2Interface"]

    
def createNewDifferentialSpeedAdapter(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = DifferentialSpeedAdapter(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["DifferentialSpeedAdapter"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_DifferentialSpeedAdapter(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_DifferentialSpeedAdapter(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("DifferentialSpeedAdapter", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewDomainAdapter(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = DomainAdapter(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["DomainAdapter"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_DomainAdapter(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_DomainAdapter(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("DomainAdapter", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewConnection(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Connection(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Connection"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Connection(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Connection(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Connection", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSerialConnection(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = SerialConnection(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["SerialConnection"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_SerialConnection(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_SerialConnection(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("SerialConnection", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewThreading(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Threading(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Threading"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Threading(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Threading(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Threading", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewSingleThreading(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = SingleThreading(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["SingleThreading"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_SingleThreading(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_SingleThreading(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("SingleThreading", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewPrimitive(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Primitive(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Primitive"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Primitive(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Primitive(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Primitive", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewInterface(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Interface(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Interface"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Interface(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Interface(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Interface", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewStateVariable(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = StateVariable(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["StateVariable"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_StateVariable(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_StateVariable(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("StateVariable", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewRangeAdapter(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = RangeAdapter(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["RangeAdapter"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_RangeAdapter(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_RangeAdapter(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("RangeAdapter", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewDomainInterface(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = DomainInterface(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["DomainInterface"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_DomainInterface(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_DomainInterface(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("DomainInterface", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewinterface2primitive(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = interface2primitive(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["interface2primitive"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_interface2primitive(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_interface2primitive(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("interface2primitive", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewprimitive2connection(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = primitive2connection(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["primitive2connection"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_primitive2connection(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_primitive2connection(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("primitive2connection", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewconnection2threading(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = connection2threading(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["connection2threading"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_connection2threading(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_connection2threading(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("connection2threading", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewconnectionStartup(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = connectionStartup(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["connectionStartup"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_connectionStartup(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_connectionStartup(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("connectionStartup", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewconnectionKeepalive(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = connectionKeepalive(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["connectionKeepalive"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_connectionKeepalive(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_connectionKeepalive(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("connectionKeepalive", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewconnectionTerminate(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = connectionTerminate(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["connectionTerminate"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_connectionTerminate(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_connectionTerminate(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("connectionTerminate", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewinterface2domainAdapter(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = interface2domainAdapter(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["interface2domainAdapter"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_interface2domainAdapter(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_interface2domainAdapter(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("interface2domainAdapter", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewdomainInterface2domainAdapter(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = domainInterface2domainAdapter(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["domainInterface2domainAdapter"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_domainInterface2domainAdapter(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_domainInterface2domainAdapter(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("domainInterface2domainAdapter", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewdomainInterface2Interface(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = domainInterface2Interface(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["domainInterface2Interface"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_domainInterface2Interface(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_domainInterface2Interface(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("domainInterface2Interface", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_RDIS_META(self)
   ne = len(self.ASGroot.listNodes["ASG_RDIS_META"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_RDIS_META", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("String", "ATOM3String", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Boolean", "ATOM3Boolean", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Float", "ATOM3Float", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Action", "ATOM3Action", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Link", "ATOM3Link", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Port", "ATOM3Port", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Connection", "ATOM3Connection", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("MSEnum", "ATOM3MSEnum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Text", "ATOM3Text", params, (None, 0) ))
    objs.append(obj)
    self.typeList.setValue(objs)

