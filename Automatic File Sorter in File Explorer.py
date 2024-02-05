#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, shutil


# In[7]:


path =r"C:/Users/shree/OneDrive/Pictures/python tut/"


# In[10]:


file_name=os.listdir(path)
#showing content of folder


# In[9]:


folder_names =['xlsx files','image files','text files']

#check if folders exists and if not creates folder
for loop in range(0,3):
    if not os.path.exists(path+folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


# In[12]:


#moves files to appropriate folders
for file in file_name:
    if ".xlsx" in file and not os.path.exists(path+"xlsx files/" + file):
        shutil.move(path+file,path+"xlsx files/" + file)
    elif ".png" in file and not os.path.exists(path+"image files/" + file):
        shutil.move(path+file,path+"image files/" + file)
    elif ".txt" in file and not os.path.exists(path+"text files/" + file):
        shutil.move(path+file,path+"text files/" + file)
    
    


# In[ ]:




