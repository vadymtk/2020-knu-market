import matplotlib.pyplot as plt

import seaborn as sns

import statsmodels.formula.api as smf

import statsmodels.api as sm

import pandas as pd



def elasticity_ols(data, give_info=False):# будує лінійну регресію відносно dataframe: Quantity ~ PriceUSD

    linreg = smf.ols('Quantity ~ PriceUSD', data=data).fit()

    if give_info:

        print(linreg.summary())

        sns.set()

        fig1 = plt.figure(figsize=(12,8))

        fig2 = plt.figure(figsize=(12, 8))

        fig3 = plt.figure(figsize=(12,8))

        fig1 = sm.graphics.plot_partregress_grid(linreg, fig=fig1)

        fig2 = sm.graphics.plot_ccpr_grid(linreg, fig=fig2)

        fig3 = sm.graphics.plot_regress_exog(linreg, 'PriceUSD', fig=fig3)

        plt.show()

    return linreg.params.PriceUSD





def elasticity_ols_models(data, models, give_info=False, correct_length_of_sales=9):# знаходить эластичність по всіх моделях у models

    d = data[data['Model'].isin(models)]

    res = {}

    for j in d.Model.unique():

        d2 = d[d['Model'] == j]

        if (data[data['Model'] == j]).shape[0] >= correct_length_of_sales:

            try:

                res[j] = elasticity_ols(d2, give_info)

            except Exception:

                pass

    return pd.DataFrame.from_dict({'Model' : list(res.keys()), 'Elasticity' : list(res.values())})
