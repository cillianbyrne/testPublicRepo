# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import math
import numpy as np
import datetime


print("Hi")

covid_data = pd.read_csv(r"C:\Users\Cillian\PycharmProjects\Kaggle CSVs\owid-covid-data.csv")

def func(x, pos):  # formatter function takes tick label and tick position
    s = str(x)
    ind = s.index('.')
    s = s[:ind]
    l = len(s)
    if l <=3:
        return s
    else:
        its = int(math.floor((l-.01)/3))
        for i in range(0, its):
            y = (3*(i+1))
            s = s[:l-y] + "," + s[l-y:]
        return s

#print(covid_data.head())
print(covid_data.columns.values.tolist())
#print(covid_data["date"].unique())
#print(covid_data["location"].unique())

irish_data = covid_data.loc[covid_data["location"] == "Ireland"]
irish_day_data = irish_data.loc[irish_data["date"] == "2020-12-31"]

print(irish_day_data.describe())

irish_total_data = irish_data[["date","total_cases","total_deaths","total_tests"]].dropna()
print(irish_total_data)

dates_as_dates = [datetime.datetime.strptime(d, "%Y-%m-%d") for d in irish_total_data["date"]]

colour = "Blue"
fig, ax1 = plt.subplots()
ax1.set_ylabel('Cases', color=colour)
ax1.plot(dates_as_dates, irish_total_data["total_cases"]*1000000, label = "Total Cases", color=colour)
ax1.yaxis.set_major_formatter(tkr.FuncFormatter(func))


colour="Red"
ax2 = ax1.twinx()
ax2.set_ylabel('Deaths', color=colour)
ax2.plot(dates_as_dates, irish_total_data["total_deaths"]*1000000, label = "Total Deaths", color=colour)
ax2.yaxis.set_major_formatter(tkr.FuncFormatter(func))



plt.title('Cases & Deaths of COVID in Ireland')
plt.xlabel('Dates')
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


