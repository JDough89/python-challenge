#Imports necessary libraries
import pandas as pd
import numpy as np
import math

#Assigns and imports the PyBank.csv file
df = pd.read_csv('/Users/Jackson/Desktop/DUBootCamp/Module3Challenge/Instructions/PyBank/Resources/budget_data.csv')

#Checks to see if there are any empty cells within the dataset
df.isna().any()

#Formats float values
def format_float(value):
    return f'{value:,.2f}'

#Determines the total for the "Profits/Losses" column
total = df['Profit/Losses'].sum()

#Determines the the number of months based on the number of rows
monthcount = df.shape[0]

#Creates a new column for comparison
df['shifted_column'] = df['Profit/Losses'].shift(1)

#Compares the difference between the original column values and the newly created colum
df['difference'] = df['Profit/Losses']-df['shifted_column']

#determines the average of the newly created column
average = df['difference'].mean()

#Determines the maximum increase per month
maximum = df['difference'].max()

#Determines the maximum decrease per month
minimum = df['difference'].min()

#Outputs the resluts
print(" Financial Analysis","\n","-----------------",'\n', "Total Months:", monthcount,'\n', "Total:", "$",total,"\n", "Average Change:", "$","%.2f" %  average, "\n", 
      "Greatest Increase in Profits: ", math.trunc(maximum), "\n", "Greatest Decrease in Profits: ", math.trunc(minimum) )

#Assigns and imports the PyPoll.csv file
df1 = pd.read_csv('/Users/Jackson/Desktop/DUBootCamp/Module3Challenge/Instructions/PyPoll/Resources/election_data.csv')

#Checks to see if there are any empty cells within the dataset
df1.isna().any()

#Determines total number of votes based on number of rows in the .csv files
TotalVotes = df1.shape[0]

#Determines the number of votes for Diana DeGette
DGVoteCount = df1['Candidate'].value_counts()['Diana DeGette']

#Determines the number of votes for Charles Casper Stockham
CCSVoteCount = df1['Candidate'].value_counts()['Charles Casper Stockham']

#Determines the number of votes for Raymon Anthony Doane
RADVoteCount = df1['Candidate'].value_counts()['Raymon Anthony Doane']

#Determines the vote percentage for Diana Degette
DGVotePercentage = (DGVoteCount/TotalVotes)*100

#Determines the vote percentage for Charles Casper Stockham
CCSVotePercentage = (CCSVoteCount/TotalVotes)*100

#Determines the vote percentage for Raymon Anthony Doane
RADVotePercentage = (RADVoteCount/TotalVotes)*100

#Set the variable "winner" based on the candidate whose name appeared most in the column 'Candidate'
winner = df1['Candidate'].value_counts().idxmax()

#Outputs the results
print(" Election Results", '\n', "----------","\n","Total Votes:", TotalVotes,"\n","----------","\n", "Diana DeGette:", "%.3f" % DGVotePercentage,"%","(",DGVoteCount,")","\n",
      "Charles Casper Stockham: ", "%.3f" %CCSVotePercentage, "%", "(",CCSVoteCount,")","\n", "Raymon Anthony Doane: ","%.3f" % RADVotePercentage,"%", "(",RADVoteCount,")"  "\n", 
      "----------" ,"\n", "Winner: ", winner,"\n","----------")
