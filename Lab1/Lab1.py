#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
import pymorphy2


# In[2]:


m = pymorphy2.MorphAnalyzer()
nltk.download('punkt')


# In[77]:


text = open('Text.txt', 'r', encoding='utf-8')
text = text.read()
print(text)


# In[78]:


sentences  = sent_tokenize(text)
for sentence in sentences:
    words = word_tokenize(sentence)
    for i in range(len(words) - 1):
        word_first = words[i]
        word_second = words[i + 1]
        parse_first = m.parse(word_first)[0]
        parse_second = m.parse(word_second)[0]
        if ((parse_first.tag.POS == 'NOUN') | (parse_first.tag.POS == 'ADJF')) & ((parse_second.tag.POS == 'NOUN') | (parse_second.tag.POS == 'ADJF')):
            if parse_first.tag.case == parse_second.tag.case:
                if parse_first.tag.gender == parse_second.tag.gender:
                    if parse_first.tag.number == parse_second.tag.number:
                        print(parse_first.normal_form, parse_second.normal_form)

