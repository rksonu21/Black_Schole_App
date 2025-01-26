#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import math
import scipy
from scipy.stats import norm


# In[3]:


def calculate_d1(S, K, T, r, sigma):
    return (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))


# In[4]:


def calculate_d2(d1, sigma, T):
    return d1 - sigma * math.sqrt(T)


# In[5]:


def calculate_call_price(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)


# In[6]:


def calculate_put_price(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, sigma, T)
    return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


# In[7]:


def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes option price.

    Parameters:
        S (float): Current stock price
        K (float): Strike price
        T (float): Time to maturity (in years)
        r (float): Risk-free interest rate (as a decimal)
        sigma (float): Volatility of the stock (as a decimal)
        option_type (str): 'call' or 'put'

    Returns:
        float: Option price
    """
    if option_type.lower() == 'call':
        return calculate_call_price(S, K, T, r, sigma)
    elif option_type.lower() == 'put':
        return calculate_put_price(S, K, T, r, sigma)
    else:
        raise ValueError("option_type must be 'call' or 'put'")



# In[8]:


# Streamlit App
st.title("Black-Scholes Option Pricing Calculator")

st.sidebar.header("Input Parameters")
S = st.sidebar.number_input("Current Stock Price (S)", value=100.0)
K = st.sidebar.number_input("Strike Price (K)", value=110.0)
T = st.sidebar.number_input("Time to Maturity (T, in years)", value=1.0)
r = st.sidebar.number_input("Risk-Free Rate (r, as a decimal)", value=0.05)
sigma = st.sidebar.number_input("Volatility (sigma, as a decimal)", value=0.2)
option_type = st.sidebar.selectbox("Option Type", ("call", "put"))

if st.sidebar.button("Calculate"):
    try:
        price = black_scholes(S, K, T, r, sigma, option_type=option_type)
        st.write(f"The {option_type.capitalize()} Option Price is: {price:.2f}")
    except ValueError as e:
        st.error(e)


# In[ ]:




