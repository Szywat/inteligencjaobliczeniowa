import pandas as pd
import numpy as np

df = pd.read_csv("iris_with_errors.csv")

values = df.values[:, :4]

for i in range(len(values)):
    for j in range(len(values[i])):
        if float(values[i][j]):
            print(values[i][j])

        # print(values[i][j])
# print(df.values[:, :4])