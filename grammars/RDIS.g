grammar RDIS;

tokens {
	ROBOT;
	OCURLY 	= '{' ;
	CCURLY 	= '}' ;
	COLON   = ':' ;
	COMMA   = ',' ;
	PRIMITIVES = '"primitive"' ;
	NAME = '"name"';
}

@lexer::header {
package edu.ua.cs.rdis.gen;
}

@header {
package edu.ua.cs.rdis.gen;
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
	:	OCURLY topLevelStatement (COMMA topLevelStatement)* CCURLY
	;

topLevelStatement
	: nameStatement
	;

nameStatement
	: NAME COLON Identifier
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
