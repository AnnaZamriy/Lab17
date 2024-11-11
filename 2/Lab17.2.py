import pandas as pd
import numpy as np 

series = pd.read_csv("2/words.txt", sep=",")

list1 = series["СЛОВА"].tolist()

list2 = []

#голосні
list3 = ['у','е','ї','і','а','о','є','я','и','ю']

def count(word):
    c = 0
    for i in word:
        if i in list3:
            c += 1
    return c

for s in list1:
    if count(s) >= 3:
        list2.append(s)

with open("sort_words", 'w', encoding="utf-8") as file:
    file.write(str(list2))
