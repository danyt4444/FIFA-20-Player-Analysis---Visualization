import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
from collections import Counter

#with open('players_20.csv', newline='') as csvfile:
    #data = csv.DictReader(csvfile)
    #print("OVERALL NAME AGE VALUE SKILL")
    #print("---------------------------------")
    #for row in data:
        #print(row['overall'],row['short_name'], row['age'])

#Read csv file and convert to DataFrame
data = pd.read_csv('players_20.csv')
df = pd.DataFrame(data)


#Analyze top 50 players (name, age, height, wight, rating)
print("These are the 50 best players in FIFA 20")
print("----------------------------------------------------------------")
df_top50 = df[:50][['short_name','age','height_cm','weight_kg','overall']]
print(df_top50)


#statistics regarding these different categories
print(df_top50.describe())


#Create a scatterplot only for goalkeepers based on height and rating/ statistics
gk_data =df[df['player_positions'] == 'GK']
gk_data = gk_data[['height_cm', 'overall']]
print(gk_data)
gk_scatter = (gk_data.plot(x='height_cm', y='overall', style='o'))
plt.savefig('gk_scatter.png')
plt.show(gk_scatter)
print(gk_data.describe())


# Goalkeeper regression
x = gk_data[:200].height_cm
y = gk_data[:200].overall
stats = linregress(x, y)
m = stats.slope
b = stats.intercept
plt.scatter(x, y)
plt.plot(x, m * x + b, color="red")
plt.savefig("figure.png")

#CB data and heatmap
CB_data =df[df['player_positions'] == 'CB']
CB_data = CB_data[['height_cm', 'overall','weight_kg']]

print(CB_data)
print(CB_data.describe())

heatmap1_data = pd.pivot_table(CB_data, values='overall',
                     index=['height_cm'],
                     columns='weight_kg')

heatmap_CB = sns.heatmap(heatmap1_data, cmap="YlOrRd")
heatmap_CB.invert_yaxis()
plt.show(heatmap_CB)


#heatmap for wage, age and overall
heatmap2_data = pd.pivot_table(df[:50], values='wage_eur',
                     index=['overall'],
                     columns='age')
heatmap_wage = sns.heatmap(heatmap2_data, cmap="YlOrRd")
heatmap_wage.invert_yaxis()
plt.show(heatmap_wage)

#Linear Regression for wage and overall
x2 = df[:200].overall
y2 = df[:200].wage_eur
stats = linregress(x2, y2)
m = stats.slope
b = stats.intercept
plt.scatter(x2, y2)
plt.plot(x2, m * x2 + b, color="red")
plt.savefig("figure2.png")


#Top 7 most common nationalities in top 200 highest rated players
most_common_nat = df[:200]['nationality'].value_counts()
top10_most_common_nat = most_common_nat[:7]
top10_most_common_nat.reset_index()
top10_most_common_nat.columns = ['country', 'number_players']
print(top10_most_common_nat)
print(top10_most_common_nat.columns)


#Bar graph for top nationalities
ax = top10_most_common_nat.plot.bar( x='country', y='number_players', rot=0)
plt.ylim(0, 40)
plt.show(ax)


#Top 7 most common clubs for 200 highest rated players
most_common_club = df[:200]['club'].value_counts()
top10_most_common_club = most_common_club[:7]
top10_most_common_club.reset_index()
top10_most_common_club.columns = ['club', 'number_players']
print(top10_most_common_club)
print(top10_most_common_club.columns)

#Bar Graph Top clubs for top 200 rate players
ax = top10_most_common_club.plot.bar( x='club', y='number_players', rot=0)
plt.xticks(fontsize = 6)
plt.ylim(0, 40)
plt.show(ax)












