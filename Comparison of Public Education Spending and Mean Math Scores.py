import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#read data files
score_data = pd.read_csv('PISA Mean Math Scores.csv')
spending_data = pd.read_csv('OECD Public Education Spending.csv')

#removing unneeded rows and grouping data
score_data = score_data.drop(['INDICATOR','FREQUENCY','MEASURE','Flag Codes'], axis=1)
avg_score = score_data.groupby(['LOCATION','TIME']).agg({'Value':np.mean})

#removing unneeded rows
spending_data = spending_data.drop(['INDICATOR','SUBJECT','MEASURE','FREQUENCY','Flag Codes'],axis=1).dropna()

#creating a new dataframe by joining the other two
edu_data = pd.merge(avg_score, spending_data, on=['LOCATION','TIME'])

edu_data = edu_data.rename(columns = {'LOCATION':'Country', 'Value_x':'Mean_Score', 'Value_y':'Spending'})
#countries = ['USA','CAN','ITA','FRA','GBR','JPN','SWE','RUS','ESP']
#edu_data = edu_data[edu_data['Country'].isin(countries)]

#print(edu_data) 

#plt.plot(edu_data.Spending, edu_data.Mean_Score, 'ro')
plt.plot(edu_data.Country, edu_data[edu_data['Mean_Score'].index()])



