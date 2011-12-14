grammar RDIS;

options {
	output=AST;
}

// This section contains keywords for our language.
tokens {
	// Dummies
	ROBOT;
	
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
	
	// Threading keywords
	THREADING = '"threading"';
	SINGLE = '"single"';
	FREQ = '"freq"';
	
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
	ARGUMENTS = '"arguments"';
	RETURNS = '"returns"';
	ADHOC = '"adhoc"';
	
	// TODO: Domain modeling keywords.
	
	// Data type labels
	FLOAT = '"float"';
	INT = '"int"';		// Not used to label matched tokens. (That's what NUMBER is for).
	STRING = '"string"';	// This could be confusing. Serves as a type label for matched strings and also a keyword.
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
 
// START RULE: The root object.
rdis
	: object -> ^(ROBOT object)
	;
	
// Basic JSON syntax for an object.
object
	: OCURLY (definition (COMMA definition)*)? CCURLY -> ^(OBJECT definition*)
	;

// Matches JSON arrays.
list
	: OSQUARE (value (COMMA value)*)? CSQUARE -> ^(LIST value*)
	;


// This is a standard member/value pair for JSON.
definition
	: keyword COLON value -> ^(keyword value)
	;

// This matches any known keyword.
// Note: New keywords must be added to this rule.
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
	| RETURNS	// TODO: Do we keep this?
	| THREADING
	| SINGLE
	| FREQ
	| ADHOC
	| ARGUMENTS
	;
	
// Valid values are any primitive value type, plus lists, objects, ID's
// and keywords.
value
	: string
	| number
	| identifier
	| list
	| object
	| keyword
	;

// Matches an identifier token.
identifier
	: Identifier -> ^(IDENTIFIER Identifier)
	;

// Matches a string token.
string
	: String -> ^(STRING String)
	;
	
// Matches a JSON number.
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
