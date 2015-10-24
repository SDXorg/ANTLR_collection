#!/bin/bash
antlr4='java -jar /usr/local/lib/antlr-4.5-complete.jar'
grun='java org.antlr.v4.runtime.misc.TestRig'
rm Model*.py Model*.pyc Model.tokens
cd ../../Grammars/Vensim
$antlr4 -Dlanguage=Python2 -visitor -o ../../Compiled/Python-Vensim -no-listener Model.g4