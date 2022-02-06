# # Extracting data from the [Spanish Statistical Office (INE)](https://www.ine.es/en/index.htm)

# The Spanish Statistical Office provides an API to extract data.
# - The request is of the form `https://servicios.ine.es/wstempus/jsstat/{language}/DATASET/{table_id}`
#     - The language can be `EN` (English) or `ES` (Spanish)
#     - The table ID is obtained by looking at the `t` parameter of the table we want to extract
#         - For example, the ID of the table ["Immigration flow from abroad by year, sex and age"](https://www.ine.es/jaxiT3/Tabla.htm?t=24387&L=1) is `24387`
# - The data is returned as a [JSON-stat](https://json-stat.org) object. We can use the library `pyjstat` to easily process this object and convert it to a pandas dataframe
# - More instructions [here](https://www.ine.es/dyngs/DataLab/en/manual.html?cid=1259945948447) (although no English version!)

# The following code provides an example of how to extract the data from the table ["Immigration flow from abroad by year, sex and age"](https://www.ine.es/jaxiT3/Tabla.htm?t=24387&L=1)

# ## Setup

from IPython.display import display
import numpy as np
import pandas as pd
from pyjstat import pyjstat
import seaborn as sns
import matplotlib.pyplot as plt

# ## Data extraction

# Immigration flow from abroad by year, sex and age
URL = 'https://servicios.ine.es/wstempus/jsstat/EN/DATASET/24387'
raw_data = pyjstat.Dataset.read(URL).write('dataframe')
display(raw_data.head())

# ## Data preparation

data = (raw_data
    .rename(columns={'Periodo': 'Period'})
    .assign(**{'value': lambda df: df['value'].astype('int')})
    .assign(**{'Year': lambda df: df['Period'].str[:4]})
)
display(data.head())

# ## Visualization example

# +
df = (data
    .loc[lambda df: df['Sex'] == 'Both sexes']
    .loc[lambda df: df['Age'] == 'Total']
    # Aggregate semesters
    .groupby(['Year'], as_index=False)
    .agg({'value': 'sum'})
)

g = sns.lineplot(
    data=df,
    x='Year', y='value',
    marker='o',
)

g.set(title='Number of inmigrants per year', xlabel='', ylabel='')
ylabels = [f'{x / 1000:.0f} K' for x in g.get_yticks()]
g.set_yticks(g.get_yticks().tolist())
g.set_yticklabels(ylabels)
plt.xticks(rotation=45)
plt.grid()

plt.show()
