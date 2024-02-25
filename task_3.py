
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium



accident_df = pd.read_csv('accident.csv')



print(accident_df.info())



print(accident_df.describe())



print("Missing values per column:")
print(accident_df.isnull().sum())



accident_df.dropna(inplace=True)





accident_map = folium.Map(location=[accident_df['Latitude'].mean(), accident_df['Longitude'].mean()], zoom_start=10)

for index, row in accident_df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']]).add_to(accident_map)

accident_map.save('accident_hotspots_map.html')



fig, axes = plt.subplots(2, 2, figsize=(18, 14))

sns.countplot(x='Road_Conditions', data=accident_df, order=accident_df['Road_Conditions'].value_counts().index, palette='viridis', ax=axes[0, 0])
axes[0, 0].set_title('Accident Counts by Road Conditions')
axes[0, 0].set_xlabel('Road Conditions')
axes[0, 0].set_ylabel('Accident Counts')
axes[0, 0].tick_params(rotation=45)

sns.countplot(x='Weather_Conditions', data=accident_df, order=accident_df['Weather_Conditions'].value_counts().index, palette='mako', ax=axes[0, 1])
axes[0, 1].set_title('Accident Counts by Weather Conditions')
axes[0, 1].set_xlabel('Weather Conditions')
axes[0, 1].set_ylabel('Accident Counts')
axes[0, 1].tick_params(rotation=45)



accident_df['Time'] = pd.to_datetime(accident_df['Time'])
accident_df['Hour'] = accident_df['Time'].dt.hour

sns.countplot(x='Hour', data=accident_df, order=accident_df['Hour'].value_counts().index, palette='coolwarm', ax=axes[1, 0])
axes[1, 0].set_title('Accident Counts by Time of Day')
axes[1, 0].set_xlabel('Hour of Day')
axes[1, 0].set_ylabel('Accident Counts')



sns.pairplot(accident_df[['Latitude', 'Longitude', 'Road_Conditions', 'Weather_Conditions', 'Speed_limit', 'Number_of_Casualties', 'Number_of_Vehicles']], diag_kind='kde')
plt.suptitle('Pairplot of Selected Variables', y=1.02, fontsize=16)
plt.show()



correlation_matrix = accident_df.corr()
plt.figure(figsize=(16, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix')
plt.show()
