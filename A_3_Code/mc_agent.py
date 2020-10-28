#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: Skeleton code for Monte Carlo Exploring Starts Control Agent
           for use on A3 of Reinforcement learning course University of Alberta Fall 2017

"""

from utils import rand_in_range, rand_un
import numpy as np
import pickle

num_rows = 7
num_columns = 10
epsilon = 0.1
beta = 0.5
last_action = None
last_state = None

def agent_init():
    """
    Hint: Initialize the variables that need to be reset before each run begins
    Returns: nothing
    """
    global Q
    Q = [[0 for x in range(9)] for y in range(num_rows*num_columns)]
    #initialize the policy array in a smart way

def agent_start(state):
    """
    Hint: Initialize the variavbles that you want to reset before starting a new episode
    Arguments: state: numpy array
    Returns: action: integer
    """
    global last_action
    global last_state
    # pick the first action, don't forget about exploring starts
    action = np.random.randint(-1,2,size = 2)
    last_action = action
    last_state = state
    return action


def agent_step(reward, state): # returns NumPy array, reward: floating point, this_observation: NumPy array
    """
    Arguments: reward: floting point, state: integer
    Returns: action: integer
    """
    # select an action, based on Q
    print(state)
    global Q
    global last_state
    global last_action
    prob = np.random.rand()
    if prob < epsilon:
        action = np.random.randint(-1,2,size = 2)
    else:
        action = get_action(state)
    updateQ(last_state,last_action,reward,state,action)
    last_state = state
    last_action = action
    return action

def agent_end(reward):
    """
    Arguments: reward: floating point
    Returns: Nothing
    """
    # do learning and update pi
    updateQ(last_state,last_action,reward,last_state,last_action)

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

def get_action(s):
    global Q
    sindex = s[1]+s[0]*num_columns-1
    action = Q[sindex].index(max(Q[sindex]))
    if (s == [8,3]):
        print("Made it")
    x = action%3-1
    y = -(action/3)+1
    return [x,y]

def updateQ(ls,la,r,s,a):
    global Q
    lsindex = ls[1]+ls[0]*num_columns-1
    laindex = 1-la[0] + (1-la[1])*3
    sindex = s[1]+s[0]*num_columns-1
    aindex = 1-a[0] + (1-a[1])*3
    Q[lsindex][laindex] = Q[lsindex][laindex] + beta*(r+Q[sindex][aindex]-Q[lsindex][laindex])
    return
