import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


path = 'rnd_contest_data.xlsx'
df= pd.read_excel(path, sheet_name="REF raw data")
print(df.head())
df['Date'] =df["Year"].astype(str)+' '+df["Month"]
df['Date'] = pd.to_datetime(df['Date'])

def graph_sales(data, models_l=[]):
    '''
    График продаж(дин).
    :param data: df
    :param models_l: Список моделей, данные которых исп для гр
    '''


    d = data[data['Model'].isin(models_l)]
    sns.relplot(x='Date', y='SALES THS.USD', hue="Model", kind="line",data=d[['Date', 'SALES THS.USD', 'Model']])
    sns.set()
    plt.show()

graph_sales(df, ['KGN39VL306','KGN39VW306','KGN49XL30G','KGN36VL306','KGN39XI306','KGN49XW30U','KGN39XL35','KGN39XW306','KGV36UW206'])


