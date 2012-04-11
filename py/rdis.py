#!/usr/bin/env python

import struct
import re

def createEnvironment(parameterNames, values):
  env = dict()
  i = 0
  for parameter in parameterNames:
    env[parameter] = values[i]
    i += 1
  return env

def safeEval(expression, env):
  """
  If expression is not a string, it returns expression.
  Otherwise, if the first and last characters of the string
  are '<' and '>', it chops them off and evaluates the resulting
  expression under the provided environment.
  """
  if not isinstance(expression, str) or len(expression) == 0:
    return expression

  n = len(expression)
  if expression[0] == '<' and expression[n-1] == '>':
    return eval( expression[1:n-1], env )
  return expression

    

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
    self._connections[name] = apply(Connection, [], kwargs)

  def _getPrimitive(self, name):
    return self._primitives[name]

  def _callPrimitive(self, name, posArgs):
    p = self._getPrimitive(name)
    p.call(posArgs)



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

    connection = self._getConnection()
    connection.write( self._doPack(values) )
    out = self._doUnpack( connection.read() )

    ## TODO: postActions to update stateVars and shit

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

  def __init__(self, name=None):
    self._name = name
    self._memory = None

  def write(self, stuff):
    self._memory = stuff
    print(stuff)

  def read(self):
    return self._memory

def main():
  rdis = RDIS()
  rdis.addPrimitive("echo_num", pack=">I", unpack=">I", parameters=["num"],
      connection="loop", formatArgs=["<num>"])
  rdis.addConnection("loop")
  rdis._callPrimitive("echo_num", [3])

if __name__ == "__main__":
  main()
