import pandas as pd
import pandas as pd
import re
import string
from string import digits
import datetime

class BaseCleanup():
    
    """
    This is base class for cleanup something
    """

    @staticmethod
    def calculate_age(date):
        today = datetime.datetime.now()
        current_year = today.year

    @staticmethod   
    def get_year(date):
        input_date = 
        return(year)

class TextCleanup():

    """
    This class use for cleanup text object
    """

    @staticmethod
    def change_to_lowercase(text):
        return text.lower()

    @staticmethod
    def change_to_uppercase(text):
        return text.upper()

    @staticmethod
    def remove_single_quote(text):
        result = re.sub("'", "", text)
        return result

    @staticmethod
    def remove_double_quote(text):
        result = re.sub('"', '', text)
        return result 

class ListCleanup():

    """
    This class use for cleanup list object
    """
    pass

class DataFreameCleanup():
    
    @staticmethod
    def change_to_lowercase(df, column_name):
        df[:][column_name] = df[:][column_name].apply(lambda x: x.lower())
        return df

    @staticmethod
    def remove_single_quote(df, column_name):
        df[:][column_name] = df[:][column_name]. \
            apply(lambda x: re.sub("'", "", x))
        return df
    
    @staticmethod
    def remove_double_quote(df, column_name):
        df[:][column_name] = df[:][column_name]. \
            apply(lambda x: re.sub('"', '', x))
        return df

    @staticmethod
    def remove_special_character(df, column_name):
        special_characters= set(string.punctuation)
        df[:][column_name] = df[:][column_name]. \
            apply(lambda x: ''.join(char1 for char1 in x if char1 not in \
                special_characters))
        return df

    @staticmethod
    def remove_digit(df, column_name):
        num_digits= str.maketrans('','', digits)
        df[:][column_name] = df[:][column_name]. \
            apply(lambda x: x.translate(num_digits))
        return df

    @staticmethod
    def remove_space(df, column_name):
        df[:][column_name] = df[:][column_name]. \
            apply(lambda x: x.strip())
        return df