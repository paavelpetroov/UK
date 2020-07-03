import pandas as pd
import xlrd


def to_csv(address,destination):
    excel_file = pd.read_excel(address)
    excel_file.to_csv(destination)
    df = pd.read_csv(destination)
    return df

def filter_columns(dataframe):
    try:
        to_del = list(filter(lambda x: x.find("Unnamed")==0,list(dataframe.columns)))
        dataframe.drop(to_del, axis='columns', inplace=True)
    except ZeroDivisionError:
        pass
    return dataframe
