# a full stack data science project (from data collective to predictive modelling) 

# notebook imports
#matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('Survey.csv')

data.head()

data.tail()
group_data = data.groupby(['Monthly Family Income', 'Product Interested in Buying Online'])
group_data.count()

