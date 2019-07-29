# remove this file after development is over.
# This file is for running scripts to ensure devlopment is going in the right direction.

import sys
import os

from antlr4 import *
from mutandis.grammar.CLexer import CLexer
from mutandis.grammar.CParser import CParser
from mutandis.grammar.CVisitor import CVisitor
from mutandis.grammar.CListener import CListener

def main(header_path):
    input_stream = FileStream(header_path)
    lex = CLexer(input=input_stream)
    token_stream = CommonTokenStream(lex)
    # Parse all tokens until EOF
    # token_stream.fill()

    # for token in token_stream.tokens:
    #     print(token.text)
    parser = CParser(token_stream)
    tree = parser.compilationUnit()
    print(tree.getText())


if __name__ == "__main__":
    header_file_path = os.path.join(os.path.dirname(__file__),"test.h")
    main(header_file_path)