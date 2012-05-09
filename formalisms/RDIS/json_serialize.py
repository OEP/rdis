#!/usr/bin/env python

import json
import a3t
import struct
import os
from rdis import safeEval, mapType

from SerialConnection import SerialConnection
from SingleThreading import SingleThreading
import tkMessageBox

reload(a3t)

gErrorLog = []

gDebug = False

gPath = "/home/pkilgo/gen" if gDebug else os.path.dirname(__file__)

def genPath(genFile):
  """
  Returns desired path for generated files.
  """
  return absPath("gen/{}".format(genFile))

def absPath(relpath):
  """
  Returns the absolute path to a path relative to the formalism directory.
  """
  global gPath
  return "{}/{}".format(gPath,relpath)

def json_serialize(atom3i):
  """
  Main entry point for ATom3.
  """
  a3t.setInstance(atom3i)
  root = dict()

  print
  print
  print "=============== COMPILING ====================="
  print
  print

  asg = getASG()
  graphName = a3t.evalAtom3Type(asg.name)
  graphAuthor = a3t.evalAtom3Type(asg.author)
  fp = None
  filename = None
  filepath = None

  if graphName == None or len(graphName) == 0:
    reportError("Please give your model a name.")
  else:
    try:
      filename = graphName + ".rdis.json"
      filepath = genPath(filename)
      fp = open(filepath, "w")
    except IOError as e:
      reportError(str(e))

  root["name"] = graphName
  root["author"] = graphAuthor

  addPrimitives(root)
  addInterfaces(root)
  addConnections(root)
  addDomainInterfaces(root)
  addDomainOutputs(root)
  addStateVars(root)

  if not hasErrors():
    json.dump(root, fp, indent=2)
    fp.close()
    tkMessageBox.showinfo("RDIS",
      "Model successfully serialized to file: " + filepath
    )
  else:
    errors = getErrors()
    print(str(len(errors)) + " error(s) in total.")
    i = 0
    for error in errors:
      i += 1
      print "  {:2}. ".format(i) + error[0]
    return errors[0]
  
def getErrors():
  global gErrorLog
  return gErrorLog

def getError():
  global gErrorLog
  if hasErrors():
    return gErrorLog[0]
  return None

def hasErrors():
  global gErrorLog
  return len(gErrorLog) > 0

def clearErrors():
  global gErrorLog
  gErrorLog = []

def reportError(msg, semObj=None):
  global gErrorLog
  gErrorLog.append( (msg, semObj) )

##############################################################################
#
#
#
#                         MODEL QUERIES
#
#
#
##############################################################################

def getASG():
  """
  Returns the RDIS abstract syntax graph.
  """
  return a3t.getASG('RDIS_META')

def getStateVarNames():
  """
  Returns a list of StateVar names.
  """
  nameOf = lambda x: a3t.evalAtom3Type( x.name )
  return list(map(nameOf, getStateVars()))

def getStateVars():
  """
  Returns a list of StateVar semantic objects.
  """
  return a3t.getNodesOfType(getASG(), "StateVariable")

def getPrimitives():
  """
  Returns list of Primitive semantic objects.
  """
  return a3t.getNodesOfType(getASG(), "Primitive")

def getInterfaces():
  """
  Returns a list of Interface semantic objects.
  """
  return a3t.getNodesOfType(getASG(), "Interface")

def getSerialConnections():
  """
  Returns a list of Interface semantic objects.
  """
  return a3t.getNodesOfType(getASG(), "SerialConnection")

def getDomainInterfaces():
  """
  Returns a list of DomainInterface semantic objects.
  """
  return a3t.getNodesOfType(getASG(), "DomainInterface")

def getDomainOutputs():
  """
  Returns a list of DomainInterface semantic objects.
  """
  return a3t.getNodesOfType(getASG(), "DomainOutput")

##############################################################################
#
#
#
#                         CONTEXT OBJECT CONSTRUCTION
#
#
#
##############################################################################

def addStateVars(obj):
  nodes = getStateVars()
  currentList = obj.setdefault("stateVariables", [])
  newList = list(map(stateVar2dict, nodes))
  currentList.extend(newList)

def addDomainInterfaces(obj):
  nodes = getDomainInterfaces()
  if nodes == None or len(nodes) == 0: return
  currentList = obj.setdefault("domainInterfaces", [])
  newList = list(map(domainInterface2dict, nodes))
  currentList.extend(newList)

def addDomainOutputs(obj):
  nodes = getDomainOutputs()
  if nodes == None or len(nodes) == 0: return
  currentList = obj.setdefault("domainOutputs", [])
  newList = list(map(domainOutput2dict, nodes))
  currentList.extend(newList)

def addConnections(obj):
  cnx = dict();
  obj["connections"] = cnx
  addSerialConnections(cnx)

  testConnectionCount(cnx)


def addSerialConnections(obj):
  nodes = getSerialConnections()
  if nodes == None or len(nodes) == 0: return
  serialList = obj.setdefault("spp", [])
  newSerials = list(map(connection2dict, nodes))

  serialList.extend(newSerials)

def stateVar2dict(semObj):
  out = a3t.gen2dict(semObj)
  testType(out["value"], out["type"], semObj)
  return out

def domainInterface2dict(semObj):
  out = a3t.gen2dict(semObj)

  da = a3t.inTwo(semObj, "domainAdapter2domainInterface")
  if da == None:
    reportError("Domain interface must take a domain adapter on input.", semObj)
    ## Have to short-circuit to prevent weird errors from happening.
    return out
  else:
    attributes = a3t.getAttributes(da)
    out["parameters"] = attributes

  iCall = a3t.outOne(semObj, "domainInterface2Interface")
  i = a3t.outTwo(semObj, "domainInterface2Interface")
  if i == None:
    reportError("Domain interface must call a local interface.", semObj)
  else:
    name = a3t.evalAtom3Type(i.name)
    calls = a3t.gen2dict(iCall)
    iParameters = a3t.evalAtom3Type( i.parameters )
    calls["name"] = name
    out["calls"] = calls

    ## Constraints on interface call.
    testCall(calls["arguments"], out["parameters"], iParameters, iCall)

  deleteEmptyKeys(out)

  testValidName( out.get("name"), semObj )

  return out


def connection2dict(semObj):
  out = a3t.gen2dict(semObj)

  k = a3t.outOne(semObj, "connectionKeepalive")
  s = a3t.outOne(semObj, "connectionStartup")
  t = a3t.outOne(semObj, "connectionTerminate")

  for thing in (("keepalive",k),("startup",s),("terminate",t)):
    if thing[1] != None:
      out[thing[0]] = a3t.gen2dict(thing[1])
      out[thing[0]]["name"] = a3t.evalAtom3Type( a3t.outOne(thing[1]).name)

      ## Get arguments for remote interface.
      myLocals = []
      myArgs = out[thing[0]]["arguments"]
      theirParams = a3t.evalAtom3Type(a3t.outOne(thing[1]).parameters)

      testCall(myArgs, myLocals, theirParams, thing[1])

      if thing[0] == "keepalive":
        testKeepalive(out["keepalive"], k)
        if out["keepalive"]["interval"] <= 0:
          reportError("Keepalive interval should be >0.", k)

  addThreading(out, semObj)
  
  deleteEmptyKeys(out)

  if isinstance(semObj, SerialConnection):
    testSerial(out, semObj)
  else:
    reportError("Unbound connection type: {}".format(repr(semObj.__class__)),
      semObj)

  testValidName(out.get("name"), semObj)

  return out

def addThreading(obj, connectionSem):
  threadingSem = a3t.outTwo(connectionSem, "connection2threading")

  if threadingSem == None:
    reportError("Connections must have a threading object.", connectionSem)
  else:
    threadObj = a3t.gen2dict(threadingSem)
    deleteEmptyKeys(threadObj)

    if isinstance(threadingSem, SingleThreading):
      testSingleThreading(threadObj, threadingSem)
      obj["singleThreading"] = threadObj
    else:
      reportError("Unbound threading type: {}".format(
        repr(threadingSem.__class__)),
        threading
      )



def addInterfaces(obj):
  """
  Extends RDIS object's interfaces list to have the interfaces
  in the ASG.
  """
  nodes = getInterfaces()

  interfaceList = obj.setdefault("interfaces", [])
  newInterfaces = list(map(interface2dict, nodes))
  interfaceList.extend(newInterfaces)

  if len(interfaceList) == 0:
    reportError("You must have at least one interface.")

def addPrimitives(obj):
  """
  Extends rdis object's primitives list to have the primitives
  included in the ASG.
  """
  nodes = getPrimitives()
  primList = obj.setdefault("primitives", [])
  newPrimitives = list(map(primitive2dict, nodes))
  primList.extend( newPrimitives )
  if len(primList) == 0:
    reportError("You must have at least one primitive")

def domainOutput2dict(domainOutput):
  out = a3t.gen2dict(domainOutput)

  da = a3t.inTwo(domainOutput, "domainAdapter2domainOutput")
  if da == None:
    reportError("Domain output must take a domain adapter on input.",
      domainOutput)
  else:
    returns = a3t.gen2dict(da)
    testValidArgs(returns.values(), [], da)
    out["returns"] = returns
    
  deleteEmptyKeys(out)
  testValidName(out.get("name"), domainOutput)
  return out


def interface2dict(interface):
  """
  Converts interface semantic object into a Python dict.
  """
  out = a3t.gen2dict(interface)
  out["primitiveCalls"] = getPrimitiveCalls(interface, out["parameters"])

  do = a3t.outTwo(interface, "interface2domainOutput")

  if do != None:
    outputName = a3t.evalAtom3Type(do.name)
    out["triggers"] = outputName

  deleteEmptyKeys(out)

  testValidName( out.get("name"), interface )

  return out

def getPrimitiveCalls(interface, parameters):
  semCalls = a3t.filterOutboundEdges(interface, "interface2primitive")
  output = list()

  for semCall in semCalls:
    out = a3t.gen2dict(semCall)
    primitive = a3t.outOne(semCall)
    print semCall
    out["name"] = a3t.evalAtom3Type(primitive.name)

    testPrimitiveCall(out, semCall)
    output.append(out)

  return output

def getReturns(interface):
  domainAdapter = a3t.outTwo(interface, "interface2domainAdapter")
  if domainAdapter == None: return None
  returns = a3t.gen2dict(domainAdapter)
  return returns

def primitive2dict(primitive):
  out = a3t.gen2dict(primitive)
  cnx = getPrimitiveConnection(primitive)
  deleteEmptyKeys(out)

  if cnx != None:
    out["connection"] = a3t.evalAtom3Type(cnx.name)

  testPrimitive(out, primitive)

  return out

def getPrimitiveConnection(primitive):
  cxs = a3t.filterOutEntities(primitive, "primitive2connection")
  return cxs[0] if cxs != None and len(cxs)>0 else None

def deleteEmptyKeys( obj ):
  for (key,value) in obj.items():
    if isinstance(value, str) and value == "":
      del obj[key]
    elif isinstance(value, list) and len(value) == 0:
      del obj[key]

##############################################################################
#
#
#
#                         COMPILE TIME CONSTRAINTS
#
#
#
##############################################################################

def createDummyEnvironment( localParameters ):
  """
  Given a list of names, create an environment (Python dict) with those names
  as dummy variables and the state variables.
  """
  localParameters = localParameters if localParameters != None else []
  return dict.fromkeys( localParameters + getStateVarNames() )

def testConnectionCount(cnx):
  count = 0
  for t in ["spp"]:
    tmp = cnx.get(t,[])
    count += len(tmp)

  if count == 0:
    reportError("You must have at least one connection.", None)

def testPrimitiveCall(out, primCall):
  primitive = a3t.outOne(primCall)
  theirParams = a3t.evalAtom3Type(primitive.parameters)
  myArgs = a3t.evalAtom3Type(primCall.arguments)
  myLocals = a3t.evalAtom3Type( a3t.inOne(primCall).parameters )
  testCall( myArgs, myLocals, theirParams, primCall )

  if out["delay"] < 0:
    reportError("Delay must be >0.", primCall)

def testPrimitive(out, primitive):
  if out.get("connection") == None:
    reportError("Primitives must have connections.", primitive)

  ## Python has no logical xor. So this says:
  ## Primitive has one of "pack" or "format" but not both.
  if not bool("pack" in out) is not bool("format" in out):
    reportError(
      "Primitive needs one of a pack string or format string, not both.",
      primitive
    )

  ## Primitive has 0..1 of "unpack" or "regex", but not 1 of both.
  if bool("unpack" in out) and bool("regex" in out):
    reportError(
      "Primitive cannot have an unpack string and a regex string.",
      primitive
    )

  testValidName( out.get("name"), primitive )
  testValidPack( (out.get("pack"), out.get("unpack")), primitive )
  testValidRegex( (out.get("regex")), primitive)
  testValidFormat( (out.get("format")), primitive)
  testValidArgs( out.get("formatArgs"), out.get("parameters"), primitive)

def testSingleThreading(obj, semObj):
  """
  Reports error if single threading specific constraint violated.
  """
  if obj["freqHz"] <= 0:
    reportError("Threading frequency should be >0.", semObj)

def testKeepalive(obj, semObj):
  """
  Reports error if there is a serial-specific constraint violated.
  """
  if obj["interval"] <= 0:
    reportError("Keepalive interval should be >0.", semObj)

def testCall(myArgs, myLocals, theirParams, semObj):
  """
  Reports error if there is an argument length mismatch or a NameError
  raised by any argument.
  """
  if len(myArgs) != len(theirParams):
    reportError("Argument length mismatch.", semObj)
  testValidArgs(myArgs, myLocals, semObj)

def testSerial(obj, semObj):
  """
  Reports error if constraints specific to SerialConnection fails.
  """
  if obj["baud"] <= 0: reportError("Baud should be >0.", semObj)

def testValidArgs( expressions, scope, sem):
  """
  Reports an error in the model if a NameError is raised while
  evaluating any of 'expressions'.
  """
  if expressions == None: return
  for expression in expressions:
    testValidEval(expression, scope, sem)


def testValidEval(expression, scope, sem ):
  """
  Reports an error in the model if a NameError is raised while
  evaluating 'expression'.
  """
  env = createDummyEnvironment( scope )
  try:
    safeEval(expression, env)
  except Exception as e:
    if isinstance(e, NameError):
      reportError( str(e), sem )
  
def testValidName( things, sem ):
  if things == None or len(things) == 0:
    reportError("Name must be specified.", sem)

def testValidPack( strings, sem ):
  """
  Attempts to verify a list of pack strings "strings" by calling struct.size()
  on each of them and catching struct.error.
  """
  if strings == None: return
  for packString in strings:
    if packString == None or len(packString) == 0: continue
    try:
      struct.calcsize(packString)
    except struct.error as e:
      reportError("Incorrect struct string '{}': {}".format(
          repr(packString),
          str(e)
          ),
        sem
      )

def testType( initValue, ptype, semObj ):
  """
  Reports error if initValue does not safeEval() to a Python type which
  corresponds to the RDIS type ptype.
  """
  if initValue == "": return
  value = None
  try:
    value = safeEval( initValue, dict() )
  except Exception as e:
    reportError( str(e), semObj)
    return

  targetType = mapType(ptype)
  if not isinstance(value, eval(targetType)):
    reportError(
      "Invalid type. Evaluated Python type '{}' but wanted '{}'.".format(
        repr(type(value)), repr(targetType)),
      semObj
    )

def testValidRegex( strings, sem ):
  pass

def testValidFormat( strings, sem):
  pass
