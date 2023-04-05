import os
import sys
from src.logger import logging
import pandas as pd
from src.exception import CustomException
from src.datapreprocessor import Preprocessing




class DataExtract:
    def data_extract(self):
        try:
            df = pd.read_csv(r'C:\Users\chathuri_105085\PycharmProjects\assignment\data\Language Detection.csv')
            logging.info("reading data completed")
            #print(df.head())
            return df
        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj = DataExtract()
    #Extraction of data
    data_input= obj.data_extract()
    logging.info("data is ingested")
    #Preprocessing of data
    obj_preprocessor = Preprocessing()
    data_preprocessed = obj_preprocessor.RemoveNonAlphaCharacters(data_input)
    print(data_preprocessed)