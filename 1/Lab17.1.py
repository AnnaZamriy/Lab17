import pandas as pd

df = pd.read_csv("1/input.csv", sep=',')

for s in df.columns:
    suma = df[s].tolist()
    print(s, sum(suma))