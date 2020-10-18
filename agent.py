import numpy as np
import random
from enum import IntEnum

class Action(IntEnum):
    BUY = 0
    SELL = 1
    HOLD = 2

class Agent:
    def __init__(self):
        """
        Write your custom initialization sequence here.
        This can include loading models from file.
        """
        self.useless_var = 0

    def step(self, row):
        """
        Make a decision to be executed @ the open of the next timestep. 

        row is a numpy array with the same format as the training data

        Return a tuple (Action, fraction). Fraction means different 
        things for different actions...
        
        Action.BUY:  represents fraction of cash to spend on purchase 
        Action.SELL: represents fraction of owned shares to sell 
        Action.HOLD: value ignored.

        See the code below on how to return
        """
        #51, 68: 2195.58
        #52, 68: 2246.21
        #53, 68: 2382.09
        #53, 69: 2382.09
        
        # The ADX identifies a strong trend when the ADX is over 25 and a weak trend when the ADX is below 20.
        
        # if row[16] > 65:
        #     return(Action.SELL, 1)    
        # if row[16] < 17.3333:
        #     return(Action.BUY, 1)
        # elif row[16] > 40:
        #     return(Action.SELL, 1)
        # else:
        #     return(Action.HOLD, 0)

        # if row[101] < 53:
        #     return(Action.BUY, 1)
        # elif row[101] > 70:
        #     return(Action.SELL, 1)
        # else:
        #     return(Action.HOLD, 0)

        # 2410.53 
        # row[107] is slope
        # if row[107] < -0.00002 and row[101] < 53:
        #     return(Action.BUY, 1)
        # elif row[107] > 0.0003 and row[101] > 70:
        #     return(Action.SELL, 1)
        # else:
        #     return(Action.HOLD, 0)

        # if row[101] < 34 and row[33] < 0 and row[107] < -0.00002:
        #     return(Action.BUY, 1)
        # elif row[101] > 80 and row[33] > 20 and row[100] > 30:
        #     return(Action.SELL, 1)
        # else:
        #     return(Action.HOLD, 0)

        # if row[101] < 34 and row[33] < 0 and row[107] < -0.00002:
        #     return(Action.BUY, 1)
        # elif row[101] > 80 and row[33] > 20 and row[100] > 30:
        #     return(Action.SELL, 1)
        # else:
        #     return(Action.HOLD, 0)

        # CCI_14_0.015 is row 33 is Commodity Channel Index 
        # RSI_14 is row 101 is Relative strength index
        if row[101] < 32 and row[33] < -150:
            return(Action.BUY, 1)
        elif row[101] > 76 and row[33] > 150:
            return(Action.SELL, 1)
        else:
            return(Action.HOLD, 1)

