#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog , blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread


# In[2]:


example_file = glob.glob(r"wint_sky.png")[0]


# In[3]:


im = imread(example_file, as_grey=True)
plt.imshow(im,cmap=plt.get_cmap('gray'))
plt.show()


# In[4]:


blobs_log = blob_log(im,max_sigma=30 , num_sigma=10 , threshold=.1)
#compute radii in the 3rd column.
blobs_log[:,2]=blobs_log[:,2]*sqrt(2)
numrows = len(blobs_log)
print("number of stars counted: ",numrows)


# In[5]:


fig, ax = plt.subplots(1, 1)
plt.imshow(im, cmap=plt.get_cmap('gray'))
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)


# In[ ]:




