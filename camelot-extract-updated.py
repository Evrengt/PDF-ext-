#!/usr/bin/env python
# coding: utf-8

# In[1]:


import camelot
import os
import ctypes


# In[2]:


os.chdir('C:\\Users\\WIN10\\Desktop\\TASKS\\siftah')
tables2=camelot.read_pdf('YLB.pdf', flavor='stream', pages='0-8')
tables2


# In[3]:


tables2[2] 


# In[4]:


tables2[2].parsing_report


# In[5]:


df2=tables2[2].df
df2


# In[6]:


tables2[3]
tables2[3].parsing_report


# In[7]:


df3=tables2[3].df
df3


# In[8]:


tables2[5]
tables2[5].parsing_report


# In[9]:


df5=tables2[5].df
df5


# In[10]:


tables2[7]
tables2[7].parsing_report


# In[11]:


df7=tables2[7].df
df7


# In[12]:


tables2[9]
tables2[9].parsing_report


# In[13]:


df9=tables2[9].df
df9


# In[14]:


tables2[11]
tables2[11].parsing_report


# In[15]:


df11=tables2[11].df
df11


# In[16]:


tables2[13]
tables2[13].parsing_report


# In[17]:


df13=tables2[13].df
df13


# In[18]:


tables2[15]
tables2[15].parsing_report


# In[19]:


df15=tables2[15].df
df15

