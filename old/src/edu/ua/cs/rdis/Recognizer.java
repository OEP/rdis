package edu.ua.cs.rdis;

import java.io.IOException;
import java.util.List;

import org.antlr.runtime.ANTLRFileStream;
import org.antlr.runtime.CharStream;
import org.antlr.runtime.CommonTokenStream;
import org.antlr.runtime.RecognitionException;
import org.antlr.runtime.Token;

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
	
	private static void printTokens(CommonTokenStream tokens) {
		System.out.print("[");
		Token start = tokens.LT(1);
		String fmt = "%s %d";
		
		if(start.getType() >= 0) {
			System.out.printf(fmt, start.getText(), start.getType());
			tokens.consume();
		}
		
		for(Token tk = tokens.LT(1); tk.getType() >= 0; tokens.consume(), tk = tokens.LT(1)) {
			System.out.printf(", " + fmt, tk.getText(), tk.getType());
		}
		System.out.println("]");
		tokens.reset();
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
				
				printTokens(tokens);
				
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
