from func_utils import get_ISO_times
from pprint import pprint
import pandas as pd
import numpy as np
from constants import RESOLUTION
import time

# Get relevant time periods from ISO from and to
ISO_TIMES = get_ISO_times()

print(ISO_TIMES)

# Construct market prices
def construct_market_prices(client):
  pass