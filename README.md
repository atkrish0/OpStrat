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

#### Iron Butterfly:

The iron butterfly spread is a limited risk, limited profit trading strategy that is structured for a larger probability of earning a smaller limited profit when the underlying stock is perceived to have a low volatility. To setup an iron butterfly, the options trader buys a lower strike out-of-the-money put, sells a middle strike at-the-money put, sells a middle strike at-the-money call and buys another higher strike out-of-the-money call. This results in a net credit to put on the trade. 

#### Collar:

A collar is an options trading strategy that is constructed by holding shares of the underlying stock while simultaneously buying protective puts and selling call options against that holding. The puts and the calls are both out-of-the-money options having the same expiration month and must be equal in number of contracts. 

#### Butterfly Spread:

The butterfly spread is a neutral strategy that is a combination of a bull spread and a bear spread. It is a limited profit, limited risk options strategy. There are 3 striking prices involved in a butterfly spread and it can be constructed using calls or puts.

#### Broken Wing Butterfly:

A Broken Wing Butterfly is a long butterfly spread with long strikes that are not equidistant from the short strike. This leads to one side having greater risk than the other, which makes the trade slightly more directional than a standard long butterfly spread.

#### Bear Spread:

Bear spreads are comonly used when the undelying security is expeced to fall.

* Vertical Spread:

The vertical bear spread is a vertical spread in which options with a lower striking price are sold and options with a higher striking price are purchased. Depending on whether calls or puts are used, the vertical bear spread can be entered with a net credit or a net debit.

* Horizontal Spread:

The bear calendar spread and the diagonal bear spread are both time spread strategies used by option traders who believe that the price of the underlying security will remain stable in the near term but will eventually fall in the long term.

