package edu.ua.cs.robotics.rdis;

import java.util.HashMap;

/**
 * RDIS model interpreter for Java.
 *
 */
public class RDIS {
	
	/** Callback interface for triggered Domain Outputs */
	private RDIS.Callback mCallback;
	
	/**
	 * RDIS cannot be instantiated directly. Use RDIS.load(String).
	 */
	private RDIS() {
	}
	
	/**
	 * Registers a callback to handle messages 
	 * @param callback
	 */
	public void setCallback(RDIS.Callback callback) {
		mCallback = callback;
	}
	
	/**
	 * Calls a Domain Interface for this model.
	 * @param name the name of the Domain Interface to call
	 * @param domainAdapter
	 */
	public void callDomainInterface(String name, HashMap<String,Object> domainAdapter) {
		// TODO
	}
	
	/**
	 * Called on startup.
	 * @param portName the port name to use for the connection, e.g., /dev/rfcomm0
	 */
	public void startup(String portName) {
		// TODO
	}
	
	/**
	 * Periodically called by client code. Triggers keepalive Interfaces, etc.
	 */
	public void tick() {
		// TODO
	}
	
	/**
	 * Called by client code to destruct the model. Triggers terminate Interfaces, etc.
	 */
	public void terminate() {
		// TODO
	}
	
	/**
	 * Loads an RDIS object from an RDIS description.
	 * @param rdisFile path to file containing the RDIS description
	 * @return the loaded RDIS model
	 */
	public static RDIS load(String rdisFile) {
		// TODO
		return new RDIS();
	}
	
	/**
	 * Interface the client must implement to handle messages coming from triggered
	 * Domain Outputs. 
	 */
	public static interface Callback {
		/**
		 * Called in client code when a Domain Output is triggered.
		 * @param name the name of triggered Domain Output
		 * @param contents the message produced by the Domain Output
		 */
		public void onMessageReceived(String name, HashMap<String,Object> contents);
	}
}
