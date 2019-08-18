"""
Created on Wed Jul 17 13:02:07 2019

@author: Atheesh Krishnan

A python library implementation of widely used Options (Financial Derivatives) Trading Strategies.
"""
# import libraries
import pandas as pd
import numpy as np
import mibian as mb
import matplotlib.pyplot as plt
import seaborn as sns

def synthetic_long_put(spot_price, long_call_strike_price, long_call_premium):
    sT = np.arange(0.7 * spot_price, 1.3 * spot_price, 1)
    
    # A function that calculates the payoff from buying a call option. 
    # The function takes sT which is a range of possible values of stock price at expiration, 
    # strike price of the call option and premium of the call option as input. 
    # It returns the call option payoff.

    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    
    stock_payoff = (sT - spot_price) * -1.0

    synthetic_long_put_payoff = long_call_payoff + stock_payoff  
    print("Maximum Profit: {}".format(max(synthetic_long_put_payoff)))
    print("Maximum Loss: {}".format(min(synthetic_long_put_payoff)))
    # Plot
    fig, ax = plt.subplots()
    ax.spines['top'].set_visible(False) # Top border removed 
    ax.spines['right'].set_visible(False) # Right border removed
    ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
    ax.plot(sT, synthetic_long_put_payoff, label='Synthetic Long Put')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.show()
    
def option_strangle(spot_price, long_put_strike_price, long_put_premium,\
                   long_call_strike_price, long_call_premium):
    
    sT = np.arange(0.7 * spot_price, 1.3 * spot_price, 1)
    
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    
    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, sT - strike_price, 0)- premium
    long_put_payoff = put_payoff(sT, long_put_strike_price, long_put_premium)
    
    strangle_payoff = long_call_payoff + long_put_payoff
    print("Maximum Profit: {}".format(max(strangle_payoff)))
    print("Maximum Loss: {}".format(min(strangle_payoff)))
    print("This strategy is suitable when the outlook on the stock is moderately bearish.")

    # Plot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')

    ax.plot(sT,long_call_payoff,'--',label='Long Call',color='r')
    ax.plot(sT,long_put_payoff,'--',label='Long Put',color='g')
    ax.plot(sT,strangle_payoff,label='Strangle')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.show()

def long_short_combo(spot_price, strike_price, premium_paid, premium_received):
    
    sT = np.arange(0.7*spot_price, 1.3*spot_price, 1)
    
    def long_call(sT, strike_price, premium_paid):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium_paid
    long_call_payoff = long_call(sT, strike_price, premium_paid)
    
    def short_put(sT, strike_price, premium_received):
        return np.where(sT > strike_price, 0, sT - strike_price) + premium_received
    short_put_payoff = short_put(sT, strike_price, premium_received)
    
    ls_combo_payoff = long_call_payoff + short_put_payoff
    
    print("Maximum Profit: {}".format(max(ls_combo_payoff)))
    print("Maximum Loss: {}".format(min(ls_combo_payoff)))
    # plot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT,ls_combo_payoff,color='b', label = 'Long Short Combo')
    ax.plot(sT,short_put_payoff,'--',color='r', label = 'Short Put')
    ax.plot(sT,long_call_payoff,'--',color='g', label = 'Long Call')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.grid()
    plt.show()
    
def jade_lizard(spot_price, long_call_strike_price, long_call_premium, \
                short_call_strike_price, short_call_premium, \
                short_put_strike_price, short_put_premium):
    
    sT = np.arange(0.9*spot_price, 1.1*spot_price, 1)
    
    # payoff on purchase of call options
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium) * -1.0
    
    # payoff on purchasing put options
    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 0) - premium
    
    short_put_payoff = put_payoff(sT, short_put_strike_price, short_put_premium) * -1.0
    
    jade_lizard_payoff = long_call_payoff + short_call_payoff + short_put_payoff
    
    print("Maximum Profit: {}".format(max(jade_lizard_payoff)))
    print("Maximum Loss: {}".format(min(jade_lizard_payoff)))
    # plot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT,long_call_payoff,'--',label='Long Strike Call',color='g')
    ax.plot(sT,short_call_payoff,'--',label='Short Strike Call',color='r')
    ax.plot(sT,short_put_payoff,'--',label='Short Strike Put',color='m')
    ax.plot(sT,jade_lizard_payoff,label='Jade Lizard Payoff')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit and Loss')
    plt.legend()
    plt.grid()
    plt.show()
    
def iron_condor(spot_price, long_call_strike_price, long_call_premium, \
                short_call_strike_price, short_call_premium, \
                long_put_strike_price, long_put_premium, \
                short_put_strike_price, short_put_premium):
    
    sT = np.arange(0.9*spot_price, 1.1*spot_price, 1)
    
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium) * -1.0 

    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 0) - premium

    long_put_payoff = put_payoff(sT, long_put_strike_price, long_put_premium)
    short_put_payoff = put_payoff(sT, short_put_strike_price, short_put_premium) * -1.0

    iron_condor_payoff = long_call_payoff + short_call_payoff + long_put_payoff + short_put_payoff

    print("Maximum Profit: {}".format(max(iron_condor_payoff)))
    print("Maximum Loss: {}".format(min(iron_condor_payoff)))

    # plot
    fig, ax = plt.subplots()
    ax.spines['top'].set_position('zero')
    ax.plot(sT,long_call_payoff,'--',label='Long 140 Strike Call',color='g')
    ax.plot(sT,short_call_payoff,'--',label='Short 130 Strike Call',color='r')
    ax.plot(sT,long_put_payoff,'--',label='Long 60 Strike Put',color='y')
    ax.plot(sT,short_put_payoff,'--',label='Short 70 Strike Put',color='m')
    ax.plot(sT,iron_condor_payoff,label='Iron Condor')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.grid()
    plt.show()

def iron_butterfly(spot_price, long_call_strike_price, long_call_premium, \
                   short_call_strike_price, short_call_premium, \
                   long_put_strike_price, long_put_premium, \
                   short_put_strike_price, short_put_premium):
    
    sT = np.arange(0.7*spot_price, 1.3*spot_price, 1)
    
    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium) * -1.0

    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 0) - premium

    long_put_payoff = put_payoff(sT, long_put_strike_price, long_put_premium)
    short_put_payoff = put_payoff(sT, short_put_strike_price, short_put_premium) * -1.0

    iron_butterfly_payoff = long_call_payoff + short_call_payoff + long_put_payoff + short_put_payoff 

    print("Maximum Profit: {}".format(max(iron_butterfly_payoff)))
    print("Maximum Loss: {}".format(min(iron_butterfly_payoff)))

    # plot
    fig, ax = plt.subplots(figsize=(10,5))
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT, iron_butterfly_payoff, color ='b', label ='Iron Butterfly Spread')
    ax.plot(sT, long_call_payoff,'--', color ='g', label = 'Long Call')
    ax.plot(sT, short_put_payoff,'--', color ='r', label = 'Short Call')
    ax.plot(sT, long_put_payoff,'--', color ='g',label = 'Long Put')
    ax.plot(sT, short_put_payoff,'--', color ='r',label = 'Short Put')
    plt.legend()
    plt.xlabel('Stock Price (sT)')
    plt.ylabel('Profit & Loss')
    plt.show()

def collar(spot_price, long_put_strike_price, long_put_premium, short_call_strike_price, short_call_premium):

    sT = np.arange(0, spot_price*0.7, 1)

    def call_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, premium, premium - sT + strike_price)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium)

    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 0) - premium 
    long_put_payoff = put_payoff(sT, long_put_strike_price, long_put_premium)

    collar_payoff = long_put_payoff + short_call_payoff
    print("Maximum Profit: {}".format(max(collar_payoff)))
    print("Maximum Loss: {}".format(min(collar_payoff)))

    fig, ax = plt.subplots()
    ax.spines['top'].set_visible(False) # Top border removed 
    ax.spines['right'].set_visible(False) # Right border removed
    ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
    ax.plot(sT, short_call_payoff,'--',label='Short Call',color='r')
    ax.plot(sT, long_put_payoff,'--',label='Long Put',color='g')
    ax.plot(sT, collar_payoff+sT-spot_price,label='Collar')
    plt.xlabel('Stock Price', ha='left')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.show()

def butterfly_spread(spot_price, higher_long_call_strike_price, lower_long_call_strike_price, \
              higher_long_call_premium, lower_long_call_premium, \
              short_call_strike_price, short_call_premium):
    
    sT = np.arange(10,60,1)

    def call_payoff (sT, strike_price, premium):
        return np.where(sT> strike_price, sT-strike_price, 0)-premium

    higher_long_call_payoff = call_payoff(sT, higher_long_call_strike_price, higher_long_call_premium)
    lower_long_call_payoff = call_payoff(sT, lower_long_call_strike_price, lower_long_call_premium)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium) * -1.0

    butterfly_spread_payoff = lower_long_call_payoff + higher_long_call_payoff + 2 * short_call_payoff

    print("Maximum Profit: {}".format(max(butterfly_spread_payoff)))
    print("Maximum Loss: {}".format(min(butterfly_spread_payoff)))

    # plot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT, butterfly_spread_payoff ,color='b', label= 'Butterfly Spread')
    ax.plot(sT, lower_long_call_payoff,'--', color='g',label='Lower Strike Long Call')
    ax.plot(sT, higher_long_call_payoff,'--', color='g', label='Higher Strike Long Call')
    ax.plot(sT, short_call_payoff, '--', color='r', label='Short call')
    plt.legend()
    plt.xlabel('Stock Price')
    plt.ylabel('Profit & Loss')
    plt.show()

def bull_call_spread(spot_price, long_call_strike_price, long_call_premium, \
                     short_call_strike_price, short_call_premium):
    
    sT = np.arange(0.95*spot_price, 1.05*spot_price, 1)

    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium

    long_call_payoff = call_payoff(sT, long_call_strike_price, long_call_premium)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium) * -1.0

    bull_call_spread_payoff = long_call_payoff + short_call_payoff

    print("Maximum Profit: {}".format(max(bull_call_spread_payoff)))
    print("Maximum Loss: {}".format(min(bull_call_spread_payoff)))

    # plot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT,long_call_payoff,'--',label='Long 920 Strike Call',color='g')
    ax.plot(sT,short_call_payoff,'--',label='Short 940 Strike Call ',color='r')
    ax.plot(sT,bull_call_spread_payoff,label='Bull Call Spread')
    plt.xlabel('Stock Price')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.show()

def broken_wing_butterfly(spot_price, long_call_strike_price_lower, long_call_premium_lower, \
                          long_call_strike_price_higher, long_call_premium_higher, \
                          short_call_strike_price, short_call_premium):
    
    sT = np.arange(0.9 * spot_price, 1.1 * spot_price, 1)

    def call_payoff(sT, strike_price, premium):
        return np.where(sT > strike_price, sT - strike_price, 0) - premium
    
    lower_long_call_strike_payoff = call_payoff(sT, long_call_strike_price_lower, long_call_premium_lower)
    higher_long_call_strike_payoff = call_payoff(sT, long_call_strike_price_higher, long_call_premium_higher)
    short_call_payoff = call_payoff(sT, short_call_strike_price, short_call_premium)*-1.0

    broken_wing_butterfly = lower_long_call_strike_payoff + higher_long_call_strike_payoff + \
                            (2 * short_call_payoff)

    print("Maximum Profit: {}".format(max(broken_wing_butterfly)))
    print("Maximum Loss: {}".format(min(broken_wing_butterfly)))

    # plot
    fig, ax = plt.subplots()
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT, broken_wing_butterfly ,color='b', label= 'Broken Wing Butterfly Spread')
    ax.plot(sT, lower_long_call_strike_payoff,'--', color='g',label='Lower Strike Long Call')
    ax.plot(sT, higher_long_call_strike_payoff,'--', color='g', label='Higher Strike Long Call')
    ax.plot(sT, short_call_payoff, '--', color='r', label='Short call')
    plt.legend()
    plt.grid()
    plt.xlabel('Stock Price')
    plt.ylabel('Profit & Loss')
    plt.show()

def bear_spread(spot_price, long_put_strike_price, long_put_premium, \
                short_put_strike_price, short_put_premium):
    
    sT = np.arange(spot_price * 0.7, spot_price * 1.3, 1)

    def put_payoff(sT, strike_price, premium):
        return np.where(sT < strike_price, strike_price - sT, 0) - premium

    long_put_payoff = put_payoff(sT, long_put_strike_price, long_put_premium)
    short_put_payoff = put_payoff(sT, short_put_strike_price, short_put_premium) * -1.0    

    bear_put_payoff = long_put_payoff + short_put_payoff 

    print("Maximum Profit: {}".format(max(bear_put_payoff)))
    print("Maximum Loss: {}".format(min(bear_put_payoff)))  

    # plot
    fig, ax = plt.subplots(figsize=(10,5))
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT, bear_Put_payoff, color ='b', label = 'Bear Put Spread')
    ax.plot(sT, long_put_payoff,'--', color ='g', label ='Long Put')
    ax.plot(sT, short_put_payoff,'--', color ='r', label ='Short Put')
    plt.legend()
    plt.xlabel('Stock Price (sT)')
    plt.ylabel('Profit & Loss')
    plt.show()
    
def bear_call_ladder(spot_price, OTM_long_call, premium_OTM_long_call, ATM_long_call, premium_ATM_long_call, ITM_short_call, premium_ITM_short_call):
    
    sT = np.arange(0.7*spot_price, 1.3*spot_price, 1)

    def call_payoff (sT, strike_price, premium):
        return np.where(sT> strike_price, sT-strike_price, 0)-premium

    OTM_long_call_payoff = call_payoff(sT, OTM_long_call, premium_OTM_long_call)
    ATM_long_call_payoff = call_payoff(sT, ATM_long_call, premium_ATM_long_call)
    ITM_Short_call_payoff = call_payoff(sT, ITM_short_call, premium_ITM_short_call)*-1.0

    bear_call_ladder = OTM_long_call_payoff + ATM_long_call_payoff + ITM_Short_call_payoff

    print("Maximum Profit: {}".format(max(bear_call_ladder)))
    print("Maximum Loss: {}".format(min(bear_call_ladder)))


