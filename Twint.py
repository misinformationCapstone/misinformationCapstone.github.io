#!/usr/bin/env python
# coding: utf-8

# # Twint 
# ***This notebook utilizes the Twint library to pull tweets from current Verified Colorado Representatives***

# In[1]:


import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()


# ***House Of Representatives<br/>
# <br/>
# Diana DeGette (D)<br/>
# https://twitter.com/repdianadegette?lang=en <br/>
# 1st district<br/>
# <br/>
# Joe Neguse (D)<br/>
# https://twitter.com/repjoeneguse?lang=en <br/>
# 2nd district<br/>
# <br/>
# Lauren Boebert (R)? <br/>
# https://twitter.com/repboebert?lang=en <br/>
# 3rd district<br/>
# <br/>
# Ken Buck (R)<br/>
# https://twitter.com/repkenbuck?lang=en <br/>
# 4th district<br/>
# <br/>
# Doug Lamborn (R)<br/>
# https://twitter.com/repdlamborn?lang=en <br/>
# 5th district<br/>
# <br/>
# Jason Crow (D)<br/>
# https://twitter.com/repjasoncrow?lang=en <br/>
# 6th district<br/>
# <br/>
# Ed Perlmutter (D)<br/>
# https://twitter.com/repperlmutter?lang=en <br/>
# 7th district<br/>
# <br/>
# Senate<br/>
# <br/>
# Michael Bennet (D)<br/>
# https://twitter.com/senatorbennet?lang=en <br/>
# <br/>
# John Hickenlooper (D)<br/>
# https://twitter.com/hickenlooper?lang=en<br/>***
# 

# ***Diana DeGette (D)<br/>
# https://twitter.com/repdianadegette?lang=en <br/>
# 1st district<br/>***

# In[2]:


a = twint.Config()

a.Username = "RepDianaDeGette"
a.Limit = 20
a.Since = '2020-10-20'
a.Until = '2020-11-17'
a.Pandas = True


# In[3]:


twint.run.Search(a)


# In[4]:


df1 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df1.head(5)


# In[5]:


df1x = pd.DataFrame()
df1x = df1.copy()
df1x.drop(df1.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df1x.head()


# Joe Neguse (D)<br/>
# https://twitter.com/repjoeneguse?lang=en <br/>
# 2nd district<br/>

# In[6]:


b = twint.Config()

b.Username = "RepJoeNeguse"
b.Limit = 20
b.Since = '2020-10-20'
b.Until = '2020-11-17'
b.Pandas = True


# In[7]:


twint.run.Search(b)


# In[8]:


df2 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df2.head(50)


# In[9]:


df2x = pd.DataFrame()
df2x = df2.copy()
df2x.drop(df2.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df2x.head()


# ***Lauren Boebert (R)? <br/>
# https://twitter.com/repboebert?lang=en <br/>
# 3rd district<br/>***

# In[10]:


c = twint.Config()

c.Username = "RepBoebert"
c.Limit = 20
c.Since = '2020-10-20'
c.Until = '2020-11-17'
c.Pandas = True


# In[11]:


twint.run.Search(c)


# In[12]:


#df3 = twint.storage.panda.Tweets_df
#pd.set_option('display.max_columns',None)
#df3.head(50)


# ***Ken Buck (R)<br/>
# https://twitter.com/repkenbuck?lang=en <br/>
# 4th district<br/>***

# In[13]:


d = twint.Config()

d.Username = "RepKenBuck"
d.Limit = 20
d.Since = '2020-10-20'
d.Until = '2020-11-17'
d.Pandas = True


# In[14]:


twint.run.Search(d)


# In[15]:


df4 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df4.head(50)


# In[16]:


df4x = pd.DataFrame()
df4x = df4.copy()
df4x.drop(df4.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df4x.head()


# ***Doug Lamborn (R)<br/>
# https://twitter.com/repdlamborn?lang=en <br/>
# 5th district<br/>***

# In[17]:


e = twint.Config()

e.Username = "RepDLamborn"
e.Limit = 20
e.Since = '2020-10-20'
e.Until = '2020-11-17'
e.Pandas = True


# In[18]:


twint.run.Search(e)


# In[19]:


df5 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df5.head(50)


# In[20]:


df5x = pd.DataFrame()
df5x = df5.copy()
df5x.drop(df5.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df5x.head()


# ***Jason Crow (D)<br/>
# https://twitter.com/repjasoncrow?lang=en <br/>
# 6th district<br/>***

# In[21]:


f = twint.Config()

f.Username = "RepJasonCrow"
f.Limit = 20
f.Since = '2020-10-20'
f.Until = '2020-11-17'
f.Pandas = True


# In[22]:


twint.run.Search(f)


# In[23]:


df6 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df6.head(50)


# In[24]:


df6x = pd.DataFrame()
df6x = df6.copy()
df6x.drop(df6.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df6x.head()


# ***Ed Perlmutter (D)<br/>
# https://twitter.com/repperlmutter?lang=en <br/>
# 7th district<br/>***

# In[25]:


g = twint.Config()

g.Username = "RepPerlmutter"
g.Limit = 20
g.Since = '2020-10-20'
g.Until = '2020-11-17'
g.Pandas = True


# In[26]:


twint.run.Search(g)


# In[27]:


df7 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df7.head(50)


# In[28]:


df7x = pd.DataFrame()
df7x = df7.copy()
df7x.drop(df7.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df7x.head()


# ***Senate<br/>
# <br/>
# Michael Bennet (D)<br/>
# https://twitter.com/senatorbennet?lang=en <br/>***

# In[29]:


h = twint.Config()

h.Username = "SenatorBennet"
h.Limit = 20
h.Since = '2020-10-20'
h.Until = '2020-11-17'
h.Pandas = True


# In[30]:


twint.run.Search(h)


# In[31]:


df8 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df8.head(50)


# In[32]:


df8x = pd.DataFrame()
df8x = df8.copy()
df8x.drop(df8.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df8x.head()


# ***John Hickenlooper (D)<br/>
# https://twitter.com/hickenlooper?lang=en<br/>***

# In[33]:


i = twint.Config()

i.Username = "Hickenlooper"
i.Limit = 20
i.Since = '2020-10-20'
i.Until = '2020-11-17'
i.Pandas = True


# In[34]:


twint.run.Search(i)


# In[35]:


df9 = twint.storage.panda.Tweets_df
pd.set_option('display.max_columns',None)
df9.head(50)


# In[36]:


df9x = pd.DataFrame()
df9x = df9.copy()
df9x.drop(df9.columns.difference(['date','tweet','username','name','retweet','nlikes','nreplies','nretweets']), 1, inplace=True)
df9x.head()


# ## Filtering 
# ***This cell filters the previous dataframes for the most pertinent columns.***

# In[53]:


dfList = [df1x,df2x,df4x,df5x,df6x,df7x,df8x,df9x]
allTweetsdf = pd.DataFrame()
#for i in dfList:
allTweetsdf = allTweetsdf.append(dfList)
allTweetsdf = allTweetsdf.reset_index(drop=True)

pd.set_option('display.max_rows', None)
allTweetsdf.head(10000)


# In[ ]:





# In[63]:


allTweetsSumdf = pd.DataFrame(columns = allTweetsdf.columns)
uniqueUsers = []

for index, row in allTweetsdf.iterrows():
    if row['username'] not in uniqueUsers:
        uniqueUsers.append(row['username'])
        
        
likesList = []
likesCount = 0
repliesList = []
repliesCount = 0
retweetList = []
retweetCount = 0

colList = ['nlikes','nreplies','nretweets']
a = allTweetsdf[colList].iloc[0:35].sum()  
a = allTweetsdf[colList].iloc[35].sum()  
    
#allTweetsSumdf
print(allTweetsdf[colList].iloc[35])


# In[65]:


import altair as alt

base = alt.Chart(allTweetsdf).mark_bar(color='red',size=10).encode(
    x=alt.X('name',title='Name'),
    y=alt.Y('average(nlikes)',title='likes'),
    color= alt.Color('name', scale=alt.Scale(scheme='rainbow')),
    tooltip = ["nreplies","nretweets"]
).properties(
     title={
    "text": ["Number of Likes per Representative"]},
     width=300,
     height=300
)
base


# In[64]:


import altair as alt

base1 = alt.Chart(allTweetsdf).mark_bar(color='red',size=10).encode(
    x=alt.X('name',title='Name'),
    y=alt.Y('average(nreplies)',title='Replies'),
    color= alt.Color('name', scale=alt.Scale(scheme='rainbow')),
    tooltip = ["nlikes","nretweets"]
).properties(
     title={
    "text": ["Number of Replies per Representative"]},
     width=300,
     height=300
)
base1


# In[ ]:




