#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=9562c881-baf7-4a5b-80e5-d0dc559416b5&as-searchtext=lapt"
req=requests.get(url)
req


# In[3]:


content=BeautifulSoup(req.content,'html.parser')
content
print(content.prettify())


# In[4]:


laptops=content.find_all('div',{'class':'_4rR01T'})
print(laptops)


# In[5]:


print(len(laptops))


# In[6]:


laptops=laptops[0]


# In[7]:


laptops


# In[8]:


name=content.find_all('div',{'class':'_4rR01T'})
#print(name)
#print(type(name))
#name=name[0]
#name=name.text
#print(name)
len(name)


# In[9]:


rating=content.find_all('div',{'class':'_3LWZlK'})
#ratings=rating[0].text
#print(ratings)
len(rating) 


# In[10]:


price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
print(price)


# In[11]:


price=content.find_all('div',{'class':'_30jeq3 _1_WHN1'})
#print(price)
#price=price[0].text
#print(price)
len(price)


# In[12]:


nm=[]
pr=[]
rt=[]


# In[13]:


for i in name:
    nm.append(i.text)
    
for i in price:
    pr.append(i.text)
    
for i in range(len(nm)):
    rt.append(rating[i].text)


# In[14]:


data={'NAME':nm,'PRICE':pr,'RATINGS':rt}
df=pd.DataFrame(data)
print(df)


# In[16]:


df.to_excel('newdatlap.xlsx',index=False)


# In[ ]:




