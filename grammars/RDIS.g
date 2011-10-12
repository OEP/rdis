grammar RDIS;

options {
	output=AST;
}

tokens {
	// Dummies
	ROBOT;
	STATE_VECTOR;
	DECLARE_STATEVAR;
	
	// JSON syntax bits
	OCURLY 	= '{' ;
	CCURLY 	= '}' ;
	OSQUARE = '[' ;
	CSQUARE = ']' ;
	COLON   = ':' ;
	COMMA   = ',' ;
	
	// Keywords
	STATE = '"state"' ;
	NAME = '"name"';
	TYPE = '"type"';
	VALUE = '"value"';
	
	// Data type labels
	STRING;
	NUMBER;
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
	:	OCURLY topLevelStatement (COMMA topLevelStatement)* CCURLY -> ^(ROBOT topLevelStatement+)
	;

topLevelStatement
	: nameStatement
	| stateVarsDeclaration
	;

stateVarsDeclaration
	: STATE COLON OSQUARE stateVar (COMMA stateVar)* CSQUARE
		-> ^(STATE_VECTOR stateVar+)
	;
	
stateVar
	: OCURLY stateVarStatement (COMMA stateVarStatement)* CCURLY
		-> ^(DECLARE_STATEVAR stateVarStatement+)
	;
	
stateVarStatement
	: nameStatement
	| TYPE COLON VarType -> ^(VarType)
	| VALUE COLON value -> ^(value)
	;

nameStatement
	: NAME COLON Identifier -> ^(Identifier)
	;

value
	: string
	| number
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
 
VarType
	: '"int"' | '"string"' | '"float"'
	;

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
