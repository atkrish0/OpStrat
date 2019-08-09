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

#### Synthetic Long Put:

A synthetic long put is created when short stock position is combined with a long call of the same series.
The synthetic long put is so named because the established position has the same profit potential as long put.

The formula for calculating profit is given below:

    Maximum Profit = Unlimited
    Profit Achieved When Price of Underlying < Sale Price of Underlying - Premium Paid
    Profit = Sale Price of Underlying - Price of Underlying - Premium Paid

The formula for calculating maximum loss is given below:

    Max Loss = Premium Paid + Commissions Paid
    Max Loss Occurs When Price of Underlying = Strike Price of Long Call

#### Option Strangle:

A strangle is an investment strategy involving the purchase or sale of particular option derivatives that allows the holder to profit based on how much the price of the underlying security moves, with relatively minimal exposure to the direction of price movement. A purchase of particular options is known as a long strangle, while a sale of the same options is known as a short strangle.
