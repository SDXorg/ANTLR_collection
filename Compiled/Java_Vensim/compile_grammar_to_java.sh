#!/bin/bash
export CLASSPATH=".:/usr/local/lib/antlr-4.5-complete.jar:$CLASSPATH"
antlr4='java -jar /usr/local/lib/antlr-4.5-complete.jar'
grun='java org.antlr.v4.runtime.misc.TestRig'
rm Model*.java Model*.class Model.tokens
#next line - use a subshell to switch directories, then come back here
(cd ../../Grammars/Vensim; $antlr4 -visitor -o ../../Compiled/Java_Vensim -listener Model.g4)
javac *.java