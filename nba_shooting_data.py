# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 13:10:40 2022

@author: Kevin Luu
"""

##For the NBA shooting data, we want to:
##1. EXPLORE: At what range is each player most likely to score a shot
##2. VISUALIZE: Plot the shots made by X and Y position on the court. For each 
##shot, differentiate between the four different players
##3. ANALYZE: Are players most likely to score a shot the closer they get to the
##basket?

#Necessary libraries to use
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset
df = pd.read_csv("C:\\Users\\Kevin Luu\\Downloads\\nba_shooting_data.csv")
print(df)

#Printing out the rows and columns of the dataset
print("The numbers of rows and columns of the dataset", df.shape)

#Loading the first five values from the dataset
df_h = df.head()
print(df_h)

#Want to know information about the dataset
df_i = df.info()
print(df_i)

#Now we want to use isna() function and aggregate the dataset using sum() 
##function to get the total count of missing values
df_is = df.isna().sum()
print(df_is)

#We see that there are 0 missing values, so no need to manipulate to dataset

#Using statistics
df_stats = df.describe()
print(df_stats)

#In addition, we can find the top recurrence in the dataset
df_recurrence = df.describe(include = object)
print(df_recurrence)

#We see that Trae Young is the most frquent player who missed his shots, and
#blocked by Russell Westbrook. 

#Want to know at what range is each player most likely to score a point

#For shooters
df_shooter = df['SHOOTER'].unique()
print("The shooters in the dataset are", df_shooter)

df_shooter_values = df['SHOOTER'].value_counts(dropna=True)
print(df_shooter_values)

#For ranges
df_range = df['RANGE'].unique()
print("The ranges in the dataset are", df_range)

df_range_values = df['RANGE'].value_counts(dropna=True)
print(df_range_values)

#Want to compare between the players and ranges
shooter_range_compare = df.groupby(['SHOOTER', 'RANGE', 'SCORE']).sum()
print(shooter_range_compare)

#Seeing the data, we predict that Chris Paul would make his shots on the range,
#(10,14), Russell Westbrook for the range (15,19), Seth Curry for the range of
#(25,29), and Trae Young for the range of (25,29) as well.

#Data Visualization
shots = df[['SHOOTER', 'SCORE']]

shots['SCORE'].hist(by=shots['SHOOTER'])

#Based on the graph, we see that Seth Curry has made most of his shots than Russell
#Westbrook, and Trae Young. We also notice that Chris Paul has missed his shots more
#but the shots he made are barely close to his missed shots.

#We want to analyze if the players are most likely to score a shot the closer
#they get to the basket.

#Calculating the averages to see the players are most likely to score a shot
#the closer they get to the basket
shooter_range_averages = df.groupby(['SHOOTER', 'RANGE', 'SCORE']).mean()
print(shooter_range_averages)

#Based on this, we see that the players are most not likely to score a shot the closer
#they get to the basket



