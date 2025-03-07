#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
d1={"name":["sai","sub","poo"],"age":[20,21,22]}
d2={"name":["rek","jai","gamo"],"age":[14,17,18]}


# In[14]:


df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame(d2)
print(df2)
newdf=df1.join(df2)
print(newdf)


# In[15]:


#merge
d1={"name":["sai","rishi","thara"],"age":[20,21,22]}
d2={"name":["ricky","sajid","tharun"],"age":[20,21,22]}


# df1=pd.DataFrame(d1

# In[22]:


df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame(d2)
print(df2)
newdf1=(df2.merge(df1,on="age")),
newdf2=(df1.merge(df2,on="age"))
print(newdf1)
print(newdf2)


# In[ ]:





# In[ ]:




