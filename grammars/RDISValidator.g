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
}

@header {
package edu.ua.cs.rdis.gen;
}

rdis
	: ^(ROBOT ^(OBJECT (namePair|stateVector)+)) -> ^(ROBOT namePair stateVector)
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
	: ^(OBJECT (stateVarType|namePair|stateVarValue)+) -> ^(STATE_VAR stateVarType namePair stateVarValue?)
	;
	
stateVarType
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