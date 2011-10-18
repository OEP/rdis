tree grammar RDISValidator;

options {
	tokenVocab=RDIS;
	ASTLabelType=CommonTree;
	output=AST;
}

tokens {
	STATE_VECTOR;
	STATE_VAR;
}

@header {
package edu.ua.cs.rdis.gen;
}

rdis
	: ^(ROBOT ^(OBJECT (namePair|stateVector)+)) -> ^(ROBOT namePair stateVector)
	;
	
stateVector
	: ^(STATE ^(LIST stateVar+)) -> ^(STATE_VECTOR stateVar+)
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
	
object
	: ^(OBJECT definition*)
	;

list
	: ^(LIST value*)
	;

definition
	: ^(keyword value)
	;

keyword
	: NAME
	| INTERVAL
	| SPEED
	| TYPE
	| VALUE
	| ON_START
	| ON_TERMINATE
	| ON_KEEPALIVE
	| STATE
	| CONNECTIONS
	| SPP
	| INT
	| STRING
	| FLOAT
	| PRIMITIVES
	| SIGNATURE
	| WRITE_FORMAT
	| FORMAT
	| READ_FORMAT
	| REGEX
	| PRIMITIVE
	| PARAMETERS
	| INTERFACES
	| EXPRESSION
	| RETURNS
	;
	
primitiveValue
	: string
	| number
	;
	
value
	: primitiveValue
	| identifier
	| list
	| object
	| keyword
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