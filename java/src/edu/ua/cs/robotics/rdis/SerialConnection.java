package edu.ua.cs.robotics.rdis;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import gnu.io.CommPort;
import gnu.io.CommPortIdentifier;
import gnu.io.NoSuchPortException;
import gnu.io.PortInUseException;
import gnu.io.SerialPort;
import gnu.io.UnsupportedCommOperationException;

public class SerialConnection extends Connection {
	
	private SerialPort mPort;
	
	private int mBaud;

	@Override
	public void startup(String portName) throws RDISException {
		try {
			CommPortIdentifier portIdentifier = CommPortIdentifier.getPortIdentifier(portName);
			CommPort commPort = portIdentifier.open("RDIS", 2000);
			mPort = (SerialPort) commPort;
			mPort.setSerialPortParams(mBaud, SerialPort.DATABITS_8, SerialPort.STOPBITS_1, SerialPort.PARITY_NONE);
		}
		catch (NoSuchPortException e) {
			throw new RDISException(String.format("No such port: %s", portName), e);
		} catch (PortInUseException e) {
			throw new RDISException(String.format("Port in use: %s", portName), e);
		} catch (UnsupportedCommOperationException e) {
			throw new RDISException("Invalid parameters set.", e);
		}
	}
	
	@Override
	public void write(byte stuff[]) throws IOException {
		OutputStream out = mPort.getOutputStream();
		out.write(stuff);
	}
	
	@Override
	public byte[] read(int num) throws IOException {
		InputStream in = mPort.getInputStream();
		byte buffer[] = new byte[num];
		int bytesRead = in.read(buffer);
		return buffer;
	}

	@Override
	public void terminate() {
		if(mPort != null) {
			mPort.close();
		}
	}

}
