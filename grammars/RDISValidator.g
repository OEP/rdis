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
}

@header {
package edu.ua.cs.rdis.gen;
}

rdis
	: ^(ROBOT ^(OBJECT (namePair|stateVector|connections|primitives)+)) -> ^(ROBOT namePair stateVector connections primitives)
	;

primitives
	: ^(PRIMITIVES ^(LIST primitive+)) -> ^(PRIMITIVES primitive+)
	;
	
primitive
	: ^(OBJECT (primitiveSignature)+) -> ^(PRIMITIVE primitiveSignature)
	;
	
primitiveSignature
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
	
connections
	: ^(CONNECTIONS ^(OBJECT (serialConnections)+)) -> ^(CONNECTIONS serialConnections?)
	;
	
serialConnections
	: ^(SPP ^(LIST serialConnection+)) -> ^(SPP serialConnection)
	;
	
serialConnection
	: ^(OBJECT (namePair|connectionSpeed|connectionOnStart|connectionOnTerminate|connectionOnKeepalive)+) ->
		^(SERIAL_CONNECTION namePair connectionSpeed connectionOnStart connectionOnTerminate connectionOnKeepalive)
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