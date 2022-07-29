class SimilarityCalculation:

    def first_way(firstArray, secondArray):
        for person in secondArray:
            for human in firstArray:
                if(human == person):
                    firstArray.remove(person)
        print(firstArray)

    def second_way(firstArray, secondArray):
        res = list(set(firstArray) - set(secondArray))
        print(res)