tree grammar RDISValidator;

options {
	tokenVocab=RDIS;
	ASTLabelType=CommonTree;
	output=AST;
}

@header {
package edu.ua.cs.rdis.gen;
}

rdis
	: ^(ROBOT object)
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
	
value
	: string
	| number
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