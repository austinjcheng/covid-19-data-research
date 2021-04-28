import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('seaborn-whitegrid')
from extract import read_excel

data = read_excel()

def vis(num):

    name = data.iloc[num].name
    # print(name)
    raw = data.iloc[num][0:12]

    raw.index = ['2020-'+ str(i) if i >= 10 else '2020-0'+ str(i) for i in range(1,13)]

    print(raw)

    fig, ax = plt.subplots(figsize=(12, 4))
    raw.plot(ax=ax)

    style = dict(size=10, color='gray')
    ax.text(0.5, 520000, "New Year's Day", **style)
    # ax.text('2012-7-4', 4250, "Independence Day", ha='center', **style)
    # ax.text('2012-9-4', 4850, "Labor Day", ha='center', **style)

    ax.set(title='Retail and food services sales, total',
           ylabel='sum of month sale')


    plt.show()


if __name__ == "__main__":
    vis(0)