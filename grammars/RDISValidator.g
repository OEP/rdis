tree grammar RDISValidator;

// This grammar takes a syntax-bound tree from RDIS.g and creates
// a syntax-free AST for use in later steps.
options {
	tokenVocab=RDIS;
	ASTLabelType=CommonTree;
	output=AST;
}

import StateVectorObject;

// These are helper tokens to mark objects as validated objects.
tokens {
	SERIAL_CONNECTION;
	KEEPALIVE_OBJECT;
	FORMAL_PARAMETER;
	EXPR_LIST;
	ARGUMENT;
	ARGUMENT_LIST;
	EXPR;
	INTERFACE;
	PRIMITIVE_CALL;
	SINGLE_THREAD_OBJECT;
	PAIR;
}


@header {
package edu.ua.cs.rdis.gen;
}


// START RULE
rdis
	: ^(ROBOT ^(OBJECT (namePair|threadingObject|stateVectorDecl|connections|primitives|interfaces)+))
	-> ^(ROBOT namePair threadingObject stateVectorDecl connections primitives interfaces)
	;

// The declaration for a State Vector (actual object definition in delegate grammar)
stateVectorDecl
  : ^(STATE stateVector)
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
	
// Matches an interface object.
interfaceObject
	: ^(OBJECT (genericSignature|interfaceFreqTypeStmt|interfacePrimitiveStmt)+)
	      -> ^(INTERFACE genericSignature interfaceFreqTypeStmt interfacePrimitiveStmt)
	;
	
// Matches an interface frequency type (e.g., "freq": "adhoc",)
interfaceFreqTypeStmt
	: ^(FREQ interfaceFreqType)
	;

// Valid frequency types. Add new frequency types here.
interfaceFreqType
	: ADHOC
	;

// Matches a primitive call description.
interfacePrimitiveStmt
	: ^(PRIMITIVE interfacePrimitiveObject)
	;
	
// This matches the primitive call object itself.
interfacePrimitiveObject
	: ^(OBJECT (namePair|argumentListStmt|returnListStmt)+)
        -> ^(PRIMITIVE_CALL namePair argumentListStmt returnListStmt?)
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
	: ^(ARGUMENTS argumentList)
	;
	
argumentList
	: ^(LIST argument+) -> ^(ARGUMENT_LIST argument+)	
	;
	
argument
	: ^(OBJECT (namePair|valueStmt)+) -> ^(ARGUMENT namePair valueStmt)
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
	: ^(OBJECT (varType|namePair)+) -> ^(FORMAL_PARAMETER varType namePair)
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
	
	
varType
	: ^(TYPE (INT|FLOAT|STRING))
	;

namePair
	: ^(NAME identifier)
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
