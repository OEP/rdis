#!/usr/bin/env python

"""
A module containing functions for navigating AToM3 abstract syntax graphs.

Many of these functions assume a 1-to-1 type relation between entities but
this is a pretty common design pattern, at least for simple models.

Setup:
  import a3t
  a3t.setInstance( atom3i )

written by Paul Kilgo
"""

## Reference to the AToM3 instance.
gAtom3i = None

def setInstance(atom3i):
  """
  Set the ATOM3 instance to work with.
  """
  global gAtom3i
  gAtom3i = atom3i

def getASG(name):
  """
  Gets an ASG by name in our ATOM3 instance.
  """
  global gAtom3i
  return gAtom3i.ASGroot.getASGbyName(name)

def getNodesOfType(asg, nodeType):
  """
  From a given ASG, return a list of the nodes of a given type.
  """
  return list( asg.listNodes[nodeType] )

def getAttributes(semObj):
  """
  Returns a list of the names of the generated attributes for the
  given semantic object.
  """
  return list( semObj.generatedAttributes.keys() )

def getClassName(thing):
  """
  Returns the class name as a string.
  """
  return thing.__class__.__name__

def gen2dict(semObj):
  """
  Returns a dict() with name-value pairs of the generated attributes
  of a given semantic object.
  """
  obj = dict()
  for key in getAttributes(semObj):
    thing = getattr(semObj, key)
    obj[key] = evalAtom3Type(thing)
  return obj

def evalAtom3Type(thing):
  """
  Evaluates ATOM3Types to corresponding Python type.
  """
  className = thing.__class__.__name__

  if className == "ATOM3String":
    return evalAtom3String( thing )
  elif className == "ATOM3List":
    return evalAtom3List( thing )
  elif className == "ATOM3Enum":
    return evalAtom3Enum( thing )
  elif className == "ATOM3Integer":
    return evalAtom3Integer( thing )
  else:
    print "Unknown ATOM3Type: {}".format(className)
    return None

def evalAtom3Integer( thing ):
  """
  Evaluates an ATOM3Integer to a Python integer.
  """
  return thing.getValue()

def evalAtom3Enum( thing ):
  """
  Evaluates an ATOM3Enum to a Python string.
  """
  tmp = thing.getValue()
  return tmp[0][tmp[1]]

def evalAtom3String( thing ):
  """
  Evaulates an ATOM3String to a Python string.
  """
  return thing.getValue()

def evalAtom3List( thing ):
  """
  Evaluates an ATOM3List to a Python list.
  """
  return list(map(evalAtom3Type, thing.objectList))

def outEdgesWithNodes(node, typeFilter=None):
  """
  For one to one connections.
  Returns tupling of node's out-edges, with the nodes they connect to.
  """
  return tupledLinksNodes(node, "out_connections_", typeFilter)

def tupledLinksNodes(node, whichList, typeFilter=None):
  """
  For one-to-one connections.
  Returns a tupling of edges and the node on that edge.
  """
  returnValue = []
  edgeList = getattr(node, whichList)

  if typeFilter != None:
    edgeList = filterEdges(edgeList, typeFilter)

  for edge in edgeList:
    returnValue.append( (edge, getattr(edge, whichList)[0] ) )

  return returnValue

def followOne(node, edgeListName, filterType=None):
  """
  Follows first edge in the first edge in node's instance variables by
  name of the string 'edgeListName', of type filterType if given.
  """
  if node == None: return None
  edgeList = filterEdges(getattr(node, edgeListName), filterType)
  if len(edgeList) == 0: return None
  return edgeList[0]

def inOne(node, filterType=None):
  """
  Follows one inward link of a particular type.
  Returns the semantic node we end up at, or none.
  """
  return followOne(node, "in_connections_", filterType)


def outOne(node, filterType=None):
  """
  Follows one outward link of a particular type.
  Returns the semantic node we end up at, or none.
  """
  return followOne(node, "out_connections_", filterType)

def outTwo(node, filterType=None):
  """
  Follows two outward links, optionally of a particular type for
  the first link only.

  Returns the semantic node we end up at, or None.
  """
  return outOne( outOne(node, filterType) )

def inTwo(node, filterType=None):
  """
  Follows two inward links, optionally of a particular type for
  the first link only.

  Returns the semantic node we end up at, or None.
  """
  return inOne( inOne(node, filterType) )

def filterEntities(semObj, edgeType, edgeListName):
  """
  For a given semantic object, returns the semantic objects joined to it by
  connections of a particular type. The edge list to filter must be provided.
  """
  edgeList = getattr(semObj, edgeListName)
  edgeList = filterEdges(edgeList, edgeType)
  toEntity = lambda x: getattr(x, edgeListName)[0]
  return list(map(toEntity, edgeList))

def filterOutEntities(semObj, edgeType):
  """
  Gets a list of entities we're connected to by some edgeType.
  """
  return filterEntities(semObj, edgeType, "out_connections_")

def filterInEntities(semObj, edgeType):
  """
  Gets a list of entities we're connecting to us by some edgeType.
  """
  return filterEntities(semObj, edgeType, "in_connections_")

def filterOutboundEdges( semObj, edgeType):
  """
  Filter outbound edges of given semantic object by edge type.
  """
  return filterEdges(semObj.out_connections_, edgeType)

def filterEdges( edges, edgeType=None ):
  """
  Filters edges by given edgeType.
  """
  if edgeType == None: return list(edges)
  cn = lambda x: x.__class__.__name__
  test = lambda x: cn(x) == edgeType
  return list(filter(test, edges))
