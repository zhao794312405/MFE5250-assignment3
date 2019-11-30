import pandas as pd

dic = {'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin','Jonas'],
        'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
        'score':[12.5, 9, 16.5,float('nan') , 9, 20, 14.5, float('nan'), 8, 19]}
df=pd.DataFrame(dic)
print('In: \n', df)
df2 = df.sort_values(by=['attempts', 'name'])
print('Out: \n', df2)