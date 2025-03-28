#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([5, 7, 2, 15])

plt.bar(x,y)
plt.show()


# In[2]:


plt.bar([0.5,2.5,4.5,6.5,8.5],[50,40,70,80,20],
label="BMW",width=1)
plt.bar([1.5,3.5,5.5,7.5,9.5], [80,20,20,50,60],
label="Audi", color='c', width=1)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()


# In[3]:


#Horizontal bar
plt.barh(x,y)
plt.show()


# In[4]:


#Color option
plt.bar(x,y, color='red')
plt.show()


# In[5]:


#width option
plt.bar(x,y, color='g', width=0.1)
plt.show()


# In[6]:


#Histogram
x = np.random.normal(300, 20, 250)
plt.hist(x)
plt.show()


# In[7]:


#Pie chart
y = np.array([40, 30, 20, 10])
plt.pie(y)
plt.show()


# In[8]:


#With Labels
y = np.array([35, 25, 25, 15])
mylabels = ["MPMC", "PPML", "ContolSystem", "PSA"]
plt.pie(y, labels = mylabels)
plt.show()


# In[9]:


#Explode
y = np.array([35, 25, 25, 15])
mylabels = ["MPMC", "PPML", "ContolSystem", "PSA"]

myexplode = [0, 0, 0.3, 0]
plt.pie(y,labels=mylabels,explode=myexplode)
plt.show()


# In[ ]:




