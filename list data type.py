#!/usr/bin/env python
# coding: utf-8

# In[2]:


course = ['linux','python','aws','devops','sql']


# In[3]:


print(course)


# In[ ]:





# In[ ]:





# In[5]:


#indexing


# In[6]:


print(course[3])


# In[7]:


print(course[3].title())


# In[8]:


course.append('linux')


# In[9]:


print(course)


# In[10]:


course.insert(5,'server')


# In[11]:


print(course)


# In[12]:


course[6] = 'cloud'


# In[13]:


print(course)


# In[15]:


del course['5','6']


# In[16]:


del course[5]


# In[17]:


print(course)


# In[18]:


x = course.pop()


# In[19]:


print(course)


# In[20]:


print(x)


# In[ ]:





# In[ ]:


# Difference between 'del' and 'pop' -----> del is used to delete an element permenently
                                      where as pop will be deleted tempororly that is shared in separate variable like x,y,z,...

