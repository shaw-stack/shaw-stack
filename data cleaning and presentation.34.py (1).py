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


# In[ ]:


print("\n Drop NaNrows:\n")
df=pd.read_excel()


# In[ ]:





# In[ ]:





# In[ ]:




