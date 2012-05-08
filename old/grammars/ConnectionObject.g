tree grammar ConnectionObject;

options {
  tokenVocab=RDIS;
  ASTLabelType=CommonTree;
  output=AST;
}

/**
  * CONNECTIONS
  * Defines the grammar for the connection to the robot.
  */
	
connections
	: ^(OBJECT (serialConnections)+) -> serialConnections?
	;
	
serialConnections
	: ^(SPP ^(LIST serialConnection+)) -> ^(SPP serialConnection)
	;
	
serialConnection
	: ^(OBJECT (namePair|connectionThreading|connectionSpeed|connectionOnStart|connectionOnTerminate|connectionOnKeepalive)+) ->
	  ^(SERIAL_CONNECTION namePair connectionThreading connectionSpeed connectionOnStart connectionOnTerminate connectionOnKeepalive)
	;
	
connectionThreading
	: ^(THREADING identifier)
	;
	
connectionSpeed
	: ^(SPEED number)
	;
	
connectionOnStart
	: ^(ON_START identifier)
	;
	
connectionOnTerminate
	: ^(ON_TERMINATE identifier)
	;
	
connectionOnKeepalive
	: ^(ON_KEEPALIVE connectionKeepaliveValue)
	;
	
connectionKeepaliveValue
	: ^(OBJECT (namePair|keepaliveInterval)+) -> ^(KEEPALIVE_OBJECT namePair keepaliveInterval)
	;
		
keepaliveInterval
	: ^(INTERVAL number)
	;
