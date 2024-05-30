import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

# data_one_hot = pd.get_dummies(data['whoAmI'])
# print(data_one_hot.head())

data.loc[(data['whoAmI'] == 'robot'), 'robot'] = True
data.loc[(data['whoAmI'] != 'robot'), 'robot'] = False
data.loc[(data['whoAmI'] == 'human'), 'human'] = True
data.loc[(data['whoAmI'] != 'human'), 'human'] = False
result = data[['human', 'robot']]

print(result)
