# Vensim Grammar

The Vensim Modeling Language grammar in this folder is separated into two files:

- Model.g4
- Expr.g4

The Model grammar matches the "outer" part of a Vensim .mdl file, including equations and lookups. Model imports the Expr grammar, which matches the formula expressions on the right-hand side of equations. Expr was derived from the sample C grammar on the ANTLR website.

To build the lexer and parser in Java, give the command:
~~~
java -jar antlr-4.7-complete.jar -visitor -no-listener Model.g4
~~~

To build in JavaScript, give the command:
~~~
java -jar antlr-4.7-complete.jar -Dlanguage=JavaScript -visitor -no-listener Model.g4
~~~

The Vensim grammar has the following limitations.

- It relies on a preprocessor to join lines continued with the backslash character.
- Units and groups are stripped from the model. The grammar is not yet suitable for generating model documentation.
- Macros and tabbed arrays are unsupported. You can either rewrite the model or translate them manually.
