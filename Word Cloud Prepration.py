#!/usr/bin/env python
# coding: utf-8

# # Make Word Cloud

# This function gives an address of a text file anr return frequency of words in csv format!

# In[13]:


from hazm import *
from parsivar import Normalizer

def persian_normalizer(text):
    normal = Normalizer().normalize(text)
    return normal

#tokenozing
def persian_tokenization(text):
    tokens = word_tokenize(text)
    return tokens

#remove stopwords
stop = pd.read_table('C:\\Users\\MJavad\\Desktop\\persian.txt',encoding = 'utf-8') #address of stopwords list
stopwords = stop['li'].to_list()
def remove_persian_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output

#wordcloud
def ready_to_wordcloud(filepath):
    with open(filepath, 'r',encoding = 'utf-8') as file:
        data = file.read().replace('\n', '').replace('\u200c',' ',)
    text_normal = persian_normalizer(data)
    token = persian_tokenization(text_normal)
    no_stopword = remove_persian_stopwords(token)
    dic1 = {i:no_stopword.count(i) for i in no_stopword}
    final = pd.DataFrame(pd.Series(dic1),columns = ['Frequency']).sort_values('Frequency',ascending = False)
    final.to_excel('C:\\Users\\MJavad\\Desktop\\ابر کلمات شهرداری\\output2.xlsx',encoding = 'utf-8') #path of text file


# In[36]:


ready_to_wordcloud('C:\\Users\\MJavad\\Desktop\\ابر کلمات شهرداری\\فایل های خام\\قاسم زاده.txt') #path to save


# In[ ]:




