import datetime as datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.plotting.register_matplotlib_converters()
DATE_AXIS = {'Jan  ': 'Jan', 'Feb  ': 'Feb', 'Mar  ': 'Mar', 'Apr  ': 'Apr', 'May  ': 'May', 'Jun  ': 'Jun',
             'July  ': 'Jul', 'Aug  ': 'Aug', 'Sep  ': 'Sep', 'Oct ': 'Oct', 'Nov': 'Nov', 'Dec': 'Dec'}
FILENAME = 'rnd_contest_data.xlsx'
SHEET_WITH_DATA = 'REF raw data'
SHEET_WITH_BRANDS = 'brand encoding'
ALL_COLUMNS = ['Source', 'Month', 'Year', 'Logic', 'Brand', 'Model', 'CONSTRUCTION', 'NO. OF DOORS', 'FREEZ. POSITION',
               'HEIGHT IN CM ', 'WIDTH IN CM', 'DEPTH IN CM', 'ENERGY LABEL EU', 'NOFROST SYSTEM', 'NET LTRS.',
               'NETFREEZER LTR.', 'NETFRIG. LTRS.', 'FRONT DECORAT.', 'ICE-CUBE DISPEN', 'WATER DISPENSER',
               '0° COOLING',
               'DISPLAY', 'MOUNTING SYSTEM', 'FirstActivity', 'Sales Units', 'Sales Units%', 'SALES THS.UAH',
               'SALES THS.USD', 'SALES THS.EUR', 'Sales Value%', 'D.UNW. SALES', 'D.WGT. SALES', 'PRICE UAH/UN.',
               'PRICE INDEX%', 'PRICE USD/UN.', 'PRICE EUR/UN.', 'TOS VAL', 'Amount', 'SAP  Name', 'REF type',
               'PJT Name', 'Year2', 'Quarter', 'Type segment', 'TTL Segment', 'Address market', 'Month_', 'Height',
               'Half year', 'Price segment USD_TTL', 'Price segment USD_BMF', 'Price segment USD_TMF',
               'Price segment USD_SBS', 'Price segment USD_B-IN']


def give_data(columns=ALL_COLUMNS):   #получим pandas dataframe
    data = pd.read_excel(FILENAME, sheet_name=SHEET_WITH_DATA)
    data = data[columns]  #берем не все колонки
    data['Month'].replace(list(DATE_AXIS.keys()),
                          list(map(lambda x: datetime.datetime.strptime(x + '2018', '%b%Y'), list(DATE_AXIS.values()))),
                          inplace=True)
    data.rename(columns={'Sales Units': 'Quantity', 'PRICE USD/UN.': 'PriceUSD'}, inplace=True)
    data = data[data['Brand'] != '<OT>']
    return data


def plot_dynamics_plt(data, models=[], title=''):  
    d = data[data['Model'].isin(models)]
    ax = plt.gca()
    legend = []
    plt.title(title)
    for j in d.Model.unique():
        d2 = d[d['Model'] == j]
        d2[['Month', 'SALES THS.USD']].plot(kind='line', x='Month', y='SALES THS.USD', ax=ax, legend=False)
        legend += [j]
    plt.legend(legend)
    plt.show()


def plot_dynamics(data, models=[], title=''): #получим график продаж по всем моделям у models
    sns.set()
    d = data[data['Model'].isin(models)]
    fig = sns.relplot(x='Month', y='SALES THS.USD', hue="Model", kind="line",
                      data=d[['Month', 'SALES THS.USD', 'Model']])
    fig.fig.suptitle(title)
    plt.show()


def give_models_tree(data):     #получим словарь: ключ-бренд,значение-список моделей
    res = {}
    for i in list(data['Brand'].unique()):
        res[i] = list(data[data['Brand'] == i]['Model'].unique())
    return res


def plot_dynamics_brand(data, name, max_p=6, mean_p=2, min_p=1, correct_length=6):
    models = data[data['Brand'] == name]['Model'].unique()
    r = []
    for i in range(len(models)):
        if (data[data['Model'] == models[i]]).shape[0] < correct_length_of_sales:
            r += [i]
    models = np.delete(models, r)
    if len(models) > max_p+min_p+mean_p:
        models = sorted(models, key=lambda x: (data[data['Model'] == x])['SALES THS.USD'].mean())
        res = models[:min_p:] + models[len(models) // 2 - mean_p // 2:len(models) // 2 + mean_p // 2 + mean_p % 2:] + models[-max_p::]
        plot_dynamics(data, res, name)
    else:
        plot_dynamics(data, models, name)
