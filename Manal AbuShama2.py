# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H-rInZe38Gk_zg4laVKnPI3aT3WV8L51

# Import Classes
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

"""# declare and import Data"""

store=pd.read_csv('/content/Supermart Grocery Sales - Retail Analytics Dataset.csv')
store.info()

"""#Display columns"""

store.columns

"""# Show Data

* display data
"""

store

"""* unique"""

store.nunique()

"""* check nulls"""

store.isnull().sum()

"""* Describe"""

store.describe().T

store.describe(include='all').T

"""#Analysis Data

#1)Sales Category & Sub Category

1- Sales group by category
"""

store.groupby('Category')['Sales'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['Category'])['Sales'].sum().reset_index()
#sns.barplot(x=cat_sales.index,y=cat_sales.values)

#for i, value in enumerate(cat_sales.values):
  #px.(i,value,f'{value:.2f}',ha='center',va='bottom')

fig=px.bar(cat_sales, x='Category', y='Sales', title=' Sales by Category', text='Sales')
fig.show()

"""2- Sales group by sub category"""

store.groupby('Sub Category')['Sales'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['Sub Category'])['Sales'].sum().reset_index()

fig=px.bar(cat_sales, x='Sub Category', y='Sales', title=' Sales by Sub Category', text='Sales')
fig.show()

"""3- Sales group by category & sub category"""

cat_sales=store.groupby(['Category', 'Sub Category'])['Sales'].sum().reset_index()

fig=px.bar(cat_sales, x='Category', y='Sales', color='Sub Category', title=' Sales by Category & Sub Category', text='Sales')
fig.show()

"""4- Sales group by category Top 5"""

store.groupby(['Category'])['Sales'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Category'])['Sales'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Category', y='Sales', title=' Sales by Category Top 5', text='Sales')
fig.show()

"""5- Sales group by sub category Top 5"""

store.groupby(['Sub Category'])['Sales'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Sub Category'])['Sales'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Sub Category', y='Sales', title=' Sales by Sub Category Top 5', text='Sales')
fig.show()

"""6- Sales group by category & sub category Top 5"""

store.groupby(['Category', 'Sub Category'])['Sales'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Category', 'Sub Category'])['Sales'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Category', y='Sales', color='Sub Category', title=' Sales by Category & Sub Category Top 5', text='Sales')
fig.show()

"""#2)Prtofit Category & Sub Category

1- Profit group by category
"""

store.groupby('Category')['Profit'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['Category'])['Profit'].sum().reset_index()

fig=px.bar(cat_sales, x='Category', y='Profit', title=' Profit by Category', text='Profit')
fig.show()

"""2- Profit group by sub category"""

store.groupby('Sub Category')['Profit'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['Sub Category'])['Profit'].sum().reset_index()

fig=px.bar(cat_sales, x='Sub Category', y='Profit', title=' Profit by Sub Category', text='Profit')
fig.show()

"""3- Profit group by category & sub category"""

cat_sales=store.groupby(['Category', 'Sub Category'])['Profit'].sum().reset_index()

fig=px.bar(cat_sales, x='Category', y='Profit', color='Sub Category', title=' Profit by Category & Sub Category', text='Profit')
fig.show()

"""4- Profit group by category Top 5"""

store.groupby(['Category'])['Profit'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Category'])['Profit'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Category', y='Profit', title=' Profit by Category Top 5', text='Profit')
fig.show()

"""5- Profit group by sub category Top 5"""

store.groupby(['Sub Category'])['Profit'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Sub Category'])['Profit'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Sub Category', y='Profit', title=' Profit by Sub Category Top 5', text='Profit')
fig.show()

"""6- Profit group by category & sub category Top 5"""

store.groupby(['Category', 'Sub Category'])['Profit'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Category', 'Sub Category'])['Profit'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Category', y='Profit', color='Sub Category', title=' Profit by Category & Sub Category Top 5', text='Profit')
fig.show()

"""#3)Sales City & Region

1- Sales group by City
"""

store.groupby('City')['Sales'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['City'])['Sales'].sum().reset_index()

fig=px.bar(cat_sales, x='City', y='Sales', title=' Sales by City', text='Sales')
fig.show()

"""2- Sales group by Region"""

store.groupby('Region')['Sales'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['Region'])['Sales'].sum().reset_index()

fig=px.bar(cat_sales, x='Region', y='Sales', title=' Sales by Region', text='Sales')
fig.show()

"""3- Sales group by City & Region"""

cat_sales=store.groupby(['City', 'Region'])['Sales'].sum().reset_index()

fig=px.bar(cat_sales, x='City', y='Sales', color='Region', title=' Sales by City & Region', text='Sales')
fig.show()

"""4- Sales group by City Top 5"""

store.groupby(['City'])['Sales'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['City'])['Sales'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='City', y='Sales', title=' Sales by City Top 5', text='Sales')
fig.show()

"""5- Sales group by Region Top 5"""

store.groupby(['Region'])['Sales'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Region'])['Sales'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Region', y='Sales', title=' Sales by Region Top 5', text='Sales')
fig.show()

"""4- Sales group by City & Region Top 5"""

store.groupby(['City', 'Region'])['Sales'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['City', 'Region'])['Sales'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='City', y='Sales', color='Region', title=' Sales by City & Region Top 5', text='Sales')
fig.show()

"""#4)Profit City & Region

1- Profit group by City
"""

store.groupby('City')['Profit'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['City'])['Profit'].sum().reset_index()

fig=px.bar(cat_sales, x='City', y='Profit', title=' Profit by City', text='Profit')
fig.show()

"""2- Profit group by Region"""

store.groupby('Region')['Profit'].sum().sort_values(ascending=False)

cat_sales=store.groupby(['Region'])['Profit'].sum().reset_index()

fig=px.bar(cat_sales, x='Region', y='Profit', title=' Profit by Region', text='Profit')
fig.show()

"""3- Profit group by City & Region"""

cat_sales=store.groupby(['City', 'Region'])['Profit'].sum().reset_index()

fig=px.bar(cat_sales, x='City', y='Profit', color='Region', title=' Profit by City & Region', text='Profit')
fig.show()

"""4- Profit group by City Top 5"""

store.groupby(['City'])['Profit'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['City'])['Profit'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='City', y='Profit', title=' Profit by City Top 5', text='Profit')
fig.show()

"""5- Profit group by Region Top 5"""

store.groupby(['Region'])['Profit'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['Region'])['Profit'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='Region', y='Profit', title=' Profit by Region Top 5', text='Profit')
fig.show()

"""4- Profit group by City & Region Top 5"""

store.groupby(['City', 'Region'])['Profit'].sum().sort_values(ascending=False).head(5)

cat_sales=store.groupby(['City', 'Region'])['Profit'].sum().sort_values(ascending=False).head(5).reset_index()

fig=px.bar(cat_sales, x='City', y='Profit', color='Region', title=' Profit by City & Region Top 5', text='Profit')
fig.show()

"""#5)Catagory & Sub Category with City By Sales & Profit

1- Category & Sub Category group by City with Sales
"""

store.groupby(['City']).agg({'Sales': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Sales', ascending=False)

cat_sales=store.groupby(['City']).agg({'Sales': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Sales', ascending=False).reset_index()

fig=px.bar(cat_sales, x='City', y='Category', color='Sub Category', title=' Category & Sub Category by City according to Sales', text='Sales')
fig.show()

"""2- Category & Sub Category group by City with Profit"""

store.groupby(['City']).agg({'Profit': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Profit', ascending=False)

cat_sales=store.groupby(['City']).agg({'Profit': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Profit', ascending=False).reset_index()

fig=px.bar(cat_sales, x='City', y='Category', color='Sub Category', title=' Category & Sub Category by City according to Profit', text='Profit')
fig.show()

"""#6)Catagory & Sub Category with Customer with Sales & Profit

1- Category & Sub Category group by City with Sales
"""

store.groupby(['Customer Name']).agg({'Sales': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Sales', ascending=False)

cat_sales=store.groupby(['Customer Name']).agg({'Sales': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Sales', ascending=False).reset_index()

fig=px.bar(cat_sales, x='Customer Name', y='Category', color='Sub Category', title=' Category & Sub Category by Customer Name according to Sales', text='Sales')
fig.show()

"""2- Category & Sub Category group by Customer Name with Profit"""

store.groupby(['Customer Name']).agg({'Profit': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Profit', ascending=False)

cat_sales=store.groupby(['Customer Name']).agg({'Profit': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Profit', ascending=False).reset_index()

fig=px.bar(cat_sales, x='Customer Name', y='Category', color='Sub Category', title=' Category & Sub Category by Customer Name according to Profit', text='Profit')
fig.show()

"""3-Category & Sub Category group by Customer Name with Sales Top 5"""

store.groupby(['Customer Name']).agg({'Sales': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Sales', ascending=False).reset_index().head(5)

cat_sales=store.groupby(['Customer Name']).agg({'Sales': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Sales', ascending=False).reset_index().head(5)

fig=px.bar(cat_sales, x='Customer Name', y='Category', color='Sub Category', title=' Category & Sub Category by Customer Name according to Sales', text='Sales')
fig.show()

"""4-Category & Sub Category group by Customer Name with Profit Top 5"""

store.groupby(['Customer Name']).agg({'Profit': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Profit', ascending=False).reset_index().head(5)

cat_sales=store.groupby(['Customer Name']).agg({'Profit': 'sum','Category': 'first', 'Sub Category': 'first'}).sort_values(by='Profit', ascending=False).reset_index().head(5)

fig=px.bar(cat_sales, x='Customer Name', y='Category', color='Sub Category', title=' Category & Sub Category by Customer Name according to Profit', text='Profit')
fig.show()

"""#7)City & Region with Customer Name By Sales & Profit

1- City & Rigion group by Customer Name with Sales
"""

store.groupby(['Customer Name']).agg({'Sales': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Sales', ascending=False)

cat_sales=store.groupby(['Customer Name']).agg({'Sales': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Sales', ascending=False).reset_index()

fig=px.bar(cat_sales, x='Customer Name', y='City', color='Region', title=' City & Region by Customer Name according to Sales', text='Sales')
fig.show()

"""2- City & Region group by Customer Name with Profit"""

store.groupby(['Customer Name']).agg({'Profit': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Profit', ascending=False)

cat_sales=store.groupby(['Customer Name']).agg({'Profit': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Profit', ascending=False).reset_index()

fig=px.bar(cat_sales, x='Customer Name', y='City', color='Region', title=' City & Region by Customer Name Profit', text='Profit')
fig.show()

"""3- City & Region group by Customer Name with Sales Top 5"""

store.groupby(['Customer Name']).agg({'Sales': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Sales', ascending=False).reset_index().head(5)

cat_sales=store.groupby(['Customer Name']).agg({'Sales': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Sales', ascending=False).reset_index().head(5)

fig=px.bar(cat_sales, x='Customer Name', y='City', color='Region', title=' City & Region by Customer Name Sales', text='Sales')
fig.show()

"""4- City & Region group by Customer Name with Profit Top 5"""

store.groupby(['Customer Name']).agg({'Profit': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Profit', ascending=False).reset_index().head(5)

cat_sales=store.groupby(['Customer Name']).agg({'Profit': 'sum','City': 'first', 'Region': 'first'}).sort_values(by='Profit', ascending=False).reset_index().head(5)

fig=px.bar(cat_sales, x='Customer Name', y='City', color='Region', title=' City & Region by Customer Name Profit', text='Profit')
fig.show()