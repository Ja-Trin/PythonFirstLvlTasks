from ResourceUtil import ResourceUtil as R
from ReaderUtil import ReaderUtil as Reader
import TxtUtil
import os

class FileSelector:

    config = Reader.read_json(R.resource, R.path)

    pathToFile = f'{os.getcwd()}{config["path"]}'
    numberOfLines = config['numberOfLines']

    res = TxtUtil.TxtUtil.rewriter(pathToFile, numberOfLines)
    print(res)