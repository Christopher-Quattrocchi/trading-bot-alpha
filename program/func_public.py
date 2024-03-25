from func_utils import get_ISO_times
from pprint import pprint
import pandas as pd
import numpy as np
from constants import RESOLUTION
import time

# Get relevant time periods from ISO from and to
ISO_TIMES = get_ISO_times()

# Get candles historical
def get_candles_historical(client, market):
  
  #Define output
  close_prices = []
  
  # Extract historical price data for each timeframe
  for timeframe in ISO_TIMES.keys():
    
    # confirm times needed
    tf_obj = ISO_TIMES[timeframe]
    from_iso = tf_obj["from_iso"]
    to_iso = tf_obj["to_iso"]
    
    # protect API
    time.sleep(0.2)
    
    # Get data
    candles = client.public.get_candles(
      market=market,
      resolution=RESOLUTION,
      from_iso=from_iso,
      to_iso=to_iso,
      limit=100 # unneccessary, but made explicit
    )
    
    # structure data
    for candle in candles.data["candles"]:
      close_prices.append({"datetime": candle["startedAt"], market: candle["close"] })
      
  #construct and return DataFrame
  close_prices.reverse() # flip to old to new
  #pprint(close_prices)
  return close_prices

#print(ISO_TIMES)

# Construct market prices
def construct_market_prices(client):
  
  # Declare vars
  tradeable_markets = []
  markets = client.public.get_markets()
  
  # find tradeable pairs
  for market in markets.data["markets"].keys():
    market_info = markets.data["markets"][market]
    if market_info["status"] == "ONLINE" and market_info["type"] == "PERPETUAL":
      tradeable_markets.append(market)
      
  # set initial DataFrame
  close_prices = get_candles_historical(client, tradeable_markets[0]) 
  
  #pprint(close_prices)
  df = pd.DataFrame(close_prices)
  df.set_index("datetime", inplace=True)
  
  #check
  #pprint(df.tail(), df.head())
  
  #Append other prices to DataFrame
  #Can limit amount to loop through here to save time in development
  for market in tradeable_markets[1:]:    #here we can limit for example 1:10
    close_prices_add = get_candles_historical(client, market)
    df_add = pd.DataFrame(close_prices_add)
    df_add.set_index("datetime", inplace=True)
    df = pd.merge(df, df_add, how="outer", on="datetime", copy=False) #db stuff kinda
    del df_add # keep memory clear
    
  #check any columns with NaNs
  nans = df.columns[df.isna().any()].tolist()
  if len(nans) > 0:
    print("Dropping columns: ")
    print(nans)
    df.drop(columns=nans, inplace=True)
    
  #Return result
  #print(df)
  return df