grammar RDIS;

options {
	output=AST;
}

tokens {
	// Dummies
	ROBOT;
	STATE_VECTOR;
	CONNECTIONS;
	CONNECTION_LIST;
	DECLARE_CONNECTION;
	DECLARE_STATEVAR;
	
	// JSON syntax bits
	OCURLY 	= '{' ;
	CCURLY 	= '}' ;
	OSQUARE = '[' ;
	CSQUARE = ']' ;
	COLON   = ':' ;
	COMMA   = ',' ;
	
	// Universal keywords
	NAME = '"name"';
	
	// State vector keywords
	STATE = '"state"' ;
	TYPE = '"type"';
	VALUE = '"value"';
	
	// Connection keywords.
	CONNECTIONS = '"connections"';
	SPP = '"spp"';
	USB = '"usb"';
	SPEED = '"speed"';
	ON_START = '"onStart"';
	ON_TERMINATE = '"onTerminate"';
	ON_KEEPALIVE = '"onKeepalive"';
	INTERVAL = '"interval"';
	
	// Primitive keywords
	PRIMITIVES = '"primitives"';
	SIGNATURE = '"signature"';
	PARAMETERS = '"parameters"';
	WRITE_FORMAT = '"writeFormat"';
	FORMAT = '"format"';
	EXPRESSION = '"expression"';
	READ_FORMAT = '"readFormat"';
	REGEX = '"regex"';
	
	// Interface keywords.
	INTERFACES = '"interfaces"';
	PRIMITIVE = '"primitive"';
	RETURNS = '"returns"';
	
	// TODO: "Domain" modeling.
	
	// Data type labels
	FLOAT = '"float"';
	INT = '"int"';		// Not used to label matched tokens. (That's what NUMBER is for).
	STRING;			// This could be confusing. Serves as a type label for matched strings and also a keyword.
	NUMBER;
	IDENTIFIER;
	OBJECT;
	LIST;
}

@lexer::header {
package edu.ua.cs.rdis.gen;
}

@header {
package edu.ua.cs.rdis.gen;

import java.util.regex.Pattern;
}

// TODO: ANTLR balks at this now, so I commented it out (PMK)
//@lexer::members {
//  @Override
//  public void reportError(RecognitionException e)  {
//    throw new IllegalArgumentException(e);
//  }
//}

//@members {
//  @Override
//  public void reportError(RecognitionException e) {
//    throw new IllegalArgumentException(e);
//  }
//}

/*--------------------------------------------------
 * PARSER RULES
 *--------------------------------------------------*/
 
rdis
	: object -> ^(ROBOT object)
	;
	
object
	: OCURLY (definition (COMMA definition)*)? CCURLY -> ^(OBJECT definition*)
	;

list
	: OSQUARE (value (COMMA value)*)? CSQUARE -> ^(LIST value*)
	;

definition
	: keyword COLON value -> ^(keyword value)
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
	: Identifier -> ^(IDENTIFIER Identifier)
	;

string
	: String -> ^(STRING String)
	;
	
number
	: n=Number {Pattern.matches("(0|(-?[1-9]\\d*))(\\.\\d+)?", n.getText())}? Exponent?
	  -> ^(NUMBER Number Exponent?)
	;

/*--------------------------------------------------
 * LEXER RULES
 *--------------------------------------------------*/

Identifier
	: '"' Alpha Alphanumeric* '"'
	;
 
String 	:
	'"' StringChar* '"'
	;
	
Number
	: '-'? DecimalDigit+ ( '.' DecimalDigit+)?
	;
	
Exponent
	: ('e'|'E') '-'? DecimalDigit+
	;

fragment Alphanumeric
	: Alpha | DecimalDigit
	;

fragment Alpha
	: 'a'..'z' | 'A'..'Z'
	;
	
fragment DecimalDigit
	: '0'..'9'
	;

fragment StringChar
	: ( EscapeSequence | ~('\u0000'..'\u001f' | '\\' | '\"' ) )
	;
	
fragment HexDigit
	: '0'..'9' | 'A'..'F' | 'a'..'f'
	;
	
fragment EscapeSequence
    	:   '\\' (UnicodeEscape |'b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
    	;

fragment UnicodeEscape
	: 'u' HexDigit HexDigit HexDigit HexDigit
	;
 
Whitespace 
 	:	( '\t' | ' ' | '\r' | '\n' | '\u000C' )+ { $channel = HIDDEN; } ;
