import sys
import argparse

from antlr4 import *

from compiler.ZenithGrammarListener import ZenithGrammarListener
from compiler.ZenithGrammarLexer import ZenithGrammarLexer
from compiler.ZenithGrammarParser import ZenithGrammarParser

from Runtime import Runtime

from antlr4 import ParseTreeWalker


def export_parse_tree_to_dot(parser, tree, output_file):
    def traverse(node, node_id):
        if isinstance(node, TerminalNode):
            # Terminal nodes do not have children
            return f"{node_id} [label=\"{node}\"];\n"

        node_label = parser.ruleNames[node.getRuleIndex()]
        dot = f"{node_id} [label=\"{node_label}\"];\n"

        for i, child in enumerate(node.children or []):
            child_id = f"{node_id}_{i}"
            dot += f"{node_id} -> {child_id};\n"
            dot += traverse(child, child_id)

        return dot

    dot_content = "digraph parse_tree {\n"
    dot_content += traverse(tree, "0")
    dot_content += "}\n"

    with open(output_file, "w") as f:
        f.write(dot_content)


def main():
    # Parse input

    parser = argparse.ArgumentParser(description="Process a Zenith file.")
    parser.add_argument('file_path', type=str, help="The path to the Zenith file to process.")
    args = parser.parse_args()

    # Use the file path from the command line arguments
    file_path = args.file_path

    with open(file_path, 'r') as file:
        # Create a CharStream from the file
        lexinalCode = InputStream(file.read())

        # Create lexer and parser objects
        lexer = ZenithGrammarLexer(lexinalCode)
        tokens = CommonTokenStream(lexer)
        parser = ZenithGrammarParser(tokens)

        # Generate parser tree from lexinal code
        tree = parser.program()

        # Export parse tree as DOT file
        output_file = "../parse_tree.dot"
        export_parse_tree_to_dot(parser, tree, output_file)

        print("Parse tree DOT file generated successfully:", output_file)

        listener = ZenithGrammarListener()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        # print(tree)

        intermediate_code = listener.get_output()
        print("Compile time: No of lines in intermediate code -", len(intermediate_code.split("\n")))
        print("Intermediate code:", intermediate_code)
        if len(intermediate_code) >= 1:
            with open(file_path.replace("zth", "izth"), "w", encoding="utf-8") as f:
                for line in intermediate_code:
                    f.write(line + "\n")

        runtime = Runtime.Runtime()

        # Execute the intermediate code
        runtime.execute(intermediate_code)

        # Print the value of variables after execution (optional)
        print("Variable values after execution:", runtime.variables)


if __name__ == "__main__":
    main()
