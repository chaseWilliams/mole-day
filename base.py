import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


X = pd.read_csv('./data.csv')

molar_mass_data = X.iloc[:, [0, 4]].values
print(molar_mass_data)
