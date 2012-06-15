package edu.ua.cs.robotics.rdis;

public class Connection {

	public void write(byte stuff[]){
		
		System.out.print( stuff );
		
	}
	
	public byte[] read(int num){
		
		return new byte[ num ];
		
	}
	
}
