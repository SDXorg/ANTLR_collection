import glob
import os.path
import traceback
import sys

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Compiled.Python_Vensim import ModelParser
from Compiled.Python_Vensim import ModelLexer

#from Compiled.Python_Vensim.ModelParser import ModelParser
#from Compiled.Python_Vensim.ModelLexer import ModelLexer
import antlr4



test_dir = 'Dev Tools/test-models/tests/'
testfiles = glob.glob(test_dir+'*/*.mdl')


for modelfile in testfiles[:]:
    print modelfile
    input = antlr4.FileStream(modelfile)
    lexer = ModelLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = ModelParser(stream)
    tree = parser.model()


