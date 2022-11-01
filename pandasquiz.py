import pandas as pd
import numpy as np
import requests

# number 1

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df.apply(lambda x: x.max() - x.min())

print(df)


# number 2

data = requests.get('https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip')
data.content

p_data = pd.DataFrame(data)

# number 3 

Answer - Option A

# number 4

data_frame = pd.DataFrame(np.arange(1,11))
data_frame[data_frame > 5] = 10
print(data_frame)

# number 5

albums = requests.get('https://jsonplaceholder.typicode.com/albums').json()

al = pd.DataFrame(albums)
print(al)