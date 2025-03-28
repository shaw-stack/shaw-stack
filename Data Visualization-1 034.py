#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0,10])
ypoints = np.array([20,100])
print(plt.plot(xpoints,ypoints))
print(plt.show())


# In[2]:


x = np.array([0,5])
y = np.array([0,25])
print(plt.plot(x,y,marker='p'))
print(plt.show())


# In[3]:


xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])
print(plt.plot(xpoints,ypoints))
print(plt.show())


# In[4]:


ypoints = np.array([5,7,1,0,3])
print(plt.plot(ypoints))
print(plt.show())


# In[5]:


xpoints= np.array([3,8,1,4,9])
ypoints = np.array([5,7,1,0,3])
print(plt.plot(xpoints,ypoints))
print(plt.show())


# In[ ]:




