import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import seaborn as sns

data = pd.read_csv('mobile_cleaned.csv')
# head, tail
#print(data.shape)
#ax = sns.scatterplot(x='stand_by_time', y='battery_capacity', hue='thickness', data=data)
#ax = sns.displot(data["stand_by_time"])
ax = sns.boxplot(x='is_liked', y='battery_capacity', data=data)
plt.show()