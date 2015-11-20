import glob
import os.path
import traceback
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Compiled.Python_Vensim.ModelParser import ModelParser
from Compiled.Python_Vensim.ModelLexer import ModelLexer
import antlr4



test_dir = 'test-models/'

testfiles = glob.glob(test_dir+'*/*/*.mdl')


for modelfile in testfiles:
    print modelfile
    with open(modelfile, 'r') as file:
            text = file.read()

    text = text.split('\\\\\---///')[0] #drop layout information
    text = text.replace('\\\n\t\t' ,'') #merge lines split with \
    #print text

    input = antlr4.InputStream(text)
    lexer = ModelLexer()
    stream = antlr4.CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.model()
    break


