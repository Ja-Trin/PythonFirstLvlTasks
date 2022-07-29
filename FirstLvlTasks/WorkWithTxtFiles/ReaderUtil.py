import os
import json

class ReaderUtil:
    
    def read_json(resource, pathToResource = ''):
        os.chdir(f'{os.getcwd()}{pathToResource}')
        with open(resource, 'r') as c:
            config = json.load(c)
        return config

