#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

num_rows = 7
num_columns = 10
windspeed = [0,0,0,1,1,1,2,2,1,0]
current_state = [None,None]

def env_init():
    global current_state
    current_state = [None,None]


def env_start():
    """ returns numpy array """
    global current_state
    current_state = [0,3]
    return current_state

def env_step(action):
    """
    Arguments
    ---------
    action : int
        the action taken by the agent in the current state

    Returns
    -------
    result : dict
        dictionary with keys {reward, state, isTerminal} containing the results
        of the action taken
    """
    global current_state
    """
    action: (int,int) UpDown LeftRight
    """
    wind = windspeed[current_state[0]]
    x = current_state[1]+action[1]
    y = current_state[0]+action[0]
    if x < 0:
        x = 0
    elif x >= num_rows:
        x = num_rows-1
    if y < 0:
        y = 0
    elif y >= num_columns:
        y = num_columns-1
    current_state = [x,y+wind]
    reward = -1
    is_terminal = False
    if current_state == [8,3]:
        print("End")
        reward = 0
        is_terminal = True
    result = {"reward": reward, "state": current_state, "isTerminal": is_terminal}
    return result

def env_cleanup():
    #
    return

def env_message(in_message): # returns string, in_message: string
    """
    Arguments
    ---------
    inMessage : string
        the message being passed

    Returns
    -------
    string : the response to the message
    """
    return ""
