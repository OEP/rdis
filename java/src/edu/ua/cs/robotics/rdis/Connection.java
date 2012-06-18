package edu.ua.cs.robotics.rdis;

import java.io.IOException;

public abstract class Connection {
	
	/**
	 * Handles tasks which must be completed when the Connection is
	 * first initialized. This means intializing the port and calling
	 * startup Interfaces.
	 * @param portName name of port to open (e.g., /dev/rfcomm1, COM1, etc...)
	 */
	public abstract void startup(String portName)
		throws RDISException;
	
	/**
	 * Handles tasks which must be completed when the Connection is
	 * terminated. This means closing the port and calling terminating
	 * Interfaces.
	 */
	public abstract void terminate();

	/**
	 * Prints bytes to stdout.
	 * @param stuff
	 */
	public void write(byte stuff[]) throws IOException {
		System.out.print( stuff );
	}
	
	/**
	 * Returns a byte array of size num of all zeroes.
	 * @param num number of bytes to read
	 * @return a byte array of size num
	 */
	public byte[] read(int num) throws IOException {
		return new byte[ num ];
	}
	
}
