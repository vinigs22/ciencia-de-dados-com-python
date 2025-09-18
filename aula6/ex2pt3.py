import pandas as pd
import numpy as np

dataset = pd.read_csv('paises.csv', sep=';')
# print(dataset)

print(dataset.columns)
paises_oceania = dataset.loc[dataset["Region"].str.contains('OCEANIA'), "Country"] .tolist()
print(paises_oceania)

maior_populacao = dataset.nlargest(1, "Population")[["Country", "Region"]]
print(maior_populacao)


group_regions = dataset.groupby('Region')
print(group_regions['Literacy (%)'].mean())

no_coast = dataset[dataset['Coastline (coast/area ratio)'] == 0]
no_coast.to_csv('../datasets/noCoast.csv', sep=';')


def labelHumanitarianHelp(deathRates):
    return pd.Series(np.where(deathRates < 9, "Balanced", "Urgent"))

humaniratial_help = labelHumanitarianHelp(dataset['Deathrate'])
dataset["Humanitarian_Help"] = humaniratial_help
dataset.head()