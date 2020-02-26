# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 20:15:22 2020

@author: Arne

"""
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from statannot import add_stat_annotation

file_in = r"..\..\data\katzenquartett.csv"
df = pd.read_csv(file_in, sep=',')

#%% plot distrivution

#sns.violinplot(data=df)

ax = sns.boxplot(data=df)
# for statistical annotations, 
# see: https://github.com/webermarcolivier/statannot
ax = sns.boxplot(data=df)
test_results = add_stat_annotation(ax, data=df,
                                   box_pairs=[("Fellpflege", "Größe"), ("Fellpflege", "Unabhängkeit"), ("Lautstärke", "Intelligenz")],
                                   test='t-test_paired', text_format='star', loc='inside', verbose=2)


#%%
corr = df.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9)) 

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


#%%

# Plot sepal with as a function of sepal_length across days
g = sns.lmplot(x="Größe", y="Intelligenz",
               truncate=True, height=5, data=df)

# Use more informative axis labels than are provided by default
#g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")

