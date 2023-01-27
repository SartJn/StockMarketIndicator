#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance
vedl = yfinance.Ticker('VEDL.NS')
hist = vedl.history(period='5y')


# In[2]:


import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['High'], mode='lines'))
fig.show()


# In[3]:


fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close'], mode='lines+markers'))
fig.show()


# In[4]:


fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Open'], mode='lines+markers'))
fig.show()


# In[5]:


from plotly.subplots import make_subplots

fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=hist.index,y=hist['Close'],name='Price'),secondary_y=False)
fig2.add_trace(go.Bar(x=hist.index,y=hist['Volume'],name='Volume'),secondary_y=True)
fig2.show()


# In[6]:


fig2.update_yaxes(range=[0,7000000000],secondary_y=True)
fig2.update_yaxes(visible=False, secondary_y=True)


# In[7]:


fig3 = make_subplots(specs=[[{"secondary_y": True}]])
fig3.add_trace(go.Candlestick(x=hist.index,
                              open=hist['Open'],
                              high=hist['High'],
                              low=hist['Low'],
                              close=hist['Close'],
                             ))
fig3.add_trace(go.Bar(x=hist.index,y=hist['Volume'],name='Volume'),secondary_y=True)
fig3.update_yaxes(range=[0,7000000000],secondary_y=True)
fig3.update_yaxes(visible=False, secondary_y=True)
fig3.update_layout(yaxis_fixedrange = False)


# In[8]:


fig3.update_xaxes(rangebreaks = [
                       dict(bounds=['sat','mon']),
                       dict(values=["2021-12-25","2022-01-01"]) 
                                ])
