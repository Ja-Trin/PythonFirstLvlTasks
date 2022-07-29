from ResourceUtil import ResourceUtil as R
from ReaderUtil import ReaderUtil as Reader
import random

class TxtUtil:

    def rewriter(pathToFile, numberOfLines):

        config = Reader.read_json(R.resource)
        
        fileName = config['fileName']
        extention = config['extention']

        headersLines = config['headersLines']
        postfix = config['postfix']

        origFile = f'{pathToFile}{fileName}{extention}'
        resFile = f'{pathToFile}{fileName}{postfix}{extention}'

        resText = []
        startLine = headersLines + 1

        with open(origFile, 'r') as f:
            text = f.readlines()
            if len(text) > 0:
                resText.append(text[headersLines])
                while len(resText) < numberOfLines+startLine:
                    currentLine = random.randint(startLine,len(text)-startLine)
                    resText.append(text[currentLine])
                    text.remove(text[currentLine])

                TxtUtil.rewrite_origin(origFile, text)
                TxtUtil.write_result(resFile, resText)

            else:
                print('It\'s empty here!')

        return resFile
    
    def rewrite_origin(origFile, text):
        with open(origFile, 'w') as f:
                f.writelines(text)

    def write_result(resFile, resText):
        with open(resFile, 'w') as f:
                f.writelines(resText)