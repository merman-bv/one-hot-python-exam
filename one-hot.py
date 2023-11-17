'''
Задача 44:
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
'''

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

#creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

#perform one-hot encoding on 'team' column 
encoder_df = pd.DataFrame(encoder. fit_transform(data[['whoAmI']]). toarray ())

#merge one-hot encoded columns back with original DataFrame
final_df = data.join (encoder_df)

#view final df
print(final_df)
