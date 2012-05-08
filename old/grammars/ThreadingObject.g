tree grammar ThreadingObject;

options {
  tokenVocab=RDIS;
  ASTLabelType=CommonTree;
  output=AST;
}

tokens {
	SINGLE_THREAD_OBJECT;
}

// Main threading object. Contains "single" member, etc...	
threadingObject
	: ^(OBJECT (singleThreadingList)*) -> singleThreadingList?
	;
	
// Matches a single threading list
singleThreadingList
	: ^(SINGLE ^(LIST singleThreadingObject+)) -> ^(SINGLE singleThreadingObject+)
	;
	
// Matches a single threading object
singleThreadingObject
	: ^(OBJECT (namePair|frequency)+) -> ^(SINGLE_THREAD_OBJECT namePair frequency)
	;
	
// Matches '"freq": <number>'	
frequency
	: ^(FREQ number)
	;
