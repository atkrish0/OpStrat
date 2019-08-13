# OpStrat
Implementations of  widely used Options (Finanacial Derivatives) Trading Strategies, with a number of experimental features. Still under construction. To be converted to a library in the foreseeable future.


Strategies under consideration:

* Synthetic Long Put
* Option Strangle
* Long Short Combo
* Jade Lizard
* Iron Condor
* Iron Butterfly
* Collar
* Butterfly Spread
* Broken Wing Butterfly
* Bear Spread
* Bear Call Ladder

## Description:

#### Synthetic Long Put:

A synthetic long put is created when short stock position is combined with a long call of the same series.
The synthetic long put is so named because the established position has the same profit potential as long put.

#### Option Strangle:

A strangle is an investment strategy involving the purchase or sale of particular option derivatives that allows the holder to profit based on how much the price of the underlying security moves, with relatively minimal exposure to the direction of price movement. A purchase of particular options is known as a long strangle, while a sale of the same options is known as a short strangle.

#### Long Combo:

A Long Combo strategy is a Bullish Trading Strategy employed when a trader is expecting the price of a stock, he is holding to move up. It involves selling an OTM Put and buying an OTM Call. The strategy requires less capital as the cost of Call Option is covered by premium received from Put Option.

#### Jade Lizard:

In options trading, a jade lizard is a custom option strategy which consists of a bear vertical spread created using call options, with the addition of a put option sold at a strike price lower than the strike prices of the call spread. For one underlying security, same expiration date, this strategy consists of buying a call option at one strike price, selling another call option at a lower strike price, then selling an OTM put option at a strike price lower than that of both call options. The addition of the sale of a put option is consistent with the expected move of the underlying and results in additional premium collected. The jade lizard strategy takes advantage of the volatility skew inherently priced into options with naked puts trading richer in premium than naked calls and short call spreads trading richer in premium than short put spreads. This volatility skew effect allows the trader to collect more premium for the overall position and thus, increasing the position's probability of profit. 

#### Iron Condor:

An iron condor spread is constructed by selling one call spread and one put spread (same expiration day) on the same underlying instrument.
All four options are typically out-of-the-money (although it is not a strict requirement). When you sell the call and put spreads, you are buying the iron condor. The cash collected represents the maximum profit for the position.
It represents a 'market neutral' trade, meaning there is no inherent bullish or bearish bias.
