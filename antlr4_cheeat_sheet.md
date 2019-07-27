## To generate visitor from `g4` grammar file:

Step1: Download antlr4 complete jar from [https://www.antlr.org/download/antlr-4.7.2-complete.jar](https://www.antlr.org/download/antlr-4.7.2-complete.jar).

Step2: Fire the following command from terminal:


`java -cp "<PATH_TO_ANTLR_COMPLETE_JAR>" org.antlr.v4.Tool -Dlanguage=Python3 -visitor <PATH_TO_g4_FILE>`


The above steps should create python Lexer, Parser and Visitor classes for the grammar written in g4 file.


For further reading:

[Antlr: Straight from horses mouth](https://www.antlr.org/)

[Antlr4 mega tutorial](https://tomassetti.me/antlr-mega-tutorial/)
