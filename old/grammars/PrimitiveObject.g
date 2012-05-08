tree grammar PrimitiveObject;

options {
  tokenVocab=RDIS;
  ASTLabelType=CommonTree;
  output=AST;
}


/**
  * PRIMITIVES
  * Defines the grammar for the most basic functions of the robot.
  */
	
primitives
	: ^(LIST! primitive+)
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
