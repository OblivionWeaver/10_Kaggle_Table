import pandas
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def Correlation_Graph(data,main_column,num):
    corrmat = data.corr()
    cols = corrmat.nlargest(num, main_column)[main_column].index
    cm = np.corrcoef(data[cols].values.T)
    sns.set(font_scale=1.25)
    hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
    plt.show()
