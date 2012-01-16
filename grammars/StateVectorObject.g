tree grammar StateVectorObject;

options {
  tokenVocab=RDIS;
  ASTLabelType=CommonTree;
  output=AST;
}

tokens {
  STATE_VAR;
}


/**
  * STATE VECTOR
  * Defines the grammar for the variables which describe the robot state.
  */	

stateVector
	: ^(LIST! stateVar+)
	;
	
stateVar
	: ^(OBJECT (varType|namePair|stateVarValue)+) -> ^(STATE_VAR varType namePair stateVarValue?)
	;
	
// Don't use expressions for state vars.
stateVarValue
	: ^(VALUE primitiveValue)
	;
