import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

fig = plt.figure()
ax = plt.axes()
formatter = ticker.ScalarFormatter()
formatter.set_scientific(False)
ax.yaxis.set_major_formatter(formatter)
CSV_FILE_PATH = './reduced_2020_Taxi_Trip_Data.csv'

df = pd.read_csv(CSV_FILE_PATH)
df.columns = ['month','trip_time','passenger','distance','rate','fare']

distance = df['distance']
month = df['month']
fare = df['fare']
d_m = pd.DataFrame({'month':month,'distance':distance}).groupby('month')['distance'].mean()
d_f = pd.DataFrame({'month':month,'fare':fare}).groupby('month')['fare'].mean()


cause = []
death = []

def compare(x):
    return int(x[0].split('-')[1])


with open('./cause','r') as f:
    for i in f.readlines():
        cause.append(i.split())

list.sort(cause,key=compare)

with open('./death','r') as f:
    for i in f.readlines():
        death.append(i.split())

list.sort(death,key=compare)


month = [i for i in range(3,13)]
d = [int(death[i][1]) for i in range(len(death))]
c = [int(cause[i][1]) for i in range(len(cause))]

plt.subplots_adjust(hspace=0.5, wspace=0.3)
ax1 = plt.subplot(411)
ax1.yaxis.set_major_formatter(formatter)
plt.plot(month,d,'-g',label="month_death")
plt.legend(loc="lower right")

month_2 = [i for i in range(1,13)]

ax2 = plt.subplot(412)
ax2.yaxis.set_major_formatter(formatter)
plt.plot(month,c,'--c',label="month_cause")
plt.legend(loc="lower right")

ax3 = plt.subplot(413)
ax2.yaxis.set_major_formatter(formatter)
plt.plot(month_2,d_f,'-r',label="month_avg_fare")
plt.legend(loc="lower right")

ax4 = plt.subplot(414)
ax2.yaxis.set_major_formatter(formatter)
plt.plot(month_2,d_m,'-b',label="month_avg_distance")
plt.legend(loc="upper left")
plt.show()
#
#
#
# # ax.plot(, np.sin(x), '-b', label='Sine')