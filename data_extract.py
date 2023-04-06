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
    #modifying data
    obj_preprocessor = Preprocessing()
    df_modified = obj_preprocessor.DataSetModifying(data_input)

    #Preprocessing of data



    #data_preprocessed = obj_preprocessor.RemoveNonAlphaCharacters(data_input)
    #data_preprocessed2 = obj_preprocessor.RemoveHTMLElements(data_preprocessed)
    #print(data_preprocessed.head(1000))
