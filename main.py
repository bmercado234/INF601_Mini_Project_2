# INF601 - Advanced Programming in Python
# Braulio Mercado
# Mini Project 2

import pandas as pd
import pprint
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("spotify-2023.csv", encoding='latin1')

print(df)
df.plot()
plt.show()
