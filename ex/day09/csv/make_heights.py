import pandas as pd
import numpy as np
from scipy import stats

# 
male18 = stats.norm.rvs(171.12,5.55,size=int(stats.norm.rvs(10,5,size=1)))
female18 = stats.norm.rvs(158.03,5.56,size=int(stats.norm.rvs(10,5,size=1)))
male19 = stats.norm.rvs(171.58,5.63,size=int(stats.norm.rvs(10,5,size=1)))
female19 = stats.norm.rvs(158.23,5.37,size=int(stats.norm.rvs(10,5,size=1)))

height = np.concatenate([male18,female18,male19,female19])
age = np.concatenate([np.ones(male18.size,)*18,np.ones(female18.size,)*18,np.ones(male19.size,)*19,np.ones(female19.size,)*19])
gender = np.concatenate([np.ones(male18.size,)*0,np.ones(female18.size,)*1,np.ones(male19.size,)*0,np.ones(female19.size,)*1])

df = pd.DataFrame({'age':age,'gender':gender,'height':height})

# random shuffle
df = df.sample(frac=1).reset_index(drop=True)

# int
df[['age','gender'] = df[['age','gender']].astype(int).astype(str)

# float format %4.1f
df.to_csv('heights.csv',index=False,header=True,float_format='%4.1f')

