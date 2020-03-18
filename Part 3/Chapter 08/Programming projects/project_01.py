#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import numpy as np
import pandas as pd

#%%


def get_data_list(file_name : str) -> list:
    """
    Reads the data from a .csv file, and stores the rows as lists in a list.

    Parameters
    ----------
    file_name : str
        The filename of the csv file containg all the data.

    Returns
    -------
    list
        The list of lists containing all the stock market data.
    """
    
    data_file = open(file_name,"r")
    data_list = [ ] # start with an empty list
    for line_str in data_file:
        data_list.append(line_str.strip().split(','))
    return data_list


def get_monthly_averages(in_list : list) -> pd.core.frame.DataFrame:
    """
    Gets a list of lists, and transforms them into a dataframe containing data
    on the average prices per month and per year.

    Parameters
    ----------
    in_list : list
        The list of lists extracted from the .csv file.

    Returns
    -------
    pd.core.frame.DataFrame
        The final dataframe containing melted data.
    """
    
    # create a pandas DF based on the data
    df         = pd.DataFrame(in_list[1:])
    df.columns = in_list[0]
    
    # add columns for the extra variables we need
    df["Month"]   = df["day"] = \
        df["Year"] = df["Average monthly prices"] = np.zeros(len(df))
    
    # adjust the DF values
    for i, row in df.iterrows():
        df.at[i, "Year"], df.at[i, "Month"], df.at[i, "Day"] = df.at[i, "Date"].split("-")
        df.at[i, "Average monthly prices"] = float(df.at[i, "Adj Close"]) * float(df.at[i, "Volume"])
    del i, in_list, row
    
    # return the mean values grouped by year and month    
    return df.groupby(["Year", "Month"]).mean()


def print_info(dataframe : pd.core.frame.DataFrame) -> None:
    """
    Prints the 5 most (un)successfull months on the stock market.

    Parameters
    ----------
    dataframe : pd.core.frame.DataFrame
        The dataframe in a melted format, containing the averages per month
        and per year.

    Returns
    -------
    None
        Simply prints the relevant output.
    """
    
    pd.set_option('display.float_format', lambda x: '%d' % x)
    
    print("\n- - -\nLowest monthly prices\n- - -\n")
    print(dataframe["Average monthly prices"].sort_values()[:5])
    
    print("\n- - -\nHighest monthly prices\n- - -\n")
    print(dataframe["Average monthly prices"].sort_values()[-5:])
    

#%%

def main():
    in_list = get_data_list("table.csv")
    df_av   = get_monthly_averages(in_list)
    print_info(df_av)