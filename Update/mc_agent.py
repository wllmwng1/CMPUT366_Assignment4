#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017

"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

num_rows = 10
num_columns = 7
last_action = None
last_state = None
epsilon = 0.1
beta = 0.5

def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    global Q
    Q = [[0 for a in range(9)] for x in range(num_columns*num_rows)]
    #initialize the policy array in a smart way

def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    # pick the first action, don't forget about exploring starts
    global Q
    global last_state
    global last_action
    prob = np.random.rand()
    if prob < epsilon:
        action = np.random.randint(-1,2,2)
    else:
        actionindex = Q[state[0]+state[1]*num_rows].index(max(Q[state[0]+state[1]*num_rows]))
        action = [actionindex%3-1,-(actionindex/3)+1]
    last_state = state
    last_action = action
    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    global Q
    global last_state
    global last_action
    prob = np.random.rand()
    if prob < epsilon:
        action = np.random.randint(-1,2,2)
    else:
        actionindex = Q[state[0]+state[1]*num_rows].index(max(Q[state[0]+state[1]*num_rows]))
        action = [actionindex%3-1,-(actionindex/3)+1]
    actionindex = (1-action[1])*3+action[0]+1
    last_actionindex = (1-last_action[1])*3+last_action[0]+1
    change = beta*(reward + Q[last_state[0]+num_rows*last_state[1]][last_actionindex]- Q[state[0]+state[1]*num_rows][actionindex])
    Q[state[0]+state[1]*num_rows][actionindex] = Q[state[0]+state[1]*num_rows][actionindex] + change
    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi
    global Q
    global last_state
    global last_action
    last_actionindex = (1-last_action[1])*3+last_action[0]+1
    Q[last_state[0]+num_rows*last_state[1]][last_actionindex] = Q[last_state[0]+num_rows*last_state[1]][last_actionindex] + reward
    return

def agent_cleanup():
    """
    This function is not used
    """
    # clean up
    return

def agent_message(in_message): # returns string, in_message: string
    global Q
    """
    Arguments: in_message: string
    returns: The value function as a string.
    This function is complete. You do not need to add code here.
    """
    # should not need to modify this function. Modify at your own risk
    if (in_message == 'ValueFunction'):
        return pickle.dumps(np.max(Q, axis=1), protocol=0)
    else:
        return "I don't know what to return!!"
