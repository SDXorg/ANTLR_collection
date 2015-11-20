#!/bin/bash
antlr4='java -jar /usr/local/lib/antlr-4.5-complete.jar'
grun='java org.antlr.v4.runtime.misc.TestRig'
rm Model*.java Model*.class Model.tokens
cd ../../Grammars/Vensim
$antlr4 -visitor -o ../../Compiled/Java_Vensim -listener Model.g4