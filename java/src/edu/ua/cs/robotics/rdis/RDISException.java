package edu.ua.cs.robotics.rdis;

/**
 * Wraps that possibly don't need to be dealt
 * with by client programmers.
 *
 */
public class RDISException extends Exception {

	/**
	 * Auto-generated GUID.
	 */
	private static final long serialVersionUID = 4073415693132640393L;
	
	private String mMessage;
	
	private Exception mCause;
	
	/**
	 * Constructs an RDISException with a simple message
	 * and no cause.
	 * @param msg message associated with exception
	 */
	public RDISException(String msg) {
		this(msg, null);
	}
	
	/**
	 * Constructs an RDISException with a message and cause.
	 * @param msg message for the exception
	 * @param cause cause of the exception (if any)
	 */
	public RDISException(String msg, Exception cause) {
		mMessage = msg;
		mCause = cause;
	}
	
	public String getMessage() {
		return mMessage;
	}
	
	@Override
	public Throwable getCause() {
		return mCause;
	}
}
