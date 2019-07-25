# mutatis

This python package is for parsing C header files. 
This package uses the Lexer and Parser python files generated using Antlr4. 
The grammar file for C language has been taken from [https://github.com/antlr/grammars-v4/blob/master/c/C.g4](https://github.com/antlr/grammars-v4/blob/master/c/C.g4).


## TODO:
1. Parse C header file.
2. Traverse the C file using visitor class file.
3. Generate a ctypes python file for the given C header file.
4. Add cmd line options to the package.
