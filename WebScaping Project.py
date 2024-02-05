#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[3]:


print(soup)


# In[6]:


soup.find('table', class_ ='wikitable sortable')


# In[7]:


soup.find_all('table')[1]


# In[8]:


table = soup.find_all('table')[1]


# In[16]:


print(table)


# In[17]:


world_titles =table.find_all('th')


# In[18]:


world_titles


# In[19]:


world_table_titles =[title.text.strip() for title in world_titles]
print(world_table_titles)


# In[20]:


import pandas as pd


# In[21]:


df=pd.DataFrame(columns= world_table_titles)
df


# In[26]:


column_row =table.find_all('tr')


# In[30]:


for row in column_row[1:]:
    row_data=row.find_all('td')
    individual_row_data =[data.text.strip() for data in row_data]
    length=len(df)
    df.loc[length]=individual_row_data


# In[31]:


df


# In[35]:


df.to_csv(r'C:\Users\shree\OneDrive\Pictures\python tut\WebScraping\companies.csv', index =False)


# In[ ]:




