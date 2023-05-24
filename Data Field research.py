#!/usr/bin/env python
# coding: utf-8

# # Data Field Research

# ## Business Understanding:
# Many people try to enter the data fields nowadays as it's a trinding career track and because of the emerging technologies that depend on data. And as it's sayed "Data is the Oil of this century".
# But while trying to enter this field many people can face too many obsticals that can lead them to change thier minds and try to shift to another career.
# 
# That's why I have started to work on this project in order to have a clear understanding of the best practices that can be made in order to start a successful career in the data field.

# In[1]:


#Importing liberaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## Data Understanding:

# ## Loading data into notebook

# In[2]:


# Importing the 2022 survey data from Stack overflow webstie 
df = pd.read_csv("survey_results_public.csv")
df.head()


# In[3]:


df.shape


# In[4]:


print(df.columns)


# In[12]:


df.describe()


# ## Data Preparation:

# ## Filtering data to only include Data Field job roles

# In[5]:


# Creating a filter to extract all the DevTypes that contain the word data in it.
filter_data_jobs = lambda row: 'data' in row.lower()
mask = df['DevType'].str.lower().str.contains('data ').fillna(False)
df = df[mask]


# In[6]:


df.head()


# ## Evaluation:

# ### 1- What is the most recommended way to enter the data science field?

# In[7]:


# Trying to find the most common ways to learn coding.
jobs = df['LearnCode'].str.split(";")
jobs = jobs.explode()

jobs_count = jobs.value_counts().reset_index()
jobs_count


# ### 2- What are the most common programming languages to work with in the data field?

# In[8]:


# Exploring the Top 10 Used languages in the data Science field.
LanguageHaveWorkedWith = df['LanguageHaveWorkedWith'].str.split(";")
LanguageHaveWorkedWith = LanguageHaveWorkedWith.explode()

LanguageHaveWorkedWith_count = LanguageHaveWorkedWith.value_counts().reset_index()
LanguageHaveWorkedWith_count[:10]


# In[9]:


# Exploring the Top 10 languages to be used in the future in the data Science field.
LanguageWantToWorkWith = df["LanguageWantToWorkWith"].str.split(";")
LanguageWantToWorkWith = LanguageWantToWorkWith.explode()
LanguageWantToWorkWith_count = LanguageWantToWorkWith.value_counts().reset_index()
LanguageWantToWorkWith_count[:10]


# ### 3- Which is most prefered working situation for data field workers?

# In[10]:


# comparing the work sitiuations in the data field.
# Also visualizing the data we have come.
values = df["RemoteWork"].value_counts()
values.plot.bar()


# ### 4- What is the Average time spent searching a day?

# In[11]:


df['TimeSearching'].value_counts().reset_index()


# In[ ]:





# In[ ]:




