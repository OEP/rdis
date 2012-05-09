#!/usr/bin/env python

from ROSBoolean import ROSBoolean
from ROSTwist import ROSTwist
import a3t
import os
import tkMessageBox

reload(a3t)

gDebug = False

## Report constraint violations to ATOM3.
gErrorLog = []

gPath = "/home/pkilgo/gen" if gDebug else os.path.dirname(__file__)

def genPath(relpath):
  return absPath("gen/{}".format(relpath))

def absPath(filename):
  global gPath
  return os.path.abspath("{}/{}".format(gPath,filename))

def reportError(msg, semObj=None):
  global gErrorLog
  gErrorLog.append( (msg,semObj) )

def readFile(filename):
  global gPath
  filepath = absPath(filename)
  try:
    fp = open(filepath, "r")
    contents = fp.read()
    fp.close()
    return contents
  except IOError as e:
    msg = "Error loading '{}': {}".format(filepath, str(e))
    print(msg)
    reportError(msg)
    return "<-- TEMPLATE ERROR -->"

## TEMPLATES
gNodeTemplate = readFile("templates/node.template.py")
gTwistCallbackTemplate = readFile("templates/twistCallback.template.py")
gBoolPublisherTemplate = readFile("templates/boolPublisher.template.py")
gSubscribeInit = "rospy.Subscriber('{topicName}',{topicType},{topicCallback})"
gPublisherInit = "registerPublisher('{outputName}', rospy.Publisher('{topicName}', {topicType}), {callback})"


## Maps ATOM3 types to names of ROS types.
gTopicTypeMap = {
  'ROSTwist': 'Twist',
  'ROSBoolean': 'Bool'
}

## Buffer for textblob-building.
gLinesBuffer = []

def pushBuf():
  """
  Creates a new text buffer for us to work with.
  """
  global gLinesBuffer
  gLinesBuffer.append([])
 
def write(line, indent=0):
  """
  Writes a line to a buffer with an optional indentation.
  """
  global gLinesBuffer
  gLinesBuffer[-1].append(" "*indent + line)

def indentBlob(blob, indent=2):
  """
  Indents a blob of text by some indentation amount, 2 by default.
  """
  return "\n".join(indentLines(blob.split("\n"), indent))

def indentLines(lines, indent=2):
  """
  Indents a list of strings by some amount, 2 by default.
  """
  ind = lambda x: " "*indent + x
  return list(map(ind, lines))

def flush(indent=0):
  """
  Flushes the top of the buffer stack.
  """
  global gLinesBuffer
  blob = "\n".join(indentLines(gLinesBuffer[-1]))
  gLinesBuffer.pop(-1)
  return blob

def hasErrors():
  """
  Returns true if there were errors.
  """
  global gErrorLog
  return len(gErrorLog) > 0

def getError():
  """
  Gets first error.
  """
  if not hasErrors(): return None
  global gErrorLog
  return gErrorLog[0]

def clearErrors():
  """
  Clears all errors.
  """
  gErrorLog = []

def compile(atom3i):
  """
  Entry point for ATOM3. Compiles all ROS nodes.
  """
  global gPath
  a3t.setInstance(atom3i)

  outPath = genPath("")
  if not compileNodes() and hasErrors():
    return getError()
  else:
    tkMessageBox.showinfo("RDIS", "Files generated in: " + outPath)

def getASG():
  """
  Gets the ROS ASG.
  """
  return a3t.getASG("ROSApp_META")

def compileNodes():
  """
  Compiles all ROS nodes.
  """
  rosNodes = getROSNodes()
  result = True
  for rosNode in rosNodes:
    result = result and compileNode(rosNode)
  return result

def getROSNodes():
  """
  Returns semantic object list of ROS nodes.
  """
  return a3t.getNodesOfType( getASG(), "ROSNode" )
  
def compileNode(rosNode):
  """
  Compiles a particular ROS node.
  """
  global gNodeTemplate
  print
  print
  print "==================== COMPILING ========================="
  print
  print

  nname = a3t.evalAtom3Type(rosNode.name)
  ncallbacks = getCallbackSection(rosNode)
  ninitialization = getInitializationSection(rosNode)
  filepath = genPath("{}.gen.py".format(nname))

  if not hasErrors():
    try:
      fp = open(filepath, "w")
      fp.write(
        gNodeTemplate.format(
          nodeName=nname,
          callbackSection=ncallbacks,
          initializationSection=ninitialization
        )
      )
      fp.close()
      print "Written: {}".format(filepath)
      return filepath
    except IOError as e:
      print "Error writing to '{}': {}".format(
        filepath,
        str(e)
      )
      reportError(str(e), None)
  return False

def nameOf(semObj):
  """
  Gets attribute "name" from semantic object.
  """
  return a3t.evalAtom3Type(semObj.name)

def typeOf(semObj):
  """
  Gets the class name of semantic object.
  """
  return semObj.__class__.__name__

def rosType(semObj):
  """
  Maps ATOM3 ROS type names to actual ROS type names.
  """
  global gTopicTypeMap
  return gTopicTypeMap[typeOf(semObj)]

def getType(rosTopic):
  """
  Gets the ATOM3 ROS type for a topic.
  """
  topicType = a3t.outTwo(rosTopic, "ROSType")
  if topicType == None:
    reportError("ROS topic must have a type.", rosTopic)
  return topicType

def getOutput(rosTopic):
  """
  Gets the domain output associated with this topic.
  """
  do = a3t.inTwo(rosTopic, "GenericGraphEdge")
  if do == None:
    reportError("ROS published topic must be connected to RDIS domain output!", rosTopic)
  return do

def getInterface(rosTopic):
  """
  Gets domain interface associated with topic.
  """
  di = a3t.outTwo(rosTopic, "GenericGraphEdge")
  if di == None:
    reportError("ROS subscribed topic must be connected to RDIS domain interface!", rosTopic)
    return None
  return di

def getInterfaceAdapter(di):
  """
  Gets domain adapter associated with domain interface.
  """
  dit = a3t.inTwo(di, "domainAdapter2domainInterface")
  if dit == None:
    reportError("Domain interface has no adapter tied to it.", di)
    return None
  return dit

def getOutputAdapter(do):
  """
  Gets domain adapter associated with domain output.
  """
  adapter = a3t.inTwo(do, "domainAdapter2domainOutput")
  if adapter == None:
    reportError("Domain output has no adapter tied to it.", do)
    return None
  return adapter

def getCallbackSection(rosNode):
  """
  Returns textblob with generated callbacks and publish actions.
  """
  global gTwistCallbackTemplate
  subscribed = a3t.filterInEntities(rosNode, "ROSSubscribe")
  publishers = a3t.filterOutEntities(rosNode, "ROSPublish")
  blob = ""

  blob += "## ============ GENERATED SUBSCRIPTION CALLBACKS ==================\n\n"
  for topic in subscribed:
    blob += getCallback(topic)

  blob += "## ================= GENERATED PUBLISH ACTIONS ==================\n\n"
  for topic in publishers:
    blob += getPublishAction(topic)

  return blob

def getCallback(rosTopic):
  """
  Gets callback textblob associated with topic.
  """
  ttype = rosType(getType(rosTopic))

  if ttype == "Twist":
    return getTwistCallback(rosTopic)
  else:
    return "## Unknown topic type: " + ttype + "\n"

def getTwistCallback(rosTopic):
  """
  Gets twist callback textblob for given topic.
  """
  global gTwistCallbackTemplate
  tname = nameOf(rosTopic)
  di = getInterface(rosTopic)
  dit = getInterfaceAdapter(di)
  rdisStmts = getMappings( dit )

  return gTwistCallbackTemplate.format(
    name = tname,
    toRdis = rdisStmts,
    domainInterface = a3t.evalAtom3Type(di.name),
  )

def getPublishAction(rosTopic):
  """
  Gets publish action associated with this topic.
  """
  ttype = rosType(getType(rosTopic))
  if ttype == "Bool":
    return getBoolPublishAction(rosTopic)
  else:
    return "## Unknown topic type: " + ttype + "\n"

def getBoolPublishAction(rosTopic):
  """
  Gets boolean publisher action as a textblob.
  """
  global gBoolPublisherTemplate
  tname = nameOf(rosTopic)
  do = getOutput(rosTopic)
  adapter = getOutputAdapter(do)
  rosType = getType(rosTopic)

  return gBoolPublisherTemplate.format(
      name = tname,
      initialization = getInitializations(adapter),
      mappingStatements = getMappings(rosType),
      callback = makePublishActionName(tname)
  )

def getInitializations(adapterType, msgName="rdisMsg"):
  """
  For each attribute in adapterType, generate a statement which initializes
  that attribute in an environment. Return as a textblob.
  """
  pushBuf()
  mappings = a3t.gen2dict(adapterType)

  for (key,value) in mappings.items():
    write("env['{}'] = {}['{}']".format(key, msgName, key))
  return flush()

def getMappings(adapterType):
  """
  Generates statements which perform the argument transformation.
  """
  pushBuf()
  mappings = a3t.gen2dict(adapterType)

  for (key, value) in mappings.items():
    write("env['{}'] = rdis.safeEval('{}', env)".format(key, value))

  return flush()

def getInitializationSection(rosNode):
  """
  Generates statements which initialize ROS publishers and subscribers.
  """
  global gSubscribeInit
  global gPublisherInit
  linesBuffer = []
  subscribeTopics = a3t.filterInEntities(rosNode, "ROSSubscribe")
  publishTopics = a3t.filterOutEntities(rosNode, "ROSPublish")

  pushBuf()

  for topic in subscribeTopics:
    name = nameOf(topic)
    ttype = rosType(getType(topic))
    tcallback = makeCallbackName(name)
    write(gSubscribeInit.format(topicName=name, topicType=ttype,
      topicCallback=tcallback))

  for topic in publishTopics:
    name = nameOf(topic)
    ttype = rosType(getType(topic))
    outputName = nameOf(getOutput(topic))

    write(
      gPublisherInit.format(
        topicName=name,
        topicType=ttype,
        outputName=outputName,
        callback = makePublishActionName(name)
      )
    )

  return flush(2)

def makeCallbackName(topicName):
  return "{}_callback".format(topicName)

def makePublishActionName(topicName):
  return "publish_{}".format(topicName)
