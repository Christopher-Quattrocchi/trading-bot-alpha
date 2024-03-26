from datetime import datetime, timedelta
import time
from pprint import pprint
from web3 import Web3
from func_utils import format_number

# get existing open positions
def is_open_positions(client, market):
  
  #protect api
  time.sleep(0.2)
  
  #Get positions
  all_positions = client.private.get_positions(
    market=market,
    status="OPEN"
  )
  
  # determine if open
  if len(all_positions.data["positions"]) > 0:
    return True
  else:
    return False


#check order status
def check_order_status(client, order_id):
  order = client.private.get_order_by_id(order_id)
  return order.data["order"]["status"]

# Place market order
def place_market_order(client, market, side, size, price, reduce_only):
  # Get Position Id
  account_response = client.private.get_account()
  position_id = account_response.data["account"]["positionId"]
  
  

  # Get expiration time
  server_time = client.public.get_time()
  expiration = datetime.fromisoformat(server_time.data["iso"].replace('Z','+00:00')) + timedelta(seconds=70) # .replace('Z','+00:00') replace("Z", "")

  # Place an order
  placed_order = client.private.create_order(
    position_id=position_id, # required for creating the order signature
    market=market,
    side=side,
    order_type="MARKET",
    post_only=False,
    size=size,
    price=price,  # should be above market price for some reason
    limit_fee='0.015',
    expiration_epoch_seconds=expiration.timestamp(),
    time_in_force="FOK", # fill or kill
    reduce_only=reduce_only
)
  
# Return result
  return placed_order.data


# Abort all open positions
def abort_all_positions(client):
  
  # Cancel all orders
  client.private.cancel_all_orders()
  
  # Protect API
  time.sleep(0.5)
  
  # Get markets for reference of tick size
  markets = client.public.get_markets().data
  
  #pprint(markets)
  
  # Protect API
  time.sleep(0.5)
  
  # Get all open positions
  positions = client.private.get_positions(status="OPEN")
  all_positions = positions.data["positions"]
  
  #pprint(all_positions)
  
  # Handle open positions
  close_order = []
  if len(all_positions) > 0:
    
    # for through each position
    for position in all_positions:
      
      # Determine market
      market = position["market"]
      
      # Determine side
      side = "BUY"
      if position["side"] == "LONG":
        side = "SELL"
        
      #print(market, side)
      
      #Get price
      price = float(position['entryPrice']) # must be init as a float
      accept_price = price * 1.7 if side == "BUY" else price * 0.3
      tick_size = markets["markets"][market]["tickSize"]
      accept_price = format_number(accept_price, tick_size)
      
      # place order to close
      order = place_market_order(
        client,
        market,
        side,
        position["sumOpen"],
        accept_price,
        True
      )
      
      # append the result
      close_order.append(order)
      
      # protect API
      time.sleep(0.2)
      
    #Return closed orders
    return close_order