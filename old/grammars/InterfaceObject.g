tree grammar InterfaceObject;

options {
  tokenVocab=RDIS;
  ASTLabelType=CommonTree;
  output=AST;
}


/**
  * INTERFACES
  * Defines the grammar to represent the exposed programming interfaces.
  */

interfaceArray
	: ^(LIST! interfaceObject+)
	;
	
// Matches an interface object.
interfaceObject
	: ^(OBJECT (genericSignature|interfaceFreqTypeStmt|interfacePrimitiveStmt)+)
	      -> ^(INTERFACE genericSignature interfaceFreqTypeStmt interfacePrimitiveStmt)
	;
	
// Matches an interface frequency type (e.g., "freq": "adhoc",)
interfaceFreqTypeStmt
	: ^(FREQ interfaceFreqType)
	;

// Valid frequency types. Add new frequency types here.
interfaceFreqType
	: ADHOC
	;

// Matches a primitive call description.
interfacePrimitiveStmt
	: ^(PRIMITIVE interfacePrimitiveObject)
	;
	
// This matches the primitive call object itself.
interfacePrimitiveObject
	: ^(OBJECT (namePair|argumentListStmt|returnListStmt)+)
        -> ^(PRIMITIVE_CALL namePair argumentListStmt returnListStmt?)
	;
	
returnListStmt
	: ^(RETURNS ^(LIST identifierValuePair+)) -> ^(RETURNS identifierValuePair+)
	;
	
identifierValuePair
	: ^(OBJECT (namePair|valueStmt)+) -> ^(PAIR namePair valueStmt)
	;
	
valueStmt
	: ^(VALUE expr)	
	;
	
argumentListStmt
	: ^(ARGUMENTS argumentList)
	;
	
argumentList
	: ^(LIST argument+) -> ^(ARGUMENT_LIST argument+)	
	;
	
argument
	: ^(OBJECT (namePair|valueStmt)+) -> ^(ARGUMENT namePair valueStmt)
	;
