import os
import json
import SimilarityCalculation

class Arrays:
    resource = 'data.json'
    pathToResource = '\\ArraysDifference'

    os.chdir(f'{os.getcwd()}{pathToResource}')

    with open(resource, 'r') as file:
        text = json.load(file)

    firstArray = text['firstArray']
    secondArray = text['secondArray']

    print(f'{firstArray}\n{secondArray}')

    SimilarityCalculation.SimilarityCalculation.first_way(firstArray, secondArray)
    SimilarityCalculation.SimilarityCalculation.second_way(firstArray, secondArray)