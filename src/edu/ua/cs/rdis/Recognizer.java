package edu.ua.cs.rdis;

import java.io.IOException;

import org.antlr.runtime.ANTLRFileStream;
import org.antlr.runtime.CharStream;
import org.antlr.runtime.CommonTokenStream;
import org.antlr.runtime.RecognitionException;

import edu.ua.cs.rdis.gen.RDISLexer;
import edu.ua.cs.rdis.gen.RDISParser;

public class Recognizer {
	private static void printUsage() {
		String name = Recognizer.class.getSimpleName();
		System.out.printf("Usage: java %s <file1> [<file2>..<fileN>]\n", name);
		System.out.println("Return codes:");
		System.out.println("\t-1\t:: Usage error");
		System.out.println("\t0..N\t:: Number of failures");
	}
	
	public static void main(String args[]) {
		if(args.length == 0) {
			printUsage();
			System.exit(-1);
		}
		
		int fails = 0;
		for(String file : args) {
			try {
				CharStream input = new ANTLRFileStream(file);
				RDISLexer lex = new RDISLexer(input);
				CommonTokenStream tokens = new CommonTokenStream(lex);
				RDISParser parser = new RDISParser(tokens);
				parser.rdis();
				System.out.printf("%s: PASS\n", file);
			} catch (RecognitionException e) {
				System.out.printf("%s: FAIL: %s\n", file, e.getMessage());
				fails++;
			} catch (IOException e) {
				System.err.printf("%s: I/O error: %s\n", file, e.getMessage());
				fails++;
			} catch (IllegalArgumentException e) {
				System.out.printf("%s: FAIL: %s\n", file, e.getMessage());
				fails++;
			}
			
			
		}
		System.out.println(fails);
		System.exit(fails);
	}
}
