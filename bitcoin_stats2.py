#!/usr/pyhon
# Author : 
import os
import sys
import time
import blockchain
from blockchain import *
os.system("clear")
time.sleep(1)
print ("    ####### Author : Rahat Khan Tusar(RKT) #######")
time.sleep(2)
print (" ########## Github : https://github.com/r3k4t ##########")
time.sleep(3)
rkt = statistics.get()
print ("Trade volume btc                 : %s\n" % rkt.trade_volume_btc)
print ("Btc mined                        : %s\n" % rkt.btc_mined)
print ("Btc market price                 : %s\n" % rkt.market_price_usd)
print ("Estimated btc sent               : %s\n" % rkt.estimated_btc_sent)
print ("Total btc                        : %s\n" % rkt.total_btc)
print ("Miners revenue btc               : %s\n" % rkt.miners_revenue_btc)
print ("Total fees btc                   : %s\n" % rkt.total_fees_btc)
print ("Trade volume usd                 : %s\n" % rkt.trade_volume_usd)
print ("Miners revenue usd               : %s\n" % rkt.miners_revenue_usd)
print ("Difficulty                       : %s\n" % rkt.difficulty)
print ("Timestamp                        : %s\n" % rkt.timestamp)
print ("Hash rate                        : %s\n" % rkt.hash_rate)
print ("Next retarget                    : %s\n" % rkt.next_retarget)
print ("Total blocks                     : %s\n" % rkt.total_blocks)
print ("Mined blocks                     : %s\n" % rkt.mined_blocks)
print ("Number of transactions           : %s\n" % rkt.number_of_transactions)
print ("Minutes between blocks           : %s\n" % rkt.minutes_between_blocks)
print ("Estimated transaction volume usd : %s\n" % rkt.estimated_transaction_volume_usd)
