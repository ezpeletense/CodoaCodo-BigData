import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
#print(tips)

df = pd.read_csv('cars_depurado.csv')
#print(df)

sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex')
plt.savefig('plot1.png', dpi=300)
plt.show()
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.savefig('plot2.png', dpi=300)
plt.show()