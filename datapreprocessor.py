import re
import string
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging

class Preprocessing():
    punctuation = ["\'", "$", "-", "+", "#", ">", "{", "}", "_", "*", "`", "\\", ":", ";", "!", ",", ".", "...", "..",
                   "?", "....", ")", "(", "-"]

    def RemoveNonAlphaCharacters(self,data_input):
        try:
            logging.info("removing non alpha characters initiated")
            regex = re.compile('[%s]' % re.escape(string.punctuation))
            cleanedList = []

            for i in range(len(data_input)):
                currentPhrase = data_input['Text'].values[i]
                #print(currentPhrase)
                tokenizedList = []
                punctualtionSplittedList = []

                for splitPhrase in currentPhrase.split():
                    #print(splitPhrase)
                    splitPhrase = re.sub('\@\w+', '', splitPhrase)
                    splitPhrase = re.sub('\#\w+', '', splitPhrase)
                    splitPhrase = re.sub('\#', '', splitPhrase)
                    splitPhrase = re.sub('RT', '', splitPhrase)
                    splitPhrase = re.sub('&amp;', '', splitPhrase)
                    splitPhrase = re.sub('[0-9]+', '', splitPhrase)
                    splitPhrase = re.sub('//t.co/\w+', '', splitPhrase)
                    splitPhrase = re.sub('w//', '', splitPhrase)
                    splitPhrase = splitPhrase.lower()
                    tokenizedList.append(splitPhrase.split())

                for tokenizedElem in tokenizedList:
                    punctuation_Removed_Elem = regex.sub('', str(tokenizedElem))
                    punctualtionSplittedList.append(punctuation_Removed_Elem)
                    #print(punctualtionSplittedList)

                data_input['Text'].values[i] = punctualtionSplittedList
                #print(data_input)
            logging.info("removing non alpha characters completed")

            return data_input

        except Exception as e :
            raise CustomException(e,sys)


    def RemoveHTMLElements(data_input):
        try:
            pass
        except Exception as e :
            raise CustomException(e, sys)
