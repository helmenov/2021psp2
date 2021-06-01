# %%
import pandas as pd

#%%
df = pd.read_csv('mydata2.csv',header=0,index_col=0,skipinitialspace=True)

#%%
print(df)

print(df.values)
#%%
print(df.columns)

#%%
print(df['favoriteAnimal'])

#%%
print(df['favoriteAnimal']['aa83988848'])

#%%
print(df.iloc[1,1])

#%%
print(df.describe(include='all'))

#%%
print('{}'.format(df['favoriteAnimal'][2]))
# %%
