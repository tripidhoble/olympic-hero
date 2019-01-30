# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
print(data.head(10))


# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']<data['Total_Winter'],'Winter','Both'))
print(data.head(10))
better_event = data['Better_Event'].value_counts().idxmax()

print(better_event)


# --------------
#Code starts here

#print(data.head())
#top_countries = data['Country_Name','Total_Summer']
#print(top_countries.head())
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
#print(top_countries.tail(1))
top_countries.drop(top_countries.index[len(top_countries)-1],inplace=True)
#print(top_countries.tail(1))

def top_ten(df,column):
    country_list = []
    country_list = list(df.nlargest(10,column)['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
print("top_10_summer: \n", top_10_summer)

top_10_winter = top_ten(top_countries,'Total_Winter')
print("top_10_Winter: \n",top_10_winter)

top_10 = top_ten(top_countries,'Total_Medals')
print("top_10: \n",top_10)

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print("common: \n",common)












# --------------
#Code starts here


print(top_10_summer)
summer_df = data[data['Country_Name'].isin(top_10_summer)]
#print(summer_df)

print(top_10_winter)
winter_df = data[data['Country_Name'].isin(top_10_winter)]
#print(winter_df)

print(top_10)
top_df = data[data['Country_Name'].isin(top_10)]
#print(top_df)

ax = summer_df.plot.bar(x='Country_Name', y='Total_Summer', rot=45)
ax1 = winter_df.plot.bar(x='Country_Name', y='Total_Winter', rot=45)
ax2 = top_df.plot.bar(x='Country_Name', y='Total_Medals',rot=45)


# --------------
#Code starts here

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
print('summer_df: \n',summer_df)
summer_max_ratio = summer_df['Golden_Ratio'].max()
print('summer_max_ratio: ',summer_max_ratio)
summer_country_gold = summer_df.ix[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print('summer_country_gold: ',summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
print('winter_df: \n',winter_df)
winter_max_ratio = winter_df['Golden_Ratio'].max()
print('winter_max_ratio: ',winter_max_ratio)
winter_country_gold = winter_df.ix[winter_df['Golden_Ratio'].idxmax(), 'Country_Name']
print('winter_country_gold: ',winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
print('top_df: \n',top_df)
top_max_ratio = top_df['Golden_Ratio'].max()
print('top_max_ratio: ',top_max_ratio)
top_country_gold = top_df.ix[top_df['Golden_Ratio'].idxmax(), 'Country_Name']
print('top_country_gold: ',top_country_gold)








# --------------
#Code starts here



data_1 = data.drop(data.index[len(data)-1])

data_1['Total_Points'] = (data_1['Gold_Total']*3)+(data_1['Silver_Total']*2) + (data_1['Bronze_Total']*1)
print(data_1)

most_points = data_1['Total_Points'].max()
print('most_points: ', most_points)
best_country = data_1.ix[data_1['Total_Points'].idxmax(), 'Country_Name']
print('best_country: ', best_country)


# --------------
#Code starts here

best = data[data['Country_Name'] == best_country]
#print(best)

best = best[['Gold_Total','Silver_Total','Bronze_Total']]
print(best)

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)





