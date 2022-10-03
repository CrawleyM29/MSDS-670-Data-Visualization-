"""
Name: Mary Crawley
Project: Week 5 Mushrooms
Class: MSDS 670
School: Regis University
Date: October 02, 2022
"""
#Library
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

#File Import
mush = pd.read_csv('mushrooms.csv')

#----------Cleaning Data---------------------
print(mush.head)

for c in mush.columns:
    mush[c] = [ord(x) for x in mush[c]]
    mush[c] = pd.to_numeric(mush[c])

class_dict = {110:0, 100:1}
mush = mush.replace({"class" : class_dict})

print(mush.head)

#--------------------Exploring Data --------------
X = mush.loc[:, mush.columns != 'class']
y = mush ['class']

try:
    get_ipython().magic("matplotlib inline")
except:
    plt.ion()

# mush['odor'].plot.hist()
mush.hist(figsize=(20,20))

#-------------------Visuals------------------
plt.figure()
pd.Series(mush['class']).value_counts().sort_index().plot(kind = 'bar')
plt.ylabel("Count")
plt.xlabel("class")
plt.title('Number of poisonous/edible mushrooms (0=edible, 1=poisonous)');

mush_div = pd.melt(mush, "class", var_name="Characteristics")
fig, ax = plt.subplots(figsize=(10,5))
p = sns.violinplot(ax = ax, x="Characteristics", y="value", hue="class",
                   split = True, data=mush_div, inner = 'quartile', palette = 'Set1')
mush_no_class = mush.drop(["class"],axis = 1)
p.set_xticklabels(rotation = 90, labels = list(mush_no_class.columns))

#matplotlib barchart of number of poisonous/edible mushrooms (0=edible, 1=poisonous)
plt.figure()
pd.Series(mush['class']).value_counts().sort_index().plot(kind = 'bar')
plt.ylabel("Count")
plt.xlabel("class")
plt.title('Number of poisonous/edible mushrooms (0=edible, 1=poisonous)');

#matplotlib heatmap
plt.figure(figsize=(14,12))
sns.heatmap(mush.corr(),linewidths=.1,cmap="YlGnBu", annot=True)
plt.yticks(rotation=0);

#matplotlib barchart
