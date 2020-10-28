#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Code for the Gambler's problem environment from the Sutton and Barto
  Reinforcement Learning: An Introduction Chapter 4.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta
"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

current_state = None
num_rows = 7
num_columns = 10
windspeed = [0,0,0,1,1,1,2,2,1,0]

def env_init():
    global current_state
    current_state = [0,3]


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
    global is_terminal
    if action[0] < -1 or action[0] > 1 or action[1] < -1 or action[1] > 1:
        print "Invalid action taken!!"
        print "action : ", action
        print "current_state : ", current_state
        exit(1)


    current_state[0] = current_state[0] + action[0]
    current_state[1] = current_state[1] + action[1]
    if current_state[0] < 0:
        current_state[0] = 0
    elif current_state[0] > num_columns-1:
        current_state[0] = num_columns-1
    if current_state[1] < 0:
        current_state[1] = windspeed[current_state[0]]
    elif current_state[1] + windspeed[current_state[0]] > num_rows-1:
        current_state[1] = num_rows-1
    else:
        current_state[1] += windspeed[current_state[0]]

    reward = -1.0
    is_terminal = False
    if current_state == [8,3]:
        is_terminal = True
        current_state = None
        reward = 0.0

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
