<h2>Bitcoin_stats2</h2>

<h4>Author : RKT</h4>

### Descripton ###


![bitcoin-factory](https://user-images.githubusercontent.com/69615463/94761972-17a38d80-03c4-11eb-992a-a28746dab635.gif)


### Bitcoin statistics(stats2) ###

To install the Pi Blockchain tools library,open the command-line program and execute the following command:
<br>
<ul>
<li>sudo pip install blockchain</li>
</ul>

### Basic code ###

#!/usr/bin/python
<br>
#import blockchin library
<br>
from blockchain import statistics
<br>
#get the rkt object
<br>
rkt = statistics.get()
<br>
#get and print Bitcoin trade volume
<br>
print("Bitcoin Trade Volume:%s\n" % rkt.trade_volume_btc)
<br>
print("Bitcoin mined:%s\n" % rkt.btc_mined)
<br>
print("Bitcoin market price:%s\n" % rkt.market_price_usd)

### Git Clone ###

<ul>
<li>git clone https://github.com/r3k4t/bitcoin_stats2.git</li>
<li>cd bitcoin_stats2</li>
<li>sudo python3 bitcoin_stats2.py</li>
</ul>

### The following screenshots shows the bitcoin statistics : ###

![Screenshot at 2020-10-01 08-53-09](https://user-images.githubusercontent.com/69615463/94761800-92b87400-03c3-11eb-9390-c6696db21839.png)



