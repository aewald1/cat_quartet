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

