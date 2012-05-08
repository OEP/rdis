#!/usr/bin/env python

"""
An interpreter for RDIS models and quick-n-dirty parser for the JSON concrete
syntax.

This contains several methods which are useful to other applications which are
associated somehow with RDIS and need to emulate some of its behavior.

Usage:
  import rdis
  model = rdis.load( "/path/to/my/model.rdis.json" )

  model.startup()

  while <stuff-to-do>:
    model.tick()

    if <some-event>:
      model.callDomainInterface("interface-name", ["arg1", "arg2"])

  model.terminate()
"""

import struct     ## Used to pack bytes to send over the connection
import re         ## Used for models which reply with ASCII-encoded data.
import sys        ## Used for printing error messages.
import json       ## Used to parse RDIS textual syntax.
import time       ## Used for scheduling.
import random     ## Used for dummy methods.
import string     ## Used for checking printable characters.
import serial     ## Used for serial port connections.

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
  """
  Given two parallel lists, one of names and one of values, create a
  dictionary with the corresponding name/value pairs.
  """
  env = dict()
  i = 0
  for parameter in parameterNames:
    env[parameter] = values[i]
    i += 1
  return env

def deleteAdditions(before, after):
  """
  Deletes any key which is in after, but is not in before.
  """
  for key in after.viewkeys() - before.viewkeys():
    del after[key]

def safeEval(expression, env):
  """
  If expression is not a string, it returns expression.
  Otherwise, if the first and last characters of the string
  are '<' and '>', it chops them off and evaluates the resulting
  expression under the provided environment.
  """
  if not isinstance(expression, basestring) or len(expression) == 0:
    return expression

  returnValue = expression

  oldEnv = dict(env)
  if expression[0] == '<' and expression[-1] == '>':
    returnValue = eval( expression[1:-1], env )

  ## Subtract off any keys added by eval
  deleteAdditions(oldEnv, env)

  return returnValue

def safeEvalAll(expressions, env):
  """
  Evaluates each expression contained in expression and returns the list.
  """
  return [safeEval(k,env) for k in expressions]

def safeExecs(stmts, globalEnv=None):
  """
  Calls safeExec on a sequence of statements.
  """
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

def printBytes(byteSequence):
  """
  Prints a byte sequence to stdout.
  
  If a character is printable, it will print the ASCII representation of that
  byte as well. Otherwise, it only prints the hexadecimal represenation.
  """
  for b in byteSequence:
    if b in string.printable: print hex(ord(b)), b
    else: print hex(ord(b))

def load(rdisFile):
  """
  Builds RDIS model from its textual description.

  @raises RDISExcption if the model description is invalid.
  """
  fp = open(rdisFile)
  ctx = json.load(fp)
  fp.close()

  try:
    return RDIS(contextObject=ctx)
  except KeyError as e:
    raise RDISException("Invalid RDIS description given: " + str(e))

class RDISException(Exception):
  """
  Class for RDIS-related exceptions, generally problems with the model itself.
  This will be implemented more fully one day.
  """
  pass

class RDIS:
  """
  The public class for RDIS models.

  Generally this should be constructed by calling rdis.load(), though public
  methods exist for incrementally building a model by hand. 4 in 5 computer
  scientists agree that this is generally a bad thing to do though.
  """
  
  def __init__(self, contextObject=None):
    """
    Makes an empty RDIS object.
    """
    self._primitives = dict()
    self._connections = dict()
    self._interfaces = dict()
    self._stateVariables = dict()
    self._domainInterfaces = dict()
    self._domainOutputs = dict()
    self._callback = None
    self._name = None
    self._author = None

    if contextObject != None:
      self._fromContext(contextObject)

  def setCallback(self, callback):
    """
    Sets the callback to use when a domain output is triggered.
    """
    self._callback = callback

  def callDomainInterface(self, name, env):
    """
    Calls a domain interface by its name.

    The dictionary "env" corresponds to the parameters that the domain
    interface takes.
    """
    domainInterface = self._getDomainInterface(name)
    if domainInterface == None:
      sys.stderr.write("'{}': called nonexistant domain interface\n".format(
          name
        )
      )
      return
    domainInterface.call(env)

  def startup(self, **kwargs):
    """
    Performs initialization tasks for the model.

    This should be called after the model is constructed, but before any
    real work is done as it initializes the connection to the robot and things
    like that.
    """
    for conn in self._connections.values():
      apply(conn.startup, [], kwargs)

  def terminate(self):
    """
    Performs termination tasks for the model.

    This should be called when all work is done for the model and it is not
    needed anymore. This will do things such as putting the robot into a safe
    state and releasing any resource locks.
    """
    for conn in self._connections.values():
      conn.terminate()

  def tick(self):
    """
    Notifies the model that a single cycle for the main thread of execution
    should be performed.

    This does not necessarily correspond to the tick rate of the connection,
    but this should be called at a frequency faster than that of any component
    in the model.

    TODO: Actually there is no scheduling in the model right now. This should
    be done real soon.
    """
    for conn in self._connections.values():
      conn.tick()


  def setName(self, name):
    """
    Sets the (robot) name of the model.
    """
    self._name = name

  def getName(self):
    """
    Gets the (robot) name of the model.
    """
    return self._name

  def getAuthor(self):
    """
    Gets the author of the model.
    """
    return self._author

  def getConnection(self, name):
    """
    Gets a connection by its name.
    """
    return self._connections[name]

  def addInterface(self, name, **kwargs):
    """
    Adds a local interface to the model.
    """
    return apply(self._addElement, [name, self._interfaces, Interface], kwargs)

  def addPrimitive(self, name, **kwargs):
    """
    Adds a primitive tot he model.
    """
    return apply(self._addElement, [name, self._primitives, Primitive], kwargs)

  def addSerialConnection(self, name, **kwargs):
    """
    Adds a serial connection to the model.
    """
    return apply(self._addElement, [name, self._connections, SerialConnection],
        kwargs)

  def addStateVar(self, name, **kwargs):
    """
    Adds a state variable to the model.
    """
    return apply(self._addElement, [name, self._stateVariables, StateVar],
        kwargs)

  def addDomainInterface(self, name, **kwargs):
    """
    Adds a domain interface to the model.
    """
    return apply(self._addElement, [name, self._domainInterfaces,
      DomainInterface], kwargs)

  def addDomainOutput(self, name, **kwargs):
    """
    Adds a domain output to the model.
    """
    return apply(self._addElement, [name, self._domainOutputs,
      DomainOutput], kwargs)

  def _receiveMessage(self, who, msg):
    """
    Receives a messages from one of the lower-level components to send to the
    callback.
    """
    if self._callback == None:
      sys.stderr.write("Received message but no callback assigned!\n")
      return
    self._callback({'name': who.getName(), 'contents': msg})

  def _addElement(self, name, store, classObj, **kwargs):
    """
    Generalized method for adding a model component.
    """
    kwargs["name"] = name
    kwargs["parent"] = self
    store[name] = apply(classObj, [], kwargs)

  def getStateVarValue(self, name):
    """
    Gets the (Python) value for a state variable.
    """
    return self._stateVariables[name].getValue()

  def _getDomainInterface(self, name):
    """
    Gets a domain interface by its name.
    """
    return self._domainInterfaces.get(name)

  def _getInterface(self, name):
    """
    Gets a local interface by its name.
    """
    return self._interfaces.get(name)

  def _getPrimitive(self, name):
    """
    Gets a primitive by its name.
    """
    return self._primitives.get(name)

  def _getDomainOutput(self, name):
    """
    Gets a domain output by its name.
    """
    return self._domainOutputs.get(name)

  def _callDomainOutput(self, name):
    """
    Calls a domain output.
    """
    do = self._getDomainOutput(name)
    if do == None:
      sys.stderr.write("'{}': nonexistent domain output\n".format(name))
      return
    do.call()

  def _callPrimitive(self, name, posArgs):
    """
    Calls a primitive with given positional arguments.
    """
    p = self._getPrimitive(name)
    if p == None:
      sys.stderr.write("'{}': called nonexistent primitive\n".format(name))
      return
    elif p.parameterCount() != len(posArgs):
      sys.stderr.write(
        "Arg mismatch for primitive '{}'. Got {}, expected {}\n".format(
          name, len(posArgs), p.parameterCount()
        )
      )
      return
    p.call(posArgs)

  def _callInterface(self, name, posArgs):
    """
    Calls an interface (with provided name) with given positional arguments.
    """
    i = self._getInterface(name)
    if i == None:
      sys.stderr.write("'{}': called nonexistent local interface\n".format(
          name
        )
      )
      return
    i.call(posArgs)

  def _buildStateVarEnvironment(self):
    """
    Builds a dictionary containing the names and values of the state
    variables.
    """
    env = dict()
    for (name, stateVar) in self._stateVariables.items():
      env[name] = stateVar.getValue()
    return env

  def _updateStateVarsFromEnvironment(self, env):
    """
    Updates state variable values who share names with the keys of "env".
    """
    for (name, value) in env.items():
      stateVar = self._stateVariables[name]
      stateVar.setValue(value)

  def _fromContext(self, ctx):
    """
    Builds RDIS model from the given context object.
    """
    for key in ctx.keys():
      if key == "domainInterfaces":
        self._loadDomainInterfaces(ctx[key])
      elif key == "interfaces":
        self._loadInterfaces(ctx[key])
      elif key == 'primitives':
        self._loadPrimitives(ctx[key])
      elif key == 'connections':
        self._loadConnections(ctx[key])
      elif key == 'domainOutputs':
        self._loadDomainOutputs(ctx[key])
      elif key == 'stateVariables':
        self._loadStateVar(ctx[key])
      elif key == 'author':
        self._author = ctx[key]
      elif key == 'name':
        self._name = ctx[key]
      else:
        sys.stderr.write("Unknown element type: {}\n".format(key))

  def _loadStateVar(self, varList):
    """
    Loads state variables from the context object representation.
    """
    for var in varList:
      apply(self.addStateVar,
          [var['name']], {
          'type': var['type'],
          'value': var['value']
          }
      )
  
  def _loadDomainOutputs(self, doList):
    """
    Loads domain outputs from the context object representation.
    """
    for do in doList:
      apply(self.addDomainOutput,
          [do['name']], {
          'returns': do['returns']
          }
      )

  def _loadDomainInterfaces(self, diList):
    """
    Loads domain interfaces from the context object representation.
    """
    for di in diList:
      apply(self.addDomainInterface,
          [di["name"]], {
          'parameters':di["parameters"],
          'localInterface':di["calls"]["name"],
          'interfaceArguments':di["calls"]["arguments"]
        }
      )

  def _loadInterfaces(self, interfaceList):
    """
    Loads local interfaces from the context object representation.
    """
    for interface in interfaceList:
      apply(self.addInterface,
        [interface['name']], {
          'type': interface['type'],
          'parameters': interface.get('parameters'),
          'triggers': interface.get('triggers')
        }
      )
      i = self._getInterface(interface['name'])

      for pc in interface['primitiveCalls']:
        i.addPrimitiveCall(
          pc['name'],
          pc['arguments'],
          pc['delay'],
          pc['priority']
        )

  def _loadPrimitives(self, primitiveList):
    """
    Loads primitives from the context object representation.
    """
    for p in primitiveList:
      apply(self.addPrimitive,
        [p['name']], {
          'connection': p['connection'],
          'parameters': p.get('parameters', []),
          'formatArgs': p.get('formatArgs', []),
          'postActions': p.get('postActions', []),
          'format': p.get('format'),
          'regex': p.get('regex'),
          'pack': p.get('pack'),
          'unpack': p.get('unpack')
        }
      )

  def _loadConnections(self, connections):
    """
    Loads connections from the context object representation.
    """
    self._loadSerialConnections(connections.get('spp'))
  
  def _loadSerialConnections(self, connectionList):
    """
    Loads serial connections from the context object representation.
    """
    if connectionList == None: return
    for c in connectionList:
      apply(self.addSerialConnection,
        [c['name']], {
          'baud': c['baud'],
          'singleThreading': c.get('singleThreading'),
        })
      conn = self.getConnection(c['name'])
      k = c.get('keepalive')
      t = c.get('terminate')
      s = c.get('startup')
      if k: apply(conn.setKeepalive, [], k)
      if t: apply(conn.setTerminate, [], t)
      if s: apply(conn.setStartup, [], s)

class StateVar:

  """
  A basic unit of memory for the robot model.

  Only Primitives can manipulate state variables and they generally reflect a
  value read from the sensor, or some sort of constant about the robot.
  """

  def __init__(self, name=None, value=None, type=None, parent=None):
    """
    Constructs a state variable.
    """
    if value == None:
      value = mapDefaultValue(type)
    self._name = name
    self._parent = parent

    self._setType(type)
    self.setValue(safeEval(value,dict()))

  def getValue(self):
    """
    Gets the value of the state variable.
    """
    return self._value

  def _getDefaultValue(self):
    """
    Gets the default value for this state variable.
    """
    return mapDefaultValue(self._type)

  def setValue(self,value):
    """
    Sets the value of the state variable.
    """
    if value == None or value == "":
      value = self._getDefaultValue()
      
    self._assertType(value)
    self._value = value

  def _assertType(self, value):
    """
    Asserts value is a valid type for this state variable.

    @raises TypeError if the assertion failed.
    """
    nameType = self._getPythonType()
    valType = safeType(value)
    if not isinstance(value, eval(nameType)):
      raise TypeError(
        "Attempt to set {} ({}) to value {} ({}).".format(self._name, nameType,
        repr(value), valType)
      )

  def _getPythonType(self):
    """
    Gets the equivalent Python type for this state variable.
    """
    return mapType(self._type)

  def _setType(self, newType):
    """
    Changes this StateVar's RDIS type.
    """
    mapType(newType) ## Asserts that it is a valid RDIS type.
    self._type = newType
    
class Primitive:

  def __init__(self, parent=None, pack=None, unpack=None, parameters=[],
      regex=None, format=None, name=None, connection=None, formatArgs=[],
      postActions=[]):
    """
    Constructs a Primitive.
    """
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
    """
    Calls a primitive with the provided positional arguments.
    """
    env = createEnvironment(self._parameters, arguments)

    ## Evaluate all the args we send out on the format string.
    values = [safeEval(k,env) for k in self._formatArgs]

    ## Write the information on the connection and read back.
    connection = self._getConnection()
    connection.write( self._doPack(values) )
    out = self._doUnpack( connection )

    ## Build environments for postActions and execute them.
    envs = self._buildPostActionEnv(env, out)
    safeExecs(self._postActions, envs[1])

    ## Delete local variables that we added.
    deleteAdditions(envs[0], envs[1])

    ## Updates stateVar from the global environment.
    self._parent._updateStateVarsFromEnvironment(envs[1])

  def parameterCount(self):
    """
    Returns the number of parameters this Primitive accepts.
    """
    return len(self._parameters)

  def _buildPostActionEnv(self, parameters, out):
    """
    Builds environment for post actions.
    """
    globalEnv = self._parent._buildStateVarEnvironment()
    globalCopy = dict(globalEnv)
    globalCopy.update(parameters)
    globalCopy["__out__"] = out
    return (globalEnv, globalCopy)

  def _getConnection(self):
    """
    Gets connection associated with this Primitive.
    """
    return self._parent.getConnection(self._connection)

  def _doPack(self, values):
    """
    Decides whether or not we need to ASCII-encode or byte-pack the values we
    are writing to the robot.
    """
    if self._format != None:
      return bytes(apply(self._format.format, values))
    else:
      tmp = [str(self._pack)]
      tmp.extend(values)
      return apply(struct.pack, tmp)

  def _doUnpack(self, connection):
    """
    Unpacks arguments read from the connection using regular expressions or
    struct.unpack().
    """
    if self._regex != None:
      return re.match(self._regex, str(connection.read())).groups()
    elif self._unpack != None:
      sz = struct.calcsize(str(self._unpack))
      byteSequence = connection.read(sz)
      return struct.unpack(str(self._unpack), byteSequence)
      

class Connection:

  """
  Represents the connection from the host application to the robot.
  """

  def __init__(self, name, parent):
    """
    Constructs a connection.
    """
## TODO: THREADING
    self._name = name
    self._parent = parent
    self._startup = None
    self._keepalive = None
    self._terminate = None
    self._initialized = False

  def startup(self):
    """
    Initializes the connection if it is unintialized.
    """
    if self._initialized == True: return
    self._initialized = True
    pass

  def tick(self):
    """
    Performs any periodic actions needed by this connection.
    """
    self.keepalive()

    ## TODO: Periodic interfaces.

  def keepalive(self):
    """
    Attempts to call the keepalive if it is past due.
    """
    ## TODO: obey keepalive frequency
    self._callKeepalive()

  def _callKeepalive(self):
    """
    Calls the keepalive interface.
    """
    self._callEventInterface(self._keepalive)

  def _callStartup(self):
    """
    Calls the startup interface.
    """
    self._callEventInterface(self._startup)

  def _callTerminate(self):
    """
    Calls the termination interface.
    """
    self._callEventInterface(self._terminate)

  def _callEventInterface(self, i):
    """
    Calls a generic eventful interface.
    """
    if i == None: return
    env = self._parent._buildStateVarEnvironment()
    args = safeEvalAll(i['arguments'], env)
    self._parent._callInterface(i['name'], args)

  def setStartup(self, name, arguments=[]):
    """
    Sets the startup interface.
    """
    self._startup = {
      'name': name,
      'arguments': arguments
      ## TODO: Where is the periodicity?
    }

  def setTerminate(self, name, arguments=[]):
    """
    Sets the terminate interface.
    """
    self._terminate = {
      'name': name,
      'arguments': arguments
    }

  def setKeepalive(self, name, interval, arguments=[]):
    """
    Sets the keepalive interface.
    """
    self._keepalive = {
      'interval': interval,
      'name': name,
      'arguments': arguments
    }


  def write(self, stuff):
    """
    Dummy method for writing to an abstract connection. Prints bytes to
    stdout.
    """
    print "--- WROTE ---"
    printBytes(stuff)

  def read(self, num):
    """
    Dummy method for reading bytes. Returns arbitrary bytes.
    """
    print "--- READ ---"
    byteSequence = bytes()
    for i in range(num):
      b = random.randint(0,20)
      b = chr(3) if b==0 else chr(0)
      byteSequence += b
    printBytes(byteSequence)
    return byteSequence

class SerialConnection(Connection):

  """
  Represents a connection over the serial port.
  """

  def __init__(self, baud=9600, name=None, parent=None, singleThreading=None):
    Connection.__init__(self, name, parent)
    """
    Constructs a serial connection.
    """
    self._baud = baud

  def startup(self, port='/dev/rfcomm0'):
    """
    Opens serial port and calls startup interface.
    """
    if self._initialized: return
    self._serial = serial.Serial(port=port, baudrate=self._baud)
    self._serial.open()
    self._initialized = True
    self._callStartup()

  def terminate(self):
    """
    Executes termination interface and closes connection.
    """
    self._callTerminate()
    self._serial.close()

  def write(self, byteSequence):
    """
    Writes a byte sequence to the serial port.
    """
    self._serial.write(byteSequence)
    print "--------- WROTE (serial) ----------"
    printBytes(byteSequence)

  def read(self, num=1):
    """
    Reads a byte sequence from the serial port.
    """
    byteSequence = self._serial.read(num)
    print "--------- READ (serial) ----------"
    printBytes(byteSequence)
    return byteSequence


class DomainInterface:

  """
  Represents a domain interface.

  A domain interface is supposed to be a standardized name and message format
  which can pass into the model. It is then normally tied to some local
  interface. Domain interfaces have no return values.
  """

  def __init__(self,
    parent = None,
    name=None,
    localInterface=None,
    interfaceArguments=[],
    parameters=[]):

    """
    Constructs a domain interface.

    A domain interface has some parameters (a set of names) which must be
    satisfied by the calling entity. These parameters are then mapped into
    arguments that the local interface will accept.
    """
    
    self._parent = parent
    self._name = name
    self._localInterface = localInterface
    self._interfaceArguments = interfaceArguments
    self._parameters = parameters

  def call(self, givenEnv):
    env = dict()
    try:
      for key in self._parameters:
        env[key] = givenEnv[key]
    except KeyError as e:
      sys.stderr.write("Missing argument for {}: {}\n".format(self._name,str(e)))
      return       

    values = safeEvalAll(self._interfaceArguments,env)
    self._parent._callInterface(self._localInterface, values)

class DomainOutput:

  def __init__(self,
      parent=None,
      name=None,
      returns=None):
    self._parent = parent
    self._name = name
    self._returns = returns


  def call(self):
    outMsg = dict(self._returns)
    stateVars = self._parent._buildStateVarEnvironment()

    for (key, val) in outMsg.items():
      outMsg[key] = safeEval(val, stateVars)

    self._parent._receiveMessage(self, outMsg)

  def getName(self):
    return self._name


class Interface:

  def __init__(self, parent=None, name=None, type="adhoc", parameters=[],
      triggers=None):
    self._parent = parent
    self._name = name
    self._type = type
    self._parameters = parameters if parameters != None else []
    self._triggers = triggers
    self._primitiveCalls = []

  def addPrimitiveCall(self, name, arguments, delay=0, priority=0):
    self._primitiveCalls.append({
      'name': name,
      'arguments': arguments,
      'delay': delay,
      'priority': priority
    })

  def call(self, arguments):
    env = createEnvironment(self._parameters, arguments)

    for primCall in sorted(self._primitiveCalls, key=lambda x: x['priority']):
      args = safeEvalAll(primCall['arguments'], env)
      self._parent._callPrimitive(primCall['name'], args)
      time.sleep(primCall['delay'] / 1000.)

    if self._triggers != None:
      self._parent._callDomainOutput(self._triggers)
