#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
pd.set_option('display.max_columns',10)
print("orginal data:\n")
df=pd.read_excel("performance bob.xlsx")
print(df)


# In[14]:


f=df['NAME'].str.strip()
f.to_excel("performance bob.name.xlsx")


# In[15]:


print("\n ReplaceValue:")
k=df.fillna(method='pad')
print(k)
print("\n updated list \n")
k.to_excel("performance bob.xlsx")


# In[7]:


print("\n Drop one particular column and its values:\n")
k.drop(['SOCIAL'],axis=1,inplace=True)
print(k)
print("\n updated list \n")
k.to_excel(print("\nDrop NaN rows:\n")
f.to_excel("performance bob.name.xlsx")
print(df)
x=df.dropna()
print(x)
print("\n updated list:\n")
f.to_excel("performance bob.name.xlsx")


# In[8]:


print("\nDrop NaN rows:\n")
f.to_excel("performance bob.name.xlsx")
print(df)
x=df.dropna()
print(x)
print("\n updated list:\n")
f.to_excel("performance bob.name.xlsx")


# In[ ]:


# Replacing the values
print("\n replace values:\n")
n=pd.read_excel("performance bob.name.xlsx")
print("\n orginal data:\n")
print(n)
y=n.replace({86})
print("\n replaced dataset:\n")
print(y)
print("\nupdated dataset:\n")
y.to_excel("perfoance bob.name.xlsx")


# In[ ]:




