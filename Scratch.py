# remove this file after development is over.
# This file is for running scripts to ensure devlopment is going in the right direction.

import sys
from antlr4 import *
from ctyper.grammar.CLexer import CLexer
from ctyper.grammar.CParser import CParser

def main(argv):
    input_stream = FileStream(argv[1])
    lex = CLexer(input=input_stream)
    token_stream = CommonTokenStream(lex)
    # Parse all tokens until EOF
    token_stream.fill()

    for token in token_stream.tokens:
        print(token.text)

if __name__ == "__main__":
    main(sys.argv)