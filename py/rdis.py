#!/usr/bin/env python

import struct
import re

## Dictionary which maps RDIS types to Python types.
_gTypeMap = {
  'int': 'int',
  'float': 'float',
  'string': 'str'
}

## Dictionary which maps RDIS types to their equivalent
## default values in Python.
_gDefaultValueMap = {
  'int': 0,
  'float': 0.0,
  'string': ''
}

def dictIntersect(dictBefore, dictAfter):
  """
  For keys which intersect in dictBefore and dictAfter,
  return a new dictionary containing the values of said
  keys in dictAfter.
  """
  out = dict()
  for key in dictBefore.viewkeys() & dictAfter.viewkeys():
    out[key] = dictAfter[key]
  return out


def mapDefaultValue(typeName):
  """
  Maps an RDIS type name to Python default value.
  Raises TypeError if typeName is not a valid RDIS type.
  """
  global _gDefaultValueMap

  mapType(typeName)
  return _gDefaultValueMap[typeName]

def mapType(typeName):
  """
  Maps an RDIS type to a Python type.
  Raises TypeError if typeName is not a valid RDIS type.
  """
  global _gTypeMap
  if typeName not in _gTypeMap:
    raise TypeError("Unknown RDIS type: " + str(typeName))
  return _gTypeMap[typeName]

def createEnvironment(parameterNames, values):
  env = dict()
  i = 0
  for parameter in parameterNames:
    env[parameter] = values[i]
    i += 1
  return env

def deleteAdditions(before, after):
  for key in after.viewkeys() - before.viewkeys():
    del after[key]

def safeEval(expression, env):
  """
  If expression is not a string, it returns expression.
  Otherwise, if the first and last characters of the string
  are '<' and '>', it chops them off and evaluates the resulting
  expression under the provided environment.
  """
  if not isinstance(expression, str) or len(expression) == 0:
    return expression

  returnValue = expression

  n = len(expression)
  oldEnv = dict(env)
  if expression[0] == '<' and expression[n-1] == '>':
     returnValue = eval( expression[1:n-1], env )

  ## Subtract off any keys added by eval
  deleteAdditions(oldEnv, env)

  return returnValue

def safeExecs(stmts, globalEnv=None):
  oldGlobals = dict(globalEnv)

  for stmt in stmts:
    exec(stmt, globalEnv)

  deleteAdditions(oldGlobals, globalEnv)

def safeType( value ):
  """
  Gets a string representation of value's type.
  Safe for objects and primitive types.
  """
  varType = type(value).__name__
  if varType == "instance":
    return value.__class__.__name__
  
  return varType


class RDIS:
  
  def __init__(self):
    """
    Makes an empty RDIS object.
    """
    self._primitives = dict()
    self._connections = dict()
    self._interfaces = dict()
    self._stateVariables = dict()

  def getConnection(self, name):
    return self._connections[name]

  def addPrimitive(self, name, **kwargs):
    kwargs["name"] = name
    kwargs["parent"] = self
    self._primitives[name] = apply(Primitive, [], kwargs)

  def addConnection(self, name, **kwargs):
    kwargs["name"] = name
    kwargs["parent"] = self
    self._connections[name] = apply(Connection, [], kwargs)

  def addStateVar(self, name, **kwargs):
    kwargs["name"] = name
    kwargs["parent"] = self
    self._stateVariables[name] = apply(StateVar, [], kwargs)

  def getStateVarValue(self, name):
    return self._stateVariables[name].getValue()

  def _getPrimitive(self, name):
    return self._primitives[name]

  def _callPrimitive(self, name, posArgs):
    p = self._getPrimitive(name)
    p.call(posArgs)

  def _buildStateVarEnvironment(self):
    env = dict()
    for (name, stateVar) in self._stateVariables.items():
      env[name] = stateVar.getValue()
    return env

  def _updateStateVarsFromEnvironment(self, env):
    for (name, value) in env.items():
      stateVar = self._stateVariables[name]
      stateVar.setValue(value)

class StateVar:

  def __init__(self, name=None, value=None, type=None, parent=None):
    if value == None:
      value = mapDefaultValue(type)
    self._name = name
    self._parent = parent

    self._setType(type)
    self.setValue(value)

  def getValue(self):
    return self._value

  def setValue(self,value):
    self._assertType(value)
    self._value = value

  def _assertType(self, value):
    nameType = self._getPythonType()
    valType = safeType(value)
    if not isinstance(value, eval(nameType)):
      raise TypeError(
        "Attempt to set {} ({}) to value {} ({}).".format(self._name, nameType,
        repr(value), valType)
      )

  def _getPythonType(self):
    return mapType(self._type)

  def _setType(self, newType):
    """
    Changes this StateVar's RDIS type.
    """
    mapType(newType) ## Asserts that it is a valid RDIS type.
    self._type = newType
    
class Primitive:

  def __init__(self, parent=None, pack=None, unpack=None, parameters=[], regex=None,
      format=None, name=None, connection=None, formatArgs=[], postActions=[]):
    self._parent = parent
    self._format = format
    self._name = name
    self._pack = pack
    self._unpack = unpack
    self._regex = regex
    self._connection = connection
    self._parameters = parameters
    self._formatArgs = formatArgs
    self._postActions = postActions
    
  def call(self, arguments=[]):
    env = createEnvironment(self._parameters, arguments)

    ## Evaluate all the args we send out on the format string.
    values = [safeEval(k,env) for k in self._formatArgs]

    ## Write the information on the connection and read back.
    connection = self._getConnection()
    connection.write( self._doPack(values) )
    out = self._doUnpack( connection.read() )

    ## Build environments for postActions and execute them.
    envs = self._buildPostActionEnv(env, out)
    safeExecs(self._postActions, envs[1])

    ## Delete local variables that we added.
    deleteAdditions(envs[0], envs[1])

    ## Updates stateVar from the global environment.
    self._parent._updateStateVarsFromEnvironment(envs[1])


  def _buildPostActionEnv(self, parameters, out):
    globalEnv = self._parent._buildStateVarEnvironment()
    globalCopy = dict(globalEnv)
    globalCopy.update(parameters)
    globalCopy["__out__"] = out
    return (globalEnv, globalCopy)



  def _getConnection(self):
    return self._parent.getConnection(self._connection)

  def _doPack(self, values):
    """
    Decides whether or not we need to ASCII-encode
    or custom-encode the values we are writing to
    the robot.
    """
    if self._format != None:
      return struct.pack("s", apply(self._format.format, values))
    else:
      tmp = [self._pack]
      tmp.extend(values)
      return apply(struct.pack, tmp)

  def _doUnpack(self, byteSequence):
    if self._regex != None:
      return re.match(self._regex, str(byteSequence)).groups()
    else:
      return struct.unpack(self._unpack, byteSequence)
      

class Connection:

  def __init__(self, name=None, parent=None):
    self._name = name
    self._parent = parent
    self._memory = None

  def write(self, stuff):
    self._memory = stuff
    print(stuff)

  def read(self):
    return self._memory

def main():
  rdis = RDIS()
  rdis.addStateVar("someNumber", type="int")
  rdis.addPrimitive("echo_num", pack=">I", unpack=">I", parameters=["num"],
      connection="loop", formatArgs=["<num>"],
      postActions=["someNumber = __out__[0]"])
  rdis.addConnection("loop")
  rdis._callPrimitive("echo_num", [42])

  print rdis.getStateVarValue("someNumber")

if __name__ == "__main__":
  main()
