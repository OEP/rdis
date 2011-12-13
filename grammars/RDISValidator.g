tree grammar RDISValidator;

options {
	tokenVocab=RDIS;
	ASTLabelType=CommonTree;
	output=AST;
}

tokens {
	STATE_VAR;
	SERIAL_CONNECTION;
	KEEPALIVE_OBJECT;
	FORMAL_PARAMETER;
	EXPR_LIST;
	EXPR;
	INTERFACE;
	PRIMITIVE_CALL;
	SINGLE_THREAD_OBJECT;
	PAIR;
}

@header {
package edu.ua.cs.rdis.gen;
}

rdis
	: ^(ROBOT ^(OBJECT (namePair|threadingObject|stateVector|connections|primitives)+))
	-> ^(ROBOT namePair threadingObject stateVector connections primitives)
	;
	
// Main threading object. Contains "single" member, etc...	
threadingObject
	: ^(THREADING ^(OBJECT (singleThreadingList)+)) -> ^(THREADING singleThreadingList?)
	;
	
// Matches a single threading list
singleThreadingList
	: ^(SINGLE ^(LIST singleThreadingObject+)) -> ^(SINGLE singleThreadingObject+)
	;
	
// Matches a single threading object
singleThreadingObject
	: ^(OBJECT (namePair|frequency)+) -> ^(SINGLE_THREAD_OBJECT namePair frequency)
	;
	
// Matches '"freq": <number>'	
frequency
	: ^(FREQ number)
	;
/**
  * INTERFACES
  * Defines the grammar to represent the exposed programming interfaces.
  */

interfaces
	: ^(INTERFACES ^(LIST interfaceObject+)) -> ^(INTERFACES interfaceObject+)
	;
	
interfaceObject
	: ^(OBJECT (genericSignature|interfaceType|interfacePrimitiveStmt))
	      -> ^(INTERFACE genericSignature interfaceType interfacePrimitiveStmt)
	;
	

interfaceTypeStmt
	: ^(TYPE interfaceType)
	;
	
interfaceType
	: ADHOC
	;
	
interfacePrimitiveStmt
	: ^(PRIMITIVE interfacePrimitiveObject)
	;
	
interfacePrimitiveObject
	: ^(OBJECT (namePair|argumentListStmt|returnListStmt)+) -> ^(PRIMITIVE_CALL namePair argumentListStmt returnListStmt)
	;
	
returnListStmt
	: ^(RETURNS ^(LIST identifierValuePair+)) -> ^(RETURNS identifierValuePair+)
	;
	
identifierValuePair
	: ^(OBJECT (namePair|valueStmt)+) -> ^(PAIR namePair valueStmt)
	;
	
valueStmt
	: ^(VALUE expr)	
	;
	
argumentListStmt
	: ^(ARGUMENTS ^(LIST exprList)) ->
	;
	
exprList
	: ^(LIST expr*) -> ^(EXPR_LIST expr*)
	;

/**
  * PRIMITIVES
  * Defines the grammar for the most basic functions of the robot.
  */
	
primitives
	: ^(PRIMITIVES ^(LIST primitive+)) -> ^(PRIMITIVES primitive+)
	;
	
primitive
	: ^(OBJECT (genericSignature|writeFormat|readFormat)+) -> ^(PRIMITIVE genericSignature writeFormat readFormat)
	;
	
readFormat
	: ^(READ_FORMAT ^(OBJECT (regex|exprStmt)+)) -> ^(READ_FORMAT regex exprStmt)
	;
	
regex 	
	: ^(REGEX string)
	;
	
exprStmt
	: ^(EXPRESSION expr)
	;
		
	
writeFormat
	: ^(WRITE_FORMAT ^(OBJECT (formatString|parameterList)+)) -> ^(WRITE_FORMAT formatString parameterList)
	;
	
formatString
	: ^(FORMAT string)
	;
	
parameterList
	: ^(PARAMETERS ^(LIST expr+)) -> ^(PARAMETERS expr+)
	;
	
expr
	: primitiveValue -> ^(EXPR primitiveValue)
	;
	
genericSignature
	: ^(SIGNATURE ^(OBJECT (namePair|formalParameterList)+)) -> ^(SIGNATURE namePair formalParameterList)
	;
	
formalParameterList
	: ^(PARAMETERS ^(LIST formalParameter+)) -> ^(PARAMETERS formalParameter+)
	;
	
formalParameter
	: ^(OBJECT (varType|formalParameterValue)+) -> ^(FORMAL_PARAMETER varType formalParameterValue)
	;
	
formalParameterValue
	: ^(VALUE identifier)
	;
	
	
/**
  * CONNECTIONS
  * Defines the grammar for the connection to the robot.
  */
	
connections
	: ^(CONNECTIONS ^(OBJECT (serialConnections)+)) -> ^(CONNECTIONS serialConnections?)
	;
	
serialConnections
	: ^(SPP ^(LIST serialConnection+)) -> ^(SPP serialConnection)
	;
	
serialConnection
	: ^(OBJECT (namePair|connectionThreading|connectionSpeed|connectionOnStart|connectionOnTerminate|connectionOnKeepalive)+) ->
	  ^(SERIAL_CONNECTION namePair connectionThreading connectionSpeed connectionOnStart connectionOnTerminate connectionOnKeepalive)
	;
	
connectionThreading
	: ^(THREADING identifier)
	;
	
connectionSpeed
	: ^(SPEED number)
	;
	
connectionOnStart
	: ^(ON_START identifier)
	;
	
connectionOnTerminate
	: ^(ON_TERMINATE identifier)
	;
	
connectionOnKeepalive
	: ^(ON_KEEPALIVE connectionKeepaliveValue)
	;
	
connectionKeepaliveValue
	: ^(OBJECT (namePair|keepaliveInterval)+) -> ^(KEEPALIVE_OBJECT namePair keepaliveInterval)
	;
		
keepaliveInterval
	: ^(INTERVAL number)
	;
	
/**
  * STATE VECTOR
  * Defines the grammar for the variables which describe the robot state.
  */	

stateVector
	: ^(STATE ^(LIST stateVar+)) -> ^(STATE stateVar+)
	;
	
stateVar
	: ^(OBJECT (varType|namePair|stateVarValue)+) -> ^(STATE_VAR varType namePair stateVarValue?)
	;
	
varType
	: ^(TYPE (INT|FLOAT|STRING))
	;

namePair
	: ^(NAME identifier)
	;
	
stateVarValue
	: ^(VALUE primitiveValue)
	;
	

primitiveValue
	: string
	| number
	;

identifier
	: ^(IDENTIFIER Identifier)
	;

string
	: ^(STRING String)
	;
	
number
	: ^(NUMBER Number Exponent?)
	;