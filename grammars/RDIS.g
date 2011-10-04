grammar RDIS;

tokens {
	OCURLY 	= '{' ;
	CCURLY 	= '}' ;
	COLON   = ':' ;
	COMMA   = ',' ;
}

@lexer::header {
package edu.ua.cs.rdis.gen;
}

@header {
package edu.ua.cs.rdis.gen;
}

/** Propogate lexer errors up as IllegalArgumentExceptions */
@lexer::members {
  @Override
  public void reportError(RecognitionException e)  {
    throw new IllegalArgumentException(e);
  }
}

/** Propogate parser errors up as IllegalArgumentExceptions */
@members {
  @Override
  public void reportError(RecognitionException e) {
    throw new IllegalArgumentException(e);
  }
}

/*--------------------------------------------------
 * PARSER RULES
 *--------------------------------------------------*/
 
rdis	:	OCURLY CCURLY ;

/*--------------------------------------------------
 * LEXER RULES
 *--------------------------------------------------*/
 
String 	:
	'"' ( EscapeSequence | ~('\u0000'..'\u001f' | '\\' | '\"' ) )* '"'
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