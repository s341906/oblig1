import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import re

url = "https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/assignment1/Ruter_data.csv"
df = pd.read_csv(url, sep=';')

#df['Dato'].value_counts().sort_index().plot.bar()
#plt.show()

df['Avgangstid_p'] = pd.to_datetime(df.Tidspunkt_Planlagt_Ankomst_Holdeplass_Fra, errors='coerce')

a = df.assign(avg_tid = pd.cut(df.Avgangstid_p.dt.hour,[0,6,12,18,24],labels = ['Natt','Morgen','Dag','Kveld']))

df['Avg_tid_omr'] = a['avg_tid']

df['Avg_tid_omr'].value_counts().sort_index().plot.bar()
plt.show()

ledig = (df['Kjøretøy_Kapasitet'].values - df['Passasjerer_Ombord'].values)/df['Kjøretøy_Kapasitet'].values
df['Ledig'] = ledig

df.plot.scatter(x='Linjenavn', y='Ledig', title='Graf')
plt.show()

df.head()

#print(df)
