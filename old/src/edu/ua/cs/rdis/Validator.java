package edu.ua.cs.rdis;

import org.antlr.runtime.ANTLRFileStream;
import org.antlr.runtime.ANTLRInputStream;
import org.antlr.runtime.CharStream;
import org.antlr.runtime.CommonTokenStream;
import org.antlr.runtime.tree.CommonTree;
import org.antlr.runtime.tree.CommonTreeNodeStream;

import edu.ua.cs.rdis.gen.RDISLexer;
import edu.ua.cs.rdis.gen.RDISParser;
import edu.ua.cs.rdis.gen.RDISValidator;

public class Validator
{
	public static void main(String[] args) throws Exception {
		if(args.length == 0) {
			System.out.println("Usage: java Validator <file>");
			System.exit(1);
		}

		CommonTokenStream tokens = new CommonTokenStream();
		{
			String file = args[0];
			CharStream input = new ANTLRFileStream(file);
			RDISLexer lexer = new RDISLexer(input);
			tokens.setTokenSource(lexer);
		}

		CommonTreeNodeStream nodes;
		{
			RDISParser parser = new RDISParser(tokens);
			RDISParser.rdis_return example = parser.rdis();

			CommonTree tree = (CommonTree)example.getTree();
			nodes = new CommonTreeNodeStream(tree);
		}

		{
			RDISValidator walker = new RDISValidator(nodes);
			RDISValidator.rdis_return example = walker.rdis();
			System.out.println(example.toString());
		}
		System.exit(0);

	}
}