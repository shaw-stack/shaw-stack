#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
#Title and label
ypoints = np.array([3, 8, 1, 10, 5, 7])
print(plt.plot(ypoints, linestyle='dashed'))
plt.title('Sample graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
print(plt.show())


# In[2]:


#Marker,color,Linewidth
ypoints = np.array([3, 8, 1, 10, 5, 7])
print(plt.plot(ypoints, marker = 'o'))
print(plt.show())

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

print(plt.plot(xpoints, ypoints, 'violet'))

print(plt.show())


# In[3]:


print(plt.plot(xpoints, ypoints, linewidth='30', color='c'))
print(plt.show())

#Multiple lines and grid
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

print(plt.plot(y1))
print(plt.plot(y2))
plt.grid()
print(plt.show())


# In[4]:


#sub_plot
#plot 1
x = np.array([0,1,2,3,4,5])
y = np.array([3,8,1,10,9,4])
plt.subplot(1,2,2)
plt.plot(x,y)


# In[6]:


#plot 2
x= np.array([1, 2, 6, 8])
y= np.array([3, 8, 1, 10])
plt.subplot(1,2,2)
plt.scatter(x, y)
plt.show()

----------------------------------------------------------------------------------------------------------


# In[7]:


scatter 1
a=np.array([5, 7, 9,10])
b=np.array([2, 5, 8,2])

plt.scatter(a,b)
plt.show()


# In[ ]:




