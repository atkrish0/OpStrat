"""
Created on Wed Jul 17 13:02:07 2019

@author: Atheesh Krishnan

A python library implementation of widely used Options Trading Strategies.
"""
# import libraries
import pandas as pd
import numpy as np

def synthetic_long_put(spot_price, long_call_strike_price, long_call_premium):
    # define parameters
    """spot_price = 250
    long_call_strike_price = 300
    long_call_premium = 0.90"""
    sT = np.arange(150, 350, 1)
    
    # call payoff
    # We define a function that calculates the payoff from buying a call option. 
    # The function takes sT which is a range of possible values of stock price at expiration, 
    # strike price of the call option and premium of the call option as input. 
    # It returns the call option payoff.
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    # long call payoff
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    
    # stock payoff
    stock_payoff = (sT - spot_price) * -1.0
    
    #synth
    synthetic_long_put_payoff = long_call_payoff + stock_payoff
    print("Maximum Profit: {}".format(max(synthetic_long_put_payoff)))
    print("Maximum Loss: {}".format(min(synthetic_long_put_payoff)))
    
