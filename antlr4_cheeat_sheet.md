## To generate visitor from `g4` grammar file:

Download antlr4 complete jar from [https://www.antlr.org/download/antlr-4.7.2-complete.jar](https://www.antlr.org/download/antlr-4.7.2-complete.jar).

Fire the following command from terminal:

java -cp "<PATH_TO_antlr-4.7.2-complete.jar>" org.antlr.v4.Tool -Dlanguage=Python3 -visitor <Path_to_g4_file>


The above steps should create python Lexer, Parser and Visitor classes for the grammar written in g4 file.


For further reading:
[https://www.antlr.org/](https://www.antlr.org/)
[https://tomassetti.me/antlr-mega-tutorial/](https://tomassetti.me/antlr-mega-tutorial/)
