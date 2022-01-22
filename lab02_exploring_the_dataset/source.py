# Identified dataset : cricket data set

# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import re
import math


# The cricket dataset has many .csv files.
# We will be exploring those files using pandas library to read and parse csv files

# loading dataframes into a dictonary
def load_dataframes(dirPath):
    df_list = { } # a dictionary

    for i in os.listdir(dirPath):
        if os.path.splitext(i)[1] == ".csv": # read only csv files from the dataset
            df = pd.read_csv(f"../cricket_dataset/{i}", delimiter=',')
            df_list[i] = df

    return df_list


# columns in all the dataset
def data_in_dataset(df_list):
    for key in df_list:
        # tmp = df_list[key].columns
        # print(f"\nThe columns in {key} are = \n", tmp)

        dataType = df_list[key].dtypes

        print(f"\nThe data type of the columns of '{key}' is")
        print(dataType)
    


# comparision task 1
# use a bar chart to compare average score of the first 10 batsman in odb.csv
def barCharComparingAvgScore(df_list):
    n = 10
    df = df_list.get("odb.csv") # get the dataframe

    playerNames = []
    avgScore = []

    def valueOfBar(ax, arr):
        for i, v in enumerate(arr):
            ax.text(v + 3, i, str(v), color = 'blue', fontweight='bold')

    for i in range(n): 
        playerNames.append(df.iloc[i]["Player"])
        avgScore.append(df.iloc[i]["Average Score"])

    print(playerNames)
    print(avgScore)

    fig, ax = plt.subplots()

    ax.barh(playerNames, avgScore, align='center')

    valueOfBar(ax, avgScore)

    plt.xlabel("Name of player")
    plt.ylabel("Average score of player")
    plt.title("Comparision of average score of first 10 batsman")
    plt.show()



# composition task 1
# pie chart of total number of run of teams from different countries / areas

# here the country is given in the name of player in brackets
# so we can use regex to match the first string inside the bracket


def removeBracketAndSlashes(str):
    start, end = 0, len(str)

    if(str[0] == '('):
        start = 1
    
    if(str[-1] == '/'):
        end -= 1
    
    return str[start : end]

def getCountryNames(df):
    data = {} # dictonary
    total_runs = 0
    regstr = r"(\([a-zA-Z]+\/?)"

    for i in range(len(df)):
        m = re.search(regstr, df.iloc[i]["Player"])
        countryName = removeBracketAndSlashes(m.group(0) )

        if(countryName in data):
            total_runs += df.iloc[i]["Runs"]
            data[countryName] += df.iloc[i]["Runs"]
        else:
            total_runs += df.iloc[i]["Runs"]
            data[countryName] = df.iloc[i]["Runs"]     

    return total_runs, data

def PieChartOfRunByAreas():
    total_runs, runsByArea = getCountryNames(df_list.get("odb.csv"))

    print(total_runs, runsByArea)

    fig, ax = plt.subplots()

    ax.pie(runsByArea.values(),labels=runsByArea.keys(), radius=5, 
            autopct= lambda p : "{:.2f}% ({:d})".format(p, int(p * sum(runsByArea.values()) // 100) ) )

    plt.show()


# comparative task 2
# compare consitency of bowlers with a given span preferably

def parseSpan(spanObj):
    lst = list(map(int, spanObj.split("-")) )
    return lst[1] - lst[0]

def bowlerSpanComparision(df_list):
    df = df_list.get("odbo.csv")
    year_cnt = {}

    for i in range(len(df)):
        span = parseSpan(df.iloc[i]["Span"])
        if span in year_cnt:
            year_cnt[span] += 1
        else:
            year_cnt[span] = 1

    print( dict(sorted(year_cnt.items(), key= lambda x : x[1]) ) )


if __name__ == '__main__':
    df_list = load_dataframes("../cricket_dataset.csv")